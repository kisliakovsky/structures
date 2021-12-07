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
        with self.assertRaises(IndexError):
            queue.dequeue()
        self.assertEqual([], queue.as_list())

    def test_peak(self):
        queue = QueueWithMaxValue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(1, queue.peak())
        self.assertEqual([2, 1], queue.as_list())
        queue.dequeue()
        queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peak()

    def test_is_empty(self):
        queue = QueueWithMaxValue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

    def test_maximum(self):
        queue = QueueWithMaxValue()
        queue.enqueue(2)
        self.assertEqual(2, queue.maximum())
        queue.enqueue(7)
        self.assertEqual(7, queue.maximum())
        queue.enqueue(3)
        self.assertEqual(7, queue.maximum())
        queue.enqueue(1)
        self.assertEqual(7, queue.maximum())
        queue.enqueue(5)
        self.assertEqual(7, queue.maximum())
        queue.enqueue(2)
        self.assertEqual(7, queue.maximum())
        queue.enqueue(6)
        self.assertEqual(7, queue.maximum())
        queue.enqueue(2)
        self.assertEqual(7, queue.maximum())
        queue.dequeue()
        self.assertEqual(7, queue.maximum())
        queue.dequeue()
        self.assertEqual(6, queue.maximum())
        queue.dequeue()
        self.assertEqual(6, queue.maximum())
        queue.dequeue()
        self.assertEqual(6, queue.maximum())
        queue.dequeue()
        self.assertEqual(6, queue.maximum())
        queue.dequeue()
        self.assertEqual(6, queue.maximum())
        queue.dequeue()
        self.assertEqual(2, queue.maximum())
