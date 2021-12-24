from unittest import TestCase

from src.tree import BinaryChildrenTree


class TestBinaryChildrenTree(TestCase):

    def test_walk_in_order(self):
        tree = BinaryChildrenTree([
            (4, 1, 2),
            (2, 3, 4),
            (5, -1, -1),
            (1, -1, -1),
            (3, -1, -1)
        ])
        self.assertEqual([1, 2, 3, 4, 5], tree.walk_in_order())

    def test_walk_pre_order(self):
        tree = BinaryChildrenTree([
            (4, 1, 2),
            (2, 3, 4),
            (5, -1, -1),
            (1, -1, -1),
            (3, -1, -1)
        ])
        self.assertEqual([4, 2, 1, 3, 5], tree.walk_pre_order())

    def test_walk_post_order(self):
        tree = BinaryChildrenTree([
            (4, 1, 2),
            (2, 3, 4),
            (5, -1, -1),
            (1, -1, -1),
            (3, -1, -1)
        ])
        self.assertEqual([1, 3, 2, 5, 4], tree.walk_post_order())

    def test_is_search_tree_on_simplest_search_tree(self):
        tree = BinaryChildrenTree([
            (2, 1, 2),
            (1, -1, -1),
            (3, -1, -1)
        ])
        self.assertTrue(tree.is_search_tree())

    def test_is_search_tree_on_search_tree(self):
        tree = BinaryChildrenTree([
            (4, 1, 2),
            (2, 3, 4),
            (6, 5, 6),
            (1, -1, -1),
            (3, -1, -1),
            (5, -1, -1),
            (7, -1, -1)
        ])
        self.assertTrue(tree.is_search_tree())

    def test_is_search_tree_on_search_tree_with_equal_values(self):
        tree = BinaryChildrenTree([
            (4, 1, 2),
            (1, -1, 3),
            (5, -1, -1),
            (2, -1, 4),
            (3, 5, -1),
            (2, -1, -1)
        ])
        self.assertTrue(tree.is_search_tree())

    def test_is_search_tree_on_simplest_non_search_tree(self):
        tree = BinaryChildrenTree([
            (1, 1, 2),
            (2, -1, -1),
            (3, -1, -1)
        ])
        self.assertFalse(tree.is_search_tree())

    def test_is_search_tree_on_non_search_tree(self):
        tree = BinaryChildrenTree([
            (4, 1, -1),
            (2, 2, 3),
            (1, -1, -1),
            (5, -1, -1)
        ])
        self.assertFalse(tree.is_search_tree())

    def test_is_search_tree_on_empty_tree(self):
        tree = BinaryChildrenTree([])
        self.assertTrue(tree.is_search_tree())

    def test_is_search_tree_on_linked_list(self):
        tree = BinaryChildrenTree([
            (1, -1, 1),
            (2, -1, 2),
            (3, -1, 3),
            (4, -1, 4),
            (5, -1, -1)
        ])
        self.assertTrue(tree.is_search_tree())
