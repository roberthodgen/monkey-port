"""

This file handles incoming messages!

"""

import twilio.twiml
# from twilio.rest import TwilioRestClient
from flask import Flask, request

# import config


APP = Flask(__name__)

# Download the twilio-python library from http://twilio.com/docs/libraries
# Find these values at https://twilio.com/user/account
# CLIENT = TwilioRestClient(config.ACCOUNT_SID, config.AUTH_TOKEN)

@APP.route('/messages/incoming', methods=['GET', 'POST'])
def incoming_message():
    """ Respond to an incoming message. """

    from_number = request.values.get('From', None)
    if from_number is None:
        from_number = 'Unknown'

    sms_message = request.values.get('Body', None)
    if sms_message is None:
        sms_message = 'No message content.'

    response = twilio.twiml.Response()
    response.message(''.join(['Monkey see, monkey foo. Hello, ', from_number, "\n", sms_message]))
    return str(response)


if __name__ == '__main__':
    APP.run(debug=True)
