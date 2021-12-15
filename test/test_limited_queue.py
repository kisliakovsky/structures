from unittest import TestCase

from src.queue import LimitedQueue, FullQueueError


class TestLimitedQueue(TestCase):

    def test_enqueue(self):
        queue = LimitedQueue[str](3)
        queue.enqueue('A')
        queue.enqueue('B')
        queue.enqueue('C')
        self.assertEqual(['C', 'B', 'A'], queue.as_list())

    def test_limit(self):
        queue = LimitedQueue[str](3)
        queue.enqueue('A')
        queue.enqueue('B')
        queue.enqueue('C')
        with self.assertRaises(FullQueueError):
            queue.enqueue('D')

    def test_is_full(self):
        queue = LimitedQueue[str](3)
        self.assertFalse(queue.is_full())
        queue.enqueue('A')
        self.assertFalse(queue.is_full())
        queue.enqueue('B')
        queue.enqueue('C')
        self.assertTrue(queue.is_full())

    def test_dequeue(self):
        queue = LimitedQueue[str](3)
        queue.enqueue('A')
        queue.enqueue('B')
        self.assertEqual('A', queue.dequeue())
        self.assertEqual('B', queue.dequeue())
        with self.assertRaises(IndexError):
            queue.dequeue()
        self.assertEqual([], queue.as_list())

    def test_peek(self):
        queue = LimitedQueue[str](3)
        queue.enqueue('A')
        queue.enqueue('B')
        self.assertEqual('A', queue.peek())
        self.assertEqual(['B', 'A'], queue.as_list())
        queue.dequeue()
        queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_is_empty(self):
        queue = LimitedQueue[str](3)
        self.assertTrue(queue.is_empty())
        queue.enqueue('A')
        self.assertFalse(queue.is_empty())
