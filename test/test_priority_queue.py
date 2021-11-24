from unittest import TestCase

from src.priority_queue import PriorityQueue, PrioritizedItem


class TestPriorityQueue(TestCase):

    def test_enqueue(self):
        queue = PriorityQueue[str]()
        queue.enqueue(PrioritizedItem[str](14, 'A'))
        queue.enqueue(PrioritizedItem[str](5, 'B'))
        queue.enqueue(PrioritizedItem[str](7, 'C'))
        queue.enqueue(PrioritizedItem[str](18, 'D'))
        queue.enqueue(PrioritizedItem[str](42, 'E'))
        queue.enqueue(PrioritizedItem[str](12, 'F'))
        queue.enqueue(PrioritizedItem[str](11, 'G'))
        queue.enqueue(PrioritizedItem[str](18, 'H'))
        queue.enqueue(PrioritizedItem[str](29, 'I'))
        self.assertEqual([
            PrioritizedItem[str](42, 'E'),
            PrioritizedItem[str](29, 'I'),
            PrioritizedItem[str](12, 'F'),
            PrioritizedItem[str](18, 'D'),
            PrioritizedItem[str](14, 'A'),
            PrioritizedItem[str](7, 'C'),
            PrioritizedItem[str](11, 'G'),
            PrioritizedItem[str](5, 'B'),
            PrioritizedItem[str](18, 'H')
        ], queue.as_list())

    def test_dequeue(self):
        queue = PriorityQueue[str]()
        queue.enqueue(PrioritizedItem[str](14, 'A'))
        queue.enqueue(PrioritizedItem[str](5, 'B'))
        queue.enqueue(PrioritizedItem[str](7, 'C'))
        queue.enqueue(PrioritizedItem[str](18, 'D'))
        queue.enqueue(PrioritizedItem[str](42, 'E'))
        queue.enqueue(PrioritizedItem[str](12, 'F'))
        queue.enqueue(PrioritizedItem[str](11, 'G'))
        queue.enqueue(PrioritizedItem[str](18, 'H'))
        queue.enqueue(PrioritizedItem[str](29, 'I'))
        self.assertEqual(PrioritizedItem[str](42, 'E'), queue.dequeue())
        self.assertEqual(PrioritizedItem[str](29, 'I'), queue.dequeue())
        self.assertEqual(PrioritizedItem[str](18, 'H'), queue.dequeue())
        self.assertEqual(PrioritizedItem[str](18, 'D'), queue.dequeue())
        self.assertEqual(PrioritizedItem[str](14, 'A'), queue.dequeue())
        self.assertEqual(PrioritizedItem[str](12, 'F'), queue.dequeue())
        self.assertEqual(PrioritizedItem[str](11, 'G'), queue.dequeue())
        self.assertEqual(PrioritizedItem[str](7, 'C'), queue.dequeue())
        self.assertEqual(PrioritizedItem[str](5, 'B'), queue.dequeue())

    def test_peak(self):
        queue = PriorityQueue[str]()
        queue.enqueue(PrioritizedItem[str](14, 'A'))
        queue.enqueue(PrioritizedItem[str](5, 'B'))
        queue.enqueue(PrioritizedItem[str](7, 'C'))
        queue.enqueue(PrioritizedItem[str](18, 'D'))
        queue.enqueue(PrioritizedItem[str](42, 'E'))
        queue.enqueue(PrioritizedItem[str](12, 'F'))
        queue.enqueue(PrioritizedItem[str](11, 'G'))
        queue.enqueue(PrioritizedItem[str](18, 'H'))
        queue.enqueue(PrioritizedItem[str](29, 'I'))
        self.assertEqual(PrioritizedItem[str](42, 'E'), queue.peak())
        self.assertEqual([
            PrioritizedItem[str](42, 'E'),
            PrioritizedItem[str](29, 'I'),
            PrioritizedItem[str](12, 'F'),
            PrioritizedItem[str](18, 'D'),
            PrioritizedItem[str](14, 'A'),
            PrioritizedItem[str](7, 'C'),
            PrioritizedItem[str](11, 'G'),
            PrioritizedItem[str](5, 'B'),
            PrioritizedItem[str](18, 'H')
        ], queue.as_list())

    def test_change_priority(self):
        queue = PriorityQueue[str]()
        queue.enqueue(PrioritizedItem[str](14, 'A'))
        queue.enqueue(PrioritizedItem[str](5, 'B'))
        queue.enqueue(PrioritizedItem[str](7, 'C'))
        queue.enqueue(PrioritizedItem[str](18, 'D'))
        queue.enqueue(PrioritizedItem[str](42, 'E'))
        queue.enqueue(PrioritizedItem[str](12, 'F'))
        queue.enqueue(PrioritizedItem[str](11, 'G'))
        queue.enqueue(PrioritizedItem[str](18, 'H'))
        queue.enqueue(PrioritizedItem[str](29, 'I'))
        with self.assertRaises(IndexError):
            queue.change_priority(9, 20)
        queue.change_priority(8, 43)
        self.assertEqual(PrioritizedItem[str](43, 'H'), queue.peak())

    def test_delete(self):
        queue = PriorityQueue[str]()
        queue.enqueue(PrioritizedItem[str](14, 'A'))
        queue.enqueue(PrioritizedItem[str](5, 'B'))
        queue.enqueue(PrioritizedItem[str](7, 'C'))
        queue.enqueue(PrioritizedItem[str](18, 'D'))
        queue.enqueue(PrioritizedItem[str](42, 'E'))
        queue.enqueue(PrioritizedItem[str](12, 'F'))
        queue.enqueue(PrioritizedItem[str](11, 'G'))
        queue.enqueue(PrioritizedItem[str](18, 'H'))
        queue.enqueue(PrioritizedItem[str](29, 'I'))
        del queue[8]
        self.assertEqual([
            PrioritizedItem[str](42, 'E'),
            PrioritizedItem[str](29, 'I'),
            PrioritizedItem[str](12, 'F'),
            PrioritizedItem[str](18, 'D'),
            PrioritizedItem[str](14, 'A'),
            PrioritizedItem[str](7, 'C'),
            PrioritizedItem[str](11, 'G'),
            PrioritizedItem[str](5, 'B')
        ], queue.as_list())

    def test_is_empty(self):
        queue = PriorityQueue[str]()
        self.assertTrue(queue.is_empty())
        queue.enqueue(PrioritizedItem[str](14, 'A'))
        self.assertFalse(queue.is_empty())
