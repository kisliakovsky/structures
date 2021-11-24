from abc import ABC, abstractmethod

from src.priority_queue import PriorityQueue
from src.queue import LimitedQueue


class AbstractPacketProcessor(ABC):

    @abstractmethod
    def take(self, arrival: int, processing_time: int) -> int:
        pass


class PacketProcessor(AbstractPacketProcessor):
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


class ParallelPacketProcessor(AbstractPacketProcessor):
    def __init__(self):
        self.__buffer: PriorityQueue[int] = PriorityQueue[int]()

    def take(self, arrival: int, processing_time: int) -> int:
        pass

    def __can_be_processed_immediately(self, processing_time) -> bool:
        return self.__buffer.is_empty() and processing_time == 0

    def __exists_already_processed(self, arrival) -> bool:
        return not self.__buffer.is_empty() and self.__buffer.peak() <= arrival
