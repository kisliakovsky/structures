import sys
from unittest import TestCase

from src.queue import Queue


class TestQueue(TestCase):

    def test_enqueue(self):
        queue = Queue[str]()
        queue.enqueue('A')
        queue.enqueue('B')
        queue.enqueue('C')
        self.assertEqual(['C', 'B', 'A'], queue.as_list())

    def test_dequeue(self):
        queue = Queue[str]()
        queue.enqueue('A')
        queue.enqueue('B')
        self.assertEqual('A', queue.dequeue())
        self.assertEqual('B', queue.dequeue())
        with self.assertRaises(IndexError):
            queue.dequeue()
        self.assertEqual([], queue.as_list())

    def test_peak(self):
        queue = Queue[str]()
        queue.enqueue('A')
        queue.enqueue('B')
        self.assertEqual('A', queue.peak())
        self.assertEqual(['B', 'A'], queue.as_list())
        queue.dequeue()
        queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peak()

    def test_is_empty(self):
        queue = Queue[str]()
        self.assertTrue(queue.is_empty())
        queue.enqueue('A')
        self.assertFalse(queue.is_empty())

    def test_len(self):
        queue = Queue[str]()
        queue.enqueue('A')
        queue.enqueue('B')
        queue.enqueue('C')
        self.assertEqual(3, len(queue))
