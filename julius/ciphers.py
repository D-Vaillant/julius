""" ciphers.py:
        Ciphers!
"""
import functools
import itertools
from string import ascii_lowercase, ascii_uppercase


def letter_to_num(letter: str,
                  is_inversed=False) -> int:
    """
    Takes a letter to a number!
    """
    if letter in ascii_uppercase:
        num = ord(letter) - ord('A')
    elif letter in ascii_lowercase:
        num = ord(letter) - ord('a')
    else:
        raise TypeError("Whoa there, that's not an appropriate value.")

    return (26-num)%26 if is_inversed else num  # Right?


def encrypt(plain_text: str,
            key: str,
            decrypting=False) -> str:
    """
    Encrypts plain_text using key, using a Vigenere cipher.

    Caesar is implemented if len(k) == 1, OTP if len(key) == len(plain_text).

    If plain_text contains non-alphabetical symbols, they're changed into
    alphabetical symbols. Sets them all to lower case as well!
    """
    l2num = functools.partial(letter_to_num, is_inversed=decrypting)
    key = [l2num(k) for k in key]
    out = [chr(ord('a') + (ord(letter) - ord('a') + shift_by)%26)
           for letter, shift_by in zip(plain_text, itertools.cycle(key))]
    return ''.join(out)
