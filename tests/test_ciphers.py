""" test_ciphers.py:
        Tests ciphers...
"""
import unittest
import sys
import random
from string import ascii_lowercase
from julius.ciphers import encrypt


class CipherTester(unittest.TestCase):
    def setUp(self):
        pass

    def test_caesar_on_words(self, trials=10):
        for t in range(trials):
            orig = self.make_word(len_=random.randint(9, 18))
            for offset, key in enumerate(ascii_lowercase):
                self.assertEqual(
                    encrypt(orig, key),
                    ''.join(chr(ord('a')+(offset+ord(c)-ord('a')) % 26)
                            for c in orig)
                )

    def test_decryption_inverses(self):
        for _ in range(25):
            text = self.make_word(len_=random.randint(4, 9))
            key = self.make_word(len_=random.randint(1, 4))
            out = encrypt(encrypt(text, key), key, decrypting=True)
            self.assertEqual(text, out)

    @staticmethod
    def make_word(len_=5):
        return ''.join(random.choice(ascii_lowercase) for _ in range(len_))

    @staticmethod
    def make_sentence(len_=5):
        return ' '.join(CipherTester.make_word(len_=random.randint(3, 7))
                        for _ in range(len_))


if __name__ == "__main__":
    # Roughly equivalent to unittest.main().
    suite = unittest.TestLoader().loadTestsFromTestCase(CipherTester)
    unittest.TextTestRunner(verbosity=2, stream=sys.stderr).run(suite)
