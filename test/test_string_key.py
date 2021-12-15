from unittest import TestCase

from src.hash_table import StringKey


class TestStringKey(TestCase):
    
    def test_to_ints(self):
        key = StringKey('world')
        self.assertEqual([119, 111, 114, 108, 100], list(key.to_ints()))
