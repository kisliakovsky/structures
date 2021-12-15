from unittest import TestCase

from src.hash_table import PolynomialHashing, StringKey


class TestPolynomialHashing(TestCase):

    def test_hash(self):
        hashing = PolynomialHashing(1000000007, 263)
        self.assertEqual(407643594, hashing.hash(StringKey('world')))
