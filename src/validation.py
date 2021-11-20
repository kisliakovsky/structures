from typing import Dict, Set, Optional, Tuple

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
        self.__stacked_brackets: Optional[Stack[Tuple[int, str]]] = None

    def run(self, chars) -> ValidationResult:
        self.__stacked_brackets = Stack[str]()
        for i, char in enumerate(chars):
            if char in self.__opening_brackets:
                self.__stacked_brackets.push((i, char))
            elif char in self.__closing_brackets:
                index_and_bracket = self.__stacked_brackets.pop()
                if index_and_bracket is None or index_and_bracket[1] != self.__opening_bracket(char):
                    return ValidationResult(i + 1)
        index_and_bracket = self.__stacked_brackets.pop()
        return ValidationResult() if index_and_bracket is None else ValidationResult(index_and_bracket[0] + 1)

    def __opening_bracket(self, closing_bracket) -> str:
        return self.__bracket_pairs[closing_bracket]
