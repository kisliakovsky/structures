"""This module contains application examples of hash-calculating objects"""

from typing import Iterator

from src.hash_table import PolynomialHashing, StringKey


class RollingHashing:
    def __init__(self, string: str, modulus: int = 1000000007, base: int = 263):
        self.__prime: int = modulus
        self.__x: int = base
        self.__i: int = 0
        self.__chars = list(reversed(string))
        self.__powered_x = pow(self.__x, len(string) - 1, self.__prime)
        self.__hash: int = PolynomialHashing(modulus, base).hash(StringKey(string))

    def hash(self) -> int:
        return self.__hash

    def shift_left(self, char: chr) -> None:
        shifted_char_hash = ((ord(self.__chars[self.__i]) % self.__prime) * self.__powered_x) % self.__prime
        self.__hash = ((self.__hash - shifted_char_hash) * self.__x + ord(char)) % self.__prime
        self.__i += 1
        self.__chars.append(char)


class SearchString:
    def __init__(self, string: str):
        self.__string: str = string
        self.__string_length: int = len(string)

    def indices_of_occurrences(self, substring: str) -> Iterator[int]:
        return reversed(list(self.__indices_of_occurrences(substring)))

    def __indices_of_occurrences(self, substring: str) -> Iterator[int]:
        substring_length = len(substring)
        if substring_length == self.__string_length:
            if self.__check_substring(substring, 0):
                yield 0
            else:
                return
        elif substring_length > self.__string_length:
            return
        elif substring_length < self.__string_length:
            substring_hash = RollingHashing(substring).hash()
            start_i = self.__string_length - substring_length
            window_hashing = RollingHashing(self.__string[start_i:])
            if window_hashing.hash() == substring_hash:
                if self.__check_substring(substring, start_i):
                    yield start_i
            for i in range(start_i - 1, -1, -1):
                window_hashing.shift_left(self.__string[i])
                if window_hashing.hash() == substring_hash:
                    if self.__check_substring(substring, i):
                        yield i

    def __check_substring(self, substring: str, start_i: int) -> bool:
        return substring == self.__string[start_i:start_i + len(substring)]
