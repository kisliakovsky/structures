"""This module contains implementations of "hash table" data structure"""

import operator
from abc import ABC, abstractmethod
from functools import reduce
from typing import TypeVar, Generic, Iterator, List, Tuple, Optional

GenericKey = TypeVar('GenericKey', bound='Key')
Value = TypeVar('Value')


class Key(ABC):

    @abstractmethod
    def to_ints(self) -> Iterator[int]:
        pass


class IntKey(Key):
    def __init__(self, key: int):
        self.__key = key

    def to_ints(self) -> Iterator[int]:
        yield self.__key

    def __eq__(self, other: 'IntKey'):
        return self.__key == other.__key if isinstance(other, IntKey) else False


class StringKey(Key):
    def __init__(self, key: str):
        self.__key = key

    def to_ints(self) -> Iterator[int]:
        for char in self.__key:
            yield ord(char)

    def __eq__(self, other: 'StringKey') -> bool:
        return self.__key == other.__key if isinstance(other, StringKey) else False


class AbstractHashTable(ABC, Generic[GenericKey, Value]):

    @abstractmethod
    def put(self, key: GenericKey, value: Value) -> None:
        pass

    @abstractmethod
    def get(self, key: GenericKey) -> Optional[Value]:
        pass

    @abstractmethod
    def bucket(self, i: int) -> List[Tuple[GenericKey, Value]]:
        pass


class Hashing(ABC, Generic[GenericKey]):

    @abstractmethod
    def hash(self, key: GenericKey) -> int:
        pass


class PolynomialHashing(Hashing[GenericKey]):
    def __init__(self, modulus: int = 1000000007, base: int = 263):
        self.__modulus: int = modulus
        self.__base: int = base
        self.__base_pows: List[int] = [1, self.__base]

    def hash(self, key: GenericKey) -> int:
        hash_sum = reduce(
            operator.add,
            map(
                lambda item: ((item[1] % self.__modulus) * self.__x_pow(item[0])) % self.__modulus,
                enumerate(key.to_ints())
            )
        )
        return hash_sum % self.__modulus

    def __x_pow(self, exponent: int) -> int:
        if exponent == len(self.__base_pows) and exponent > 1:
            x_pow = (self.__base_pows[-1] * self.__base) % self.__modulus
            self.__base_pows.append(x_pow)
        return self.__base_pows[exponent]


class HashTable(AbstractHashTable[GenericKey, Value]):
    def __init__(self, number_of_buckets: int, hashing: Hashing[GenericKey]):
        self.__number_of_buckets: int = number_of_buckets
        self.__hashing: Hashing[GenericKey] = hashing
        self.__data: List[List[Tuple[GenericKey, Value]]] = [[] for _ in range(number_of_buckets)]

    def put(self, key: GenericKey, value: Value) -> None:
        bucket = self.__bucket(key)
        i = self.__key_index(key)
        if i is not None:
            bucket[i] = (key, value)
        else:
            bucket.insert(0, (key, value))

    def __key_index(self, key: GenericKey) -> Optional[int]:
        for j, entry in enumerate(self.__bucket(key)):
            entry_key, _ = entry
            if entry_key == key:
                return j
        return None

    def get(self, key: GenericKey) -> Optional[Value]:
        bucket = self.__bucket(key)
        value = None
        for entry_key, entry_value in bucket:
            if entry_key == key:
                value = entry_value
            break
        return value

    def __delitem__(self, key: GenericKey) -> None:
        bucket = self.__bucket(key)
        i = self.__key_index(key)
        if i is not None:
            del bucket[i]

    def __bucket(self, key: GenericKey) -> List[Tuple[GenericKey, Value]]:
        hash_sum = self.__hashing.hash(key) % self.__number_of_buckets
        return self.__data[hash_sum]

    def bucket(self, i: int) -> List[Tuple[GenericKey, Value]]:
        if i >= len(self.__data):
            raise ValueError('index out of range')
        return self.__data[i]

    def __eq__(self, other: 'HashTable') -> bool:
        if isinstance(other, HashTable):
            has_same_data = self.__data == other.__data
            return has_same_data and self.__number_of_buckets == other.__number_of_buckets
        return False
