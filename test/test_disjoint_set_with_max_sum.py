from unittest import TestCase

from src.disjoint_set import DisjointSetWithMaxSum


class TestDisjointSet(TestCase):

    def test_make_set(self):
        disjoint_set = DisjointSetWithMaxSum(10)
        disjoint_set.make_set(0, 1)
        self.assertEqual(0, disjoint_set.find(0))
        with self.assertRaises(ValueError):
            disjoint_set.find(1)

    def test_union(self):
        disjoint_set = DisjointSetWithMaxSum(10)
        disjoint_set.make_set(0, 1)
        with self.assertRaises(ValueError):
            disjoint_set.union(0, 5)
        for i in range(1, 10):
            disjoint_set.make_set(i, 1)
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
        disjoint_set = DisjointSetWithMaxSum(10)
        for i in range(10):
            disjoint_set.make_set(i, 1)
        disjoint_set.union(0, 5)
        disjoint_set.union(0, 7)
        disjoint_set.union(0, 9)
        disjoint_set.union(1, 2)
        disjoint_set.union(1, 3)
        disjoint_set.union(1, 6)
        disjoint_set.union(1, 8)
        self.assertEqual([
            (1, 0),
            (1, 1),
            (1, 1),
            (1, 1),
            (1, 4),
            (1, 0),
            (1, 1),
            (1, 0),
            (1, 1),
            (1, 0)
        ], disjoint_set.as_list())

    def test_max_sum(self):
        sizes = [10, 0, 5, 0, 3, 3]
        disjoint_set = DisjointSetWithMaxSum(6)
        for i, size in enumerate(sizes):
            disjoint_set.make_set(i, size)
        disjoint_set.union(5, 5)
        self.assertEqual(10, disjoint_set.max_sum())
        disjoint_set.union(5, 4)
        self.assertEqual(10, disjoint_set.max_sum())
        disjoint_set.union(4, 3)
        self.assertEqual(10, disjoint_set.max_sum())
        disjoint_set.union(3, 2)
        self.assertEqual(11, disjoint_set.max_sum())
