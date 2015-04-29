"""

Stores some helper functions.

"""

import random

import string

import hashlib

import config


def generate_id():
    """ Returns a token of a given length. """
    return ''.join(random.SystemRandom().sample(
        'bcdfghjkmnpqrstvwxyz' + string.digits, 4))

def secure_hash(a_str):
    """ Return a secure hash of `a_str`. """
    return hashlib.sha256(a_str).hexdigest()

def verbose_call_status(call_status):
	""" Return a verbose string (to speak) for a given call status as `call_status`. """
	return {
		'completed': 'The call has ended',
		'busy': 'A busy signal was received when trying to connect',
		'no-answer': 'The called party did not pick up before the timeout period passed',
		'failed': 'The call has failed',
		'canceled': 'The call was canceled before it was answered'
	}.get(call_status, 'Call status unknown')

def number_for_code(code):
	""" Return a phone number or False for a given code as `code`. """
	return config.IN_CALL_CODES.get(code, False)
