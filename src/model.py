"""

Should store information...


"""

from google.appengine.ext import ndb

from datetime import timedelta, tzinfo

import config

import utilities


def question_key_id():
    """ Return a Key ID That diesn't already exist. """
    key_id = utilities.generate_id()
    # See if this key already exists...
    key_found = ndb.Key(Option, key_id).get()
    if key_found is not None:
        # Tru again!
        return question_key_id()
    return key_id


def option_key_id():
    """ Return a Key ID that doesn't already exist. """
    key_id = utilities.generate_id()
    # See if this key already exists...
    key_found = ndb.Key(Option, key_id).get()
    if key_found is not None:
        # Try again!
        return option_key_id()
    return key_id


class UTC(tzinfo):
    """ Defines a `tzinfo` subclass for UTC/Universal Coordindated Time.
    All dates are stored in NDB without time zone information. This UTC class
    is needed so `datetime.isoformat()` includes timezone information. """

    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return timedelta(0)


class Question(ndb.Model):
    """ This represents a Question. """
    # This is the question name
    name = ndb.StringProperty(required=True)
    # Record WHEN this record was truly created and last updated
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def create_question(cls, name):
        """ Create a new Question for a given name as `name`. """
        key_id = option_key_id()
        new_question = cls(name=name, id=key_id)
        if new_question.put():
            return new_question
        else:
            return False

    @classmethod
    def get(cls, key_id):
        """ Attempt to retrieve a Question from the NDB Datastore for a given
        Key ID. """
        question_key = ndb.Key(cls, key_id)
        return question_key.get()

    @property
    def created_utc(self):
        """ Return `created` with tzinfo set to `UTC`. """
        return self.created.replace(tzinfo=UTC())

    @property
    def updated_utc(self):
        """ Return `updated` with tzinfo set to `UTC`. """
        return self.updated.replace(tzinfo=UTC())

    @property
    def json(self):
        """ Return a JSON-encodable dict for this Question. """
        json_object = {
            'question': self.name,
            'id': self.key.id(),
            'options': list(),
            'response_count': 0
        }
        # Get all Options...
        query = Option.query(Option.question==self.key).order(Option.order)
        options = query.fetch(10)
        for option in options:
            option_json = option.json
            json_object['options'].append(option_json)
            json_object['response_count'] += option_json['response_count']
        return json_object


class Option(ndb.Model):
    """ This represents one of a Question's Options. """
    # This is the Option name
    name = ndb.StringProperty(required=True)
    # Stores which Question this Option belongs to...
    question = ndb.KeyProperty(required=True)
    # Saves the order in which to present Options
    order = ndb.IntegerProperty()
    # Record WHEN this record was truly created and last updated
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def create_option(cls, question_key, name, order=None):
        """ Create a new Option under a given Question identified by
        `question_key`. """
        key_id = option_key_id()
        new_option = cls(name=name,
            question=question_key,
            id=key_id)
        if order is not None:
            new_option.order = order
        if new_option.put():
            return new_option
        else:
            return False

    @property
    def created_utc(self):
        """ Return `created` with tzinfo set to `UTC`. """
        return self.created.replace(tzinfo=UTC())

    @property
    def updated_utc(self):
        """ Return `updated` with tzinfo set to `UTC`. """
        return self.updated.replace(tzinfo=UTC())

    @property
    def json(self):
        json_object = {
            'id': self.key.id(),
            'name': self.name
        }
        # Get a count of Responses
        query = Response.query(Response.option==self.key)
        json_object['response_count'] = query.count(limit=100)
        return json_object


class Response(ndb.Model):
    """ Represents a Response to a Question's Option. """
    # Stores which Option this Response was for
    option = ndb.KeyProperty(required=True)
    # Record WHEN this record was truly created and last updated
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def create_response(cls, option, phone_number):
        """ Create a Response for a given Question. """
        key = ndb.Key(
            cls,
            utilities.secure_hash(phone_number),
            parent=option.question
        )
        new_response = cls(
            key=key,
            option=option.key
        )
        return new_response.put()

    @property
    def created_utc(self):
        """ Return `created` with tzinfo set to `UTC`. """
        return self.created.replace(tzinfo=UTC())

    @property
    def updated_utc(self):
        """ Return `updated` with tzinfo set to `UTC`. """
        return self.updated.replace(tzinfo=UTC())
