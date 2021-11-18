from typing import List, TypeVar, Generic, Optional

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.__data: List[T] = []

    def push(self, item: T) -> None:
        self.__data.append(item)

    def pop(self) -> Optional[T]:
        return self.__data.pop() if self.__data else None

    def as_list(self) -> List[T]:
        return self.__data.copy()
