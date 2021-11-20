import sys
from unittest import TestCase

from src.stack import Stack, StackWithMaxValue


class TestStackWithMaxValue(TestCase):

    def test_push(self):
        stack = StackWithMaxValue()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual([1, 2, 3], stack.as_list())

    def test_pop(self):
        stack = StackWithMaxValue()
        stack.push(1)
        self.assertEqual(1, stack.pop())
        self.assertEqual(None, stack.pop())
        self.assertEqual([], stack.as_list())

    def test_is_empty(self):
        stack = StackWithMaxValue()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_max(self):
        stack = StackWithMaxValue()
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.max())
        stack.pop()
        self.assertEqual(1, stack.max())
