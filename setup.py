""" setup.py:
        Real simple utility.

        No "install to command line" option, because nobody has requested one.
"""
from typing import Union
from io import TextIOBase

import argparse
import julius


# Some utilities.
num_to_word = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
               '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}


class MissingKeyError(Exception):
    pass


# Compatibility, I guess?
try:
    FileNotFoundError()
except NameError:
    FileNotFoundError = IOError


def file_wrapper(file_loc: str) -> str:
    try:
        out = open(file_loc, 'r').read()
    except FileNotFoundError:
        out = file_loc
    return out


def safety_wrapper(key: str, safety_level: int) -> str:
    return key


# The argparse definition.
parser = argparse.ArgumentParser(prog='julius',
                                 description="Implements a Vigenere cipher.\n"
                                             "Sends the text to sys.out.")

parser.add_argument('plain_text',
                    nargs=1,
                    help="It really should be a file location, but you can "
                         "input strings as well.")

parser.add_argument('key',
                    nargs='?',
                    default=None,
                    help="If omitted, looks to optional arguments.\n"
                         "Please only use lowercase letters! "
                         "Can also open files.")

parser.add_argument('--caesar',
                    action='store_true',
                    help="If key is omitted, generate a random key of length 1 "
                         "and use that.\n[KEY]")

parser.add_argument('--key_length',
                    nargs='?',
                    default=0,
                    type=int,
                    help="If key is omitted, generate a random key of given "
                         "length and use that.\n[KEY]")

parser.add_argument('--otp',
                    action='store_true',
                    help="If key is omitted, generate a random key of length "
                         "equal to the length of the plain_text and save it to "
                         "the given file location.\nStores a file containing "
                         "key.\n[KEY]")

parser.add_argument('--decrypt',
                    action='store_true',
                    default=False,
                    help="Key cannot be omitted. Decrypts a text encrypted "
                         "with the given key.")


parser.add_argument('--unsafe',
                    nargs='?',
                    type=int,
                    default=0,
                    help="Allows for the preservation of non-alphanumeric characters.\n"
                         "Use with caution.")


args = parser.parse_args()

plain_text = file_wrapper(args.plain_text[0])


# Some plain_text text mungling.
for k, v in num_to_word.items():
    plain_text = plain_text.replace(k, v)

# (wipe it out)
plain_text = str(char for char in plain_text if char in string.letters).lower()


# This is the part that deals with keys.
try:
    if args.key is None:
        raise KeyError
    key = file_wrapper(args.key)
    key = safety_wrapper(key, 0)
except KeyError:
    if args.decrypt:
        raise MissingKeyError("Decryption requires a key!")

    if args.otp:
        key = julius.create_random_key(length=len(plain_text))
        with open("key_{}.txt".format(plain_text[:5]), 'w') as key_file:
            key_file.write(key)

    elif args.key_length > 0:
        key = julius.create_random_key(length=args.key_length)
    elif args.caesar:
        key = julius.create_random_key(length=1)
    else:
        raise MissingKeyError("Either specify a text file location, a key, or "
                              "use one of the KEY flags.")

print(julius.vigenere(plain_text, key, decrypting=args.decrypt))
