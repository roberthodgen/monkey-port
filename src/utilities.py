"""

Stores some helper functions.

"""

import random

import string

import hashlib

def generate_id():
    """ Returns a token of a given length. """
    return ''.join(random.SystemRandom().sample(
        'bcdfghjkmnpqrstvwxyz' + string.digits, 4))

def secure_hash(a_str):
    """ Return a secure hash of `a_str`. """
    return hashlib.sha256(a_str).hexdigest()
