"""This module contains application examples of 'stack' data structure"""

from typing import Dict, Set, Tuple

from src.stack import Stack


class ValidationResult:
    def __init__(self, error_index: int = None) -> None:
        self.__error_index = error_index

    def __str__(self) -> str:
        return "Success" if self.__error_index is None else str(self.__error_index)


class BracketRuleValidation:
    def __init__(self) -> None:
        self.__bracket_pairs: Dict[str, str] = {')': '(', ']': '[', '}': '{'}
        self.__opening_brackets: Set[str] = set(self.__bracket_pairs.values())
        self.__closing_brackets: Set[str] = set(self.__bracket_pairs.keys())

    def run(self, chars) -> ValidationResult:
        stacked_brackets = Stack[Tuple[int, str]]()
        for i, char in enumerate(chars):
            if char in self.__opening_brackets:
                stacked_brackets.push((i, char))
            elif char in self.__closing_brackets:
                if stacked_brackets.is_empty():
                    return ValidationResult(i + 1)
                _, bracket = stacked_brackets.pop()
                if bracket != self.__opening_bracket(char):
                    return ValidationResult(i + 1)
        if stacked_brackets.is_empty():
            return ValidationResult()
        i, _ = stacked_brackets.pop()
        return ValidationResult(i + 1)

    def __opening_bracket(self, closing_bracket) -> str:
        return self.__bracket_pairs[closing_bracket]
