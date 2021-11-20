import sys
from unittest import TestCase

from src.stack import Stack, StackWithMaxValue


class TestStack(TestCase):

    def test_push(self):
        stack = Stack[str]()
        stack.push('A')
        stack.push('B')
        stack.push('C')
        self.assertEqual(['A', 'B', 'C'], stack.as_list())

    def test_pop(self):
        stack = Stack[str]()
        stack.push('A')
        self.assertEqual('A', stack.pop())
        self.assertEqual(None, stack.pop())
        self.assertEqual([], stack.as_list())

    def test_peak(self):
        stack = Stack[str]()
        stack.push('A')
        self.assertEqual('A', stack.peak())
        self.assertEqual(['A'], stack.as_list())
        stack.pop()
        self.assertEqual(None, stack.peak())

    def test_is_empty(self):
        stack = Stack[str]()
        self.assertTrue(stack.is_empty())
        stack.push('A')
        self.assertFalse(stack.is_empty())
