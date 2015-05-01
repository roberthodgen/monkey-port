"""

This file handles incoming messages!

"""

from flask import Flask, request, Response

import json

import config

import utilities

import model


APP = Flask(__name__)

# Download the twilio-python library from http://twilio.com/docs/libraries
# Find these values at https://twilio.com/user/account
# CLIENT = TwilioRestClient(config.ACCOUNT_SID, config.AUTH_TOKEN)

@APP.route('/api/generate_id', methods=['GET', 'POST'])
def incoming_message():
    """ Respond to an incoming message. """
    response_object = {}
    response_object['id'] = utilities.generate_id()
    return json.dumps(response_object)


@APP.route('/api/poll/<poll_id>', methods=['GET'])
def get_api_poll(poll_id):
    """ Return a single Poll. """
    response = Response()
    question = model.Question.get(poll_id)
    if not isinstance(question, model.Question):
        response.status_code = 400
        return response
    response.data = json.dumps(question.json)
    return response


@APP.route('/api/poll', methods=['POST'])
def api_poll():
    """ POST to `/api/poll`;
    create a new Poll. """
    request_object = request.get_json(force=True, silent=True)
    response = Response()
    if not isinstance(request_object, dict):
        response.status_code = 400
        return response
    poll_question = request_object.get('question', None)
    if not poll_question:
        print 'request_object does not contain `question` key!'
        response.status_code = 400
        return response
    poll_options = request_object.get('responses', None)
    if not poll_options:
        print 'request_object does not contain `responses` key!'
        response.status_code = 400
        return response
    # Verify poll_options is an Array/List
    if not isinstance(poll_options, list) or len(poll_options) < 2:
        print 'request_object value of `responses` is not a list!'
        response.status_code = 400
        return response
    question = model.Question.create_question(poll_question)
    options = list()
    for index, poll_option in enumerate(poll_options):
        print index
        option = model.Option.create_option(question.key,poll_option, index)
        options.append(option.key.get().json)
    response.headers['Content-Type'] = 'application/json'
    response.data = json.dumps({
        'question': question.name,
        'id': question.key.id(),
        'responses': options,
        'response_count': len(options)
    })
    return response


if __name__ == '__main__':
    APP.run(debug=True)
