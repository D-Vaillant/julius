""" setup.py:
        Real simple utility.

        No "install to command line" option, because nobody has requested one.
"""
# import sys
import argparse

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
                    help="If key is omitted, generate a random key of length 1 "
                         "and use that.")

parser.add_argument('--key_length',
                    nargs='?',
                    type=int,
                    help="If key is omitted, generate a random key of given "
                         "length and use that.")

parser.add_argument('--otp',
                    help="If key is omitted, generate a random key of length "
                         "equal to the length of the plain_text and save it to "
                         "the given file location.")

parser.add_argument('--decrypt',
                    help="Key cannot be omitted. Decrypts a text encrypted "
                         "with the given key.")

args = parser.parse_args()
