from unittest import TestCase

from src.priority_queue import PriorityQueue, PrioritizedItem, MaxIntPriority


class TestPriorityQueue(TestCase):

    def test_enqueue(self):
        queue = PriorityQueue[MaxIntPriority, str]()
        queue.enqueue(PrioritizedItem(MaxIntPriority(14), 'A'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(5), 'B'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(7), 'C'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(18), 'D'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(42), 'E'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(12), 'F'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(11), 'G'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(18), 'H'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(29), 'I'))
        self.assertEqual([
            PrioritizedItem(MaxIntPriority(42), 'E'),
            PrioritizedItem(MaxIntPriority(29), 'I'),
            PrioritizedItem(MaxIntPriority(12), 'F'),
            PrioritizedItem(MaxIntPriority(18), 'D'),
            PrioritizedItem(MaxIntPriority(14), 'A'),
            PrioritizedItem(MaxIntPriority(7), 'C'),
            PrioritizedItem(MaxIntPriority(11), 'G'),
            PrioritizedItem(MaxIntPriority(5), 'B'),
            PrioritizedItem(MaxIntPriority(18), 'H')
        ], queue.as_list())

    def test_dequeue(self):
        queue = PriorityQueue[MaxIntPriority, str]()
        queue.enqueue(PrioritizedItem(MaxIntPriority(14), 'A'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(5), 'B'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(7), 'C'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(18), 'D'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(42), 'E'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(12), 'F'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(11), 'G'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(18), 'H'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(29), 'I'))
        self.assertEqual(PrioritizedItem(MaxIntPriority(42), 'E'), queue.dequeue())
        self.assertEqual(PrioritizedItem(MaxIntPriority(29), 'I'), queue.dequeue())
        self.assertEqual(PrioritizedItem(MaxIntPriority(18), 'H'), queue.dequeue())
        self.assertEqual(PrioritizedItem(MaxIntPriority(18), 'D'), queue.dequeue())
        self.assertEqual(PrioritizedItem(MaxIntPriority(14), 'A'), queue.dequeue())
        self.assertEqual(PrioritizedItem(MaxIntPriority(12), 'F'), queue.dequeue())
        self.assertEqual(PrioritizedItem(MaxIntPriority(11), 'G'), queue.dequeue())
        self.assertEqual(PrioritizedItem(MaxIntPriority(7), 'C'), queue.dequeue())
        self.assertEqual(PrioritizedItem(MaxIntPriority(5), 'B'), queue.dequeue())

    def test_peak(self):
        queue = PriorityQueue[MaxIntPriority, str]()
        queue.enqueue(PrioritizedItem(MaxIntPriority(14), 'A'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(5), 'B'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(7), 'C'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(18), 'D'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(42), 'E'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(12), 'F'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(11), 'G'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(18), 'H'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(29), 'I'))
        self.assertEqual(PrioritizedItem(MaxIntPriority(42), 'E'), queue.peak())
        self.assertEqual([
            PrioritizedItem(MaxIntPriority(42), 'E'),
            PrioritizedItem(MaxIntPriority(29), 'I'),
            PrioritizedItem(MaxIntPriority(12), 'F'),
            PrioritizedItem(MaxIntPriority(18), 'D'),
            PrioritizedItem(MaxIntPriority(14), 'A'),
            PrioritizedItem(MaxIntPriority(7), 'C'),
            PrioritizedItem(MaxIntPriority(11), 'G'),
            PrioritizedItem(MaxIntPriority(5), 'B'),
            PrioritizedItem(MaxIntPriority(18), 'H')
        ], queue.as_list())

    def test_change_priority(self):
        queue = PriorityQueue[MaxIntPriority, str]()
        queue.enqueue(PrioritizedItem(MaxIntPriority(14), 'A'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(5), 'B'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(7), 'C'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(18), 'D'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(42), 'E'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(12), 'F'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(11), 'G'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(18), 'H'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(29), 'I'))
        with self.assertRaises(IndexError):
            queue.change_priority(9, MaxIntPriority(20))
        queue.change_priority(8, MaxIntPriority(43))
        self.assertEqual(PrioritizedItem(MaxIntPriority(43), 'H'), queue.peak())

    def test_delete(self):
        queue = PriorityQueue[MaxIntPriority, str]()
        queue.enqueue(PrioritizedItem(MaxIntPriority(14), 'A'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(5), 'B'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(7), 'C'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(18), 'D'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(42), 'E'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(12), 'F'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(11), 'G'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(18), 'H'))
        queue.enqueue(PrioritizedItem(MaxIntPriority(29), 'I'))
        del queue[8]
        self.assertEqual([
            PrioritizedItem(MaxIntPriority(42), 'E'),
            PrioritizedItem(MaxIntPriority(29), 'I'),
            PrioritizedItem(MaxIntPriority(12), 'F'),
            PrioritizedItem(MaxIntPriority(18), 'D'),
            PrioritizedItem(MaxIntPriority(14), 'A'),
            PrioritizedItem(MaxIntPriority(7), 'C'),
            PrioritizedItem(MaxIntPriority(11), 'G'),
            PrioritizedItem(MaxIntPriority(5), 'B')
        ], queue.as_list())

    def test_is_empty(self):
        queue = PriorityQueue[MaxIntPriority, str]()
        self.assertTrue(queue.is_empty())
        queue.enqueue(PrioritizedItem(MaxIntPriority(14), 'A'))
        self.assertFalse(queue.is_empty())
