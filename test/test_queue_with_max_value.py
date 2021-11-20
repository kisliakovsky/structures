from unittest import TestCase

from src.queue import QueueWithMaxValue


class TestQueueWithMaxValue(TestCase):

    def test_enqueue(self):
        queue = QueueWithMaxValue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual([3, 2, 1], queue.as_list())

    def test_dequeue(self):
        queue = QueueWithMaxValue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(None, queue.dequeue())
        self.assertEqual([], queue.as_list())

    def test_is_empty(self):
        queue = QueueWithMaxValue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

    def test_max(self):
        queue = QueueWithMaxValue()
        queue.enqueue(2)
        self.assertEqual(2, queue.max())
        queue.enqueue(7)
        self.assertEqual(7, queue.max())
        queue.enqueue(3)
        self.assertEqual(7, queue.max())
        queue.enqueue(1)
        self.assertEqual(7, queue.max())
        queue.enqueue(5)
        self.assertEqual(7, queue.max())
        queue.enqueue(2)
        self.assertEqual(7, queue.max())
        queue.enqueue(6)
        self.assertEqual(7, queue.max())
        queue.enqueue(2)
        self.assertEqual(7, queue.max())
        queue.dequeue()
        self.assertEqual(7, queue.max())
        queue.dequeue()
        self.assertEqual(6, queue.max())
        queue.dequeue()
        self.assertEqual(6, queue.max())
        queue.dequeue()
        self.assertEqual(6, queue.max())
        queue.dequeue()
        self.assertEqual(6, queue.max())
        queue.dequeue()
        self.assertEqual(6, queue.max())
        queue.dequeue()
        self.assertEqual(2, queue.max())
