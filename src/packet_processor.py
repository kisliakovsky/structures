from abc import ABC, abstractmethod
from heapq import heappop, heappush
from typing import Tuple, List

from src.heap import Key, Heap, Unit, FasterMinHeap
from src.queue import LimitedQueue


class PacketProcessor:
    def __init__(self, buffer_size: int):
        self.__buffer: LimitedQueue[int] = LimitedQueue[int](buffer_size)
        self.__previous_arrival: int = 0
        self.__processor_time: int = 0

    def take(self, arrival: int, processing_time: int) -> int:
        if arrival > self.__previous_arrival:
            while self.__exists_already_processed(arrival):
                self.__buffer.dequeue()
        self.__previous_arrival = arrival
        start_time = -1 if self.__buffer.is_full() else max(arrival, self.__processor_time)
        if start_time != -1 and not self.__can_be_processed_immediately(processing_time):
            finish_time = start_time + processing_time
            self.__buffer.enqueue(finish_time)
            self.__processor_time = finish_time
        return start_time

    def __can_be_processed_immediately(self, processing_time: int) -> bool:
        return self.__buffer.is_empty() and processing_time == 0

    def __exists_already_processed(self, arrival: int) -> bool:
        return not self.__buffer.is_empty() and self.__buffer.peak() <= arrival


class CoreKey(Key['CoreKey']):
    def __init__(self, i: int, time: int):
        self.__i = i
        self.__time = time

    def index(self) -> int:
        return self.__i

    def time(self) -> int:
        return self.__time

    def compare_to(self, other: 'CoreKey') -> int:
        diff_time = other.__time - self.__time
        return diff_time if diff_time != 0 else other.__i - self.__i

    def more(self) -> 'CoreKey':
        return CoreKey(self.__i, self.__time - 1)

    def add_time(self, time: int) -> 'CoreKey':
        return CoreKey(self.__i, self.__time + time)

    def __eq__(self, other):
        if isinstance(other, CoreKey):
            return self.__i == other.__i and self.__time == other.__time
        else:
            return False

    def __str__(self):
        return f"{self.__i} {self.__time}"


class ParallelPacketProcessor(ABC):

    @abstractmethod
    def take(self, processing_time: int) -> Tuple[int, int]:
        pass


class StandardParallelPacketProcessor(ParallelPacketProcessor):
    def __init__(self, n: int):
        self.__cores: List[Tuple[int, int]] = [(0, i) for i in range(n)]

    def take(self, processing_time: int) -> Tuple[int, int]:
        time, index = heappop(self.__cores)
        new_time = time + processing_time
        heappush(self.__cores, (new_time, index))
        return index, time


class FasterCustomParallelPacketProcessor(ParallelPacketProcessor):
    def __init__(self, n: int):
        self.__cores: FasterMinHeap = FasterMinHeap([(0, i) for i in range(n)])

    def take(self, processing_time: int) -> Tuple[int, int]:
        time, index = self.__cores.peak()
        new_time = time + processing_time
        self.__cores.change_key(0, (new_time, index))
        return index, time


class CustomParallelPacketProcessor(ParallelPacketProcessor):
    def __init__(self, n: int):
        self.__cores: Heap[CoreKey, CoreKey] = Heap(2, [Unit(CoreKey(i, 0)) for i in range(n)])

    def take(self, processing_time: int) -> Tuple[int, int]:
        key = self.__cores.pop().key()
        self.__cores.push(Unit(key.add_time(processing_time)))
        return key.index(), key.time()
