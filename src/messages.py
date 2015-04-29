"""

This file handles incoming messages!

"""

import twilio.twiml

from twilio.rest import TwilioRestClient

from flask import Flask, request

import config

from google.appengine.ext import ndb

import re


APP = Flask(__name__)

# Download the twilio-python library from http://twilio.com/docs/libraries
# Find these values at https://twilio.com/user/account
CLIENT = TwilioRestClient(config.ACCOUNT_SID, config.AUTH_TOKEN)

@APP.route('/messages/incoming', methods=['GET', 'POST'])
def incoming_message():
    """ Respond to an incoming message. """

    response = twilio.twiml.Response()

    from_number = request.values.get('From', False)
    if not from_number:
        from_number = 'Unknown'

    sms_message = request.values.get('Body', False)
    if not sms_message:
        print 'No SMS message received!'
        sms_message = 'No message content.'

    # Attempt to find a response for this body...
    response_key_id = re.match("[bcdfghjkmnpqrstvwxyz0-9]{4}", sms_message)
    if response_key_id:
        response.message('Your response has been recorded, thanks for voting!\n\nText another poll\'s reponse code to vote in another.')
    else:
        response.message('Could not find poll response. Please send a 4-character response code.')

    return str(response)


if __name__ == '__main__':
    APP.run(debug=True)
