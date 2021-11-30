from unittest import TestCase

from src.disjoint_set import DisjointSet


class TestDisjointSet(TestCase):

    def test_make_set(self):
        disjoint_set = DisjointSet(10)
        disjoint_set.make_set(0, 'A')
        self.assertEqual(0, disjoint_set.find(0))
        with self.assertRaises(ValueError):
            disjoint_set.find(1)

    def test_union(self):
        disjoint_set = DisjointSet(10)
        disjoint_set.make_set(0, 'A')
        with self.assertRaises(ValueError):
            disjoint_set.union(0, 5)
        for i in range(1, 10):
            disjoint_set.make_set(i, chr(ord('A') + i))
        disjoint_set.union(0, 5)
        disjoint_set.union(0, 7)
        disjoint_set.union(0, 9)
        disjoint_set.union(1, 2)
        disjoint_set.union(1, 3)
        disjoint_set.union(1, 6)
        disjoint_set.union(1, 8)
        self.assertEqual(0, disjoint_set.find(5))
        self.assertEqual(0, disjoint_set.find(7))
        self.assertEqual(0, disjoint_set.find(9))
        self.assertEqual(4, disjoint_set.find(4))
        self.assertEqual(1, disjoint_set.find(2))
        self.assertEqual(1, disjoint_set.find(3))
        self.assertEqual(1, disjoint_set.find(6))
        self.assertEqual(1, disjoint_set.find(8))

    def test_as_list(self):
        disjoint_set = DisjointSet(10)
        for i in range(10):
            disjoint_set.make_set(i, chr(ord('A') + i))
        disjoint_set.union(0, 5)
        disjoint_set.union(0, 7)
        disjoint_set.union(0, 9)
        disjoint_set.union(1, 2)
        disjoint_set.union(1, 3)
        disjoint_set.union(1, 6)
        disjoint_set.union(1, 8)
        self.assertEqual([
            ('A', 0),
            ('B', 1),
            ('C', 1),
            ('D', 1),
            ('E', 4),
            ('F', 0),
            ('G', 1),
            ('H', 0),
            ('I', 1),
            ('J', 0)
        ], disjoint_set.as_list())
