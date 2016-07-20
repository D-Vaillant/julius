""" Caesar and Vignere.
        Caesar has a trivial implementation in Python by using substitution.
        but Vignere is trickier. I've wanted to use slicing tricks but it
        seems to be very... wasteful.

"""
from ciphers import encrypt
import string
import random


class OneTimePadError(Exception):
    pass


def create_random_key(length: int) -> str:
    """ Returns a random, lowercase string with len `length`. """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def caesar(plain_text: str, key=None, decrypting=False) -> str:
    if key is None:
        key = chr(ord('a') + random.randrange(26))
    else:
        key = key.lower()

    return encrypt(plain_text, key, decrypting)


def vigenere(plain_text: str, key=None, key_length=23, decrypting=False) -> str:
    if key is None:
        key = create_random_key(length=key_length)
    else:
        key = key.lower()

    return encrypt(plain_text, key, decrypting)


def otp(plain_text: str, key=None, decrypting=False) -> str:
    if key is None:
        key = create_random_key(length=len(plain_text))
    else:
        if len(key) < len(plain_text):
            raise OneTimePadError("Key has to be at least as long as the text.")
        key = key.lower()

    return encrypt(plain_text, key, decrypting)
