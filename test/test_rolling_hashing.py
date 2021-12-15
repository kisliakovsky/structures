from unittest import TestCase

from src.search_string import RollingHashing


class TestRollingHashing(TestCase):

    def test_hash(self):
        hashing = RollingHashing('world', 1000000007, 263)
        self.assertEqual(407643594, hashing.hash())

    def test_shift_left(self):
        hashing = RollingHashing('world', 1000000007, 263)
        hashing.shift_left('a')
        self.assertEqual(791391073, hashing.hash())
