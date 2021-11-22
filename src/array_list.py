from typing import TypeVar, Generic, List, Callable

T = TypeVar('T')


class ArrayList(Generic[T]):
    def __init__(self, n: int, reallocation_coefficient: int, potential_formula: Callable[[int, int], int]):
        if n < 0:
            raise ValueError("n must be positive")
        self.__n = n
        self.__reallocation_coefficient = reallocation_coefficient
        self.__index = -1
        self.__data: List[T] = [None for _ in range(n)]
        self.__potential_formula = potential_formula
        self.__append_actual_cost = 1

    def __getitem__(self, key: int) -> T:
        return self.__data[key]

    def __occupied_cells(self) -> List[T]:
        return [item for item in self.__data if item is not None]

    def __potential(self) -> int:
        return self.__potential_formula(len(self.__occupied_cells()), len(self.__data))

    def potential(self) -> int:
        return self.__potential()

    def append(self, item: T) -> int:
        self.__index += 1
        potential_before = self.__potential()
        delta_n = 0
        if self.__index == self.__n:
            self.__n *= self.__reallocation_coefficient
            delta_n = self.__n - len(self.__data)
            self.__data = self.__data[:] + [None for _ in range(delta_n)]
        self.__data[self.__index] = item
        return self.__append_actual_cost + delta_n + (self.__potential() - potential_before)

    def __len__(self):
        return len(self.__data)
