from typing import List


class Stack(object):
    # noinspection PyDefaultArgument
    def __init__(self, data: List = []):
        self.__data = data.copy()

    def push(self, item):
        self.__data.append(item)

    def is_empty(self) -> bool:
        return len(self.__data) == 0

    def pop(self):
        return self.__data.pop()

    def as_list(self) -> List:
        return self.__data.copy()
