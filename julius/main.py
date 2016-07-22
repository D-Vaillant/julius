""" Caesar and Vignere.
        Everything is just a special case of the god function, ciphers.encrypt.

        Even decryption!
"""
from .ciphers import encrypt
import string
import random


class OneTimePadError(Exception):
    pass


def create_random_key(length: int) -> str:
    """ Returns a random, lowercase string with len `length`. """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))



def vigenere(plain_text: str, key: str, decrypting=False) -> str:
    # OOF
    key = key.lower()
    return encrypt(plain_text, key, decrypting)


def otp(plain_text: str, key: str, decrypting=False) -> str:
    if len(key) < len(plain_text):
        raise OneTimePadError("Key has to be at least as long as the text.")

    return vigenere(plain_text, key, decrypting)
