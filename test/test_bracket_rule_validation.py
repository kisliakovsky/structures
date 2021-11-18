from unittest import TestCase

from src.validation import BracketRuleValidation


class TestBracketRuleValidation(TestCase):

    def test_successful_run(self):
        validation = BracketRuleValidation()
        self.assertEqual("Success", str(validation.run("[]")))
        self.assertEqual("Success", str(validation.run("()[]")))
        self.assertEqual("Success", str(validation.run("[()]")))
        self.assertEqual("Success", str(validation.run("(())")))
        self.assertEqual("Success", str(validation.run("{[]}()")))
        self.assertEqual("Success", str(validation.run("([](){([])})")))
        self.assertEqual("Success", str(validation.run("foo(bar)")))

    def test_error_run(self):
        validation = BracketRuleValidation()
        self.assertEqual('1', str(validation.run("{")))
        self.assertEqual('9', str(validation.run("{{{{{{{{{")))
        self.assertEqual('3', str(validation.run("{[}")))
        self.assertEqual('7', str(validation.run("{{[()]]")))
        self.assertEqual('5', str(validation.run("()[]}")))
        self.assertEqual('10', str(validation.run("foo(bar[i)")))

