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
    """
    Tries to treat a string as a file location.

    If successfully, return the contents of the file.
    Otherwise, return the input string.
    """
    try:
        out = open(file_loc, 'r').read()
    except FileNotFoundError:
        out = file_loc
    return out


def safety_wrapper(key: str, safety_level = 0) -> str:
    """
    Strips a string of non-alphabetical characters, depending on the safety.
    PUNCTUATION, CAPITALIZATION
    """
    if safety_level > 2:
        safety_level -= 2
    return key

# The argparse definition.
parser = argparse.ArgumentParser(prog='julius',
                                 description="Implements a Vigenere cipher.\n"
                                             "Sends the text to sys.out.")

# The text to be ciphered through.
parser.add_argument('plain_text',
                    nargs=1,
                    help="It really should be a file location, but you can "
                         "input strings as well.")

# The key that we're ciphering with!
parser.add_argument('key',
                    nargs='?',
                    default=None,
                    help="If omitted, looks to optional KEY arguments.\n"
                         "Please only use lowercase letters! "
                         "Can also open files.")


# Key arguments.
parser.add_argument('--key_length',
                    nargs='?',
                    default=0,
                    type=int,
                    help="If key is omitted, generate a random key of given "
                         "length and use that.\n[KEY]")

parser.add_argument('--caesar',
                    action='store_true',
                    help="If key is omitted, generate a random key of length 1 "
                         "and use that.\n[KEY]")

parser.add_argument('--otp',
                    action='store_true',
                    help="If key is omitted, generate a random key of length "
                         "equal to the length of the plain_text and save it to "
                         "the given file location.\nStores a file containing "
                         "key.\n[KEY]")


# Use-case arguments.
parser.add_argument('--decrypt',
                    action='store_true',
                    help="Key cannot be omitted. Decrypts a text encrypted "
                         "with the given key.")

parser.add_argument('--unsafe',
                    nargs='?',
                    type=int,
                    default=0,
                    help="Allows for the preservation of non-alphanumeric characters.\n"
                         "Controls punctuation and capitalization.\n"
                         "0 - strip all\n1 - strip punctuation\n"
                         "2 - strip capitalization\n3 - strip none")


if __name__ == "__main__":
    args = parser.parse_args()

    # Some plain_text text mungling.
    plain_text = file_wrapper(args.plain_text[0])

    # Turn numerals into words.
    for k, v in num_to_word.items():
        plain_text = plain_text.replace(k, v)

    # Forcefully remove all non-alphabetical characters, make 'em lowercase.
    # TODO: Remove this in lieu of safety_wrapper.
    plain_text = str(char for char in plain_text
                     if char in string.letters).lower()


    # This is the part that deals with keys.
    if args.key is not None:
        # strip the key of punctuation and capitalization
        key = safety_wrapper(file_wrapper(args.key), 0)
    else:
        # Decryption requires a key to decrypt with, of course.
        if args.decrypt:
            raise MissingKeyError("Decryption requires a key!")
        # One-time pad.
        if args.otp:
            key = julius.create_random_key(length=len(plain_text))

            # Save the key to a keyfile of random name.
            with open("key_{}.txt".format(julius.create_random_key(5)), 'w')\
              as key_file:
                key_file.write(key)
                print("Saved key to {}.".format(key_file.name))
        elif args.key_length > 0:
            key = julius.create_random_key(length=args.key_length)
        elif args.caesar:
            key = julius.create_random_key(length=1)
        else:
            raise MissingKeyError("Either specify a key textfile location, a "
                                  "key, or use one of the KEY flags.")

    print(julius.vigenere(plain_text, key, decrypting=args.decrypt))
