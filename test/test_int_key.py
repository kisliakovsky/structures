from unittest import TestCase

from src.hash_table import IntKey


class TestIntKey(TestCase):
    
    def test_to_ints(self):
        key = IntKey(10)
        self.assertEqual([10], list(key.to_ints()))
