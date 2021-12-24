from unittest import TestCase

from src.tree import ParentsTree


class TestParentsTree(TestCase):

    def test_height(self):
        tree = ParentsTree([4, -1, 4, 1, 1])
        self.assertEqual(3, tree.height())
