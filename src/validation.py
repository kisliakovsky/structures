from src.stack import Stack


class ValidationResult(object):
    def __init__(self, error_index: int = None):
        self.__error_index = error_index

    def __str__(self):
        return "Success" if self.__error_index is None else str(self.__error_index)


class BracketRuleValidation(object):
    def __init__(self):
        self.__bracket_pairs = {')': '(', ']': '[', '}': '{'}
        self.__opening_brackets = set(self.__bracket_pairs.values())
        self.__closing_brackets = set(self.__bracket_pairs.keys())

    def run(self, chars) -> ValidationResult:
        stack = Stack()
        for i, char in enumerate(chars):
            if char in self.__opening_brackets:
                stack.push((i, char))
            elif char in self.__closing_brackets:
                paired_bracket = self.__bracket_pairs[char]
                if stack.is_empty():
                    return ValidationResult(i + 1)
                else:
                    j, opening_bracket = stack.pop()
                    if opening_bracket != paired_bracket:
                        return ValidationResult(i + 1)
        if stack.is_empty():
            return ValidationResult()
        else:
            j, opening_bracket = stack.pop()
            return ValidationResult(j + 1)
