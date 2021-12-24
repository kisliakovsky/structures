import operator
from unittest import TestCase

from src.stack import ComparableStack


class TestComparableStack(TestCase):

    def test_push(self):
        stack = ComparableStack[int](operator.lt)
        stack.push(None)
        stack.push(2)
        stack.push(None)
        stack.push(1)
        self.assertEqual([None, 2, 2, 2], stack.as_list())

    def test_pop_and_push(self):
        stack = ComparableStack[int](operator.lt)
        stack.pop_and_push(None)
        stack.pop_and_push(2)
        stack.pop_and_push(None)
        stack.pop_and_push(1)
        self.assertEqual([2], stack.as_list())

    def test_pop(self):
        stack = ComparableStack[int](operator.lt)
        stack.push(None)
        stack.push(2)
        stack.push(None)
        stack.push(1)
        self.assertEqual(2, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(None, stack.pop())
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self):
        stack = ComparableStack[int](operator.lt)
        with self.assertRaises(IndexError):
            stack.peek()
        stack.push(2)
        self.assertEqual(2, stack.peek())

    def test_is_empty(self):
        stack = ComparableStack[int](operator.lt)
        self.assertTrue(stack.is_empty())
        stack.push(2)
        self.assertFalse(stack.is_empty())

    def test_size(self):
        stack = ComparableStack[int](operator.lt)
        self.assertEqual(0, len(stack))
        stack.push(None)
        self.assertEqual(1, len(stack))
        stack.push(2)
        self.assertEqual(2, len(stack))
        stack.push(None)
        self.assertEqual(3, len(stack))
        stack.push(1)
        self.assertEqual(4, len(stack))

