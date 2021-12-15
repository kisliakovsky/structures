from unittest import TestCase

from src.search_string import SearchString


class TestSearchString(TestCase):

    def test_number_of_occurrences(self):
        string = SearchString('baaaaaaa')
        self.assertEqual([1, 2, 3], list(string.indices_of_occurrences('aaaaa')))
