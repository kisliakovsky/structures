from unittest import TestCase

from src.queue import Queue


class TestQueue(TestCase):

    def test_enqueue(self):
        queue = Queue[str]([])
        queue.enqueue('A')
        queue.enqueue('B')
        queue.enqueue('C')
        self.assertEqual(Queue(['A', 'B', 'C']), queue)

    def test_dequeue(self):
        queue = Queue[str]([])
        queue.enqueue('A')
        queue.enqueue('B')
        self.assertEqual('A', queue.dequeue())
        self.assertEqual('B', queue.dequeue())
        with self.assertRaises(IndexError):
            queue.dequeue()
        self.assertEqual(Queue([]), queue)

    def test_peek(self):
        queue = Queue[str]([])
        queue.enqueue('A')
        queue.enqueue('B')
        self.assertEqual('A', queue.peek())
        self.assertEqual(Queue(['A', 'B']), queue)
        queue.dequeue()
        queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_is_empty(self):
        queue = Queue[str]([])
        self.assertTrue(queue.is_empty())
        queue.enqueue('A')
        self.assertFalse(queue.is_empty())

    def test_len(self):
        queue = Queue[str]([])
        queue.enqueue('A')
        queue.enqueue('B')
        queue.enqueue('C')
        self.assertEqual(3, len(queue))
