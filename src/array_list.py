"""This module contains implementations of 'array list' data structure"""

from typing import TypeVar, Generic, List, Callable

Item = TypeVar('Item')


class ArrayList(Generic[Item]):
    def __init__(self, size: int, realloc_coeff: int, potential_formula: Callable[[int, int], int]):
        if size < 0:
            raise ValueError("n must be positive")
        self.__initial_size = size
        self.__realloc_coeff = realloc_coeff
        self.__index = -1
        self.__data: List[Item] = [None for _ in range(size)]
        self.__potential_formula = potential_formula
        self.__append_actual_cost = 1

    def __getitem__(self, key: int) -> Item:
        return self.__data[key]

    def __occupied_cells(self) -> List[Item]:
        return [item for item in self.__data if item is not None]

    def __potential(self) -> int:
        return self.__potential_formula(len(self.__occupied_cells()), len(self.__data))

    def potential(self) -> int:
        return self.__potential()

    def append(self, item: Item) -> int:
        self.__index += 1
        potential_before = self.__potential()
        delta_n = 0
        if self.__index == self.__initial_size:
            self.__initial_size *= self.__realloc_coeff
            delta_n = self.__initial_size - len(self.__data)
            self.__data = self.__data[:] + [None for _ in range(delta_n)]
        self.__data[self.__index] = item
        return self.__append_actual_cost + delta_n + (self.__potential() - potential_before)

    def __len__(self):
        return len(self.__data)
