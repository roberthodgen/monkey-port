"""

This file handles incoming messages!

"""

from flask import Flask

import json

import utilities

# import config


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


if __name__ == '__main__':
    APP.run(debug=True)
