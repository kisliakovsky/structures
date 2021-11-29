from random import randint
from unittest import TestCase

from src.packet_processor import StandardParallelPacketProcessor


class TestParallelPacketProcessor(TestCase):

    def test_growing_packets(self):
        packet_processor = StandardParallelPacketProcessor(2)
        self.assertEqual((0, 0), packet_processor.take(1))
        self.assertEqual((1, 0), packet_processor.take(2))
        self.assertEqual((0, 1), packet_processor.take(3))
        self.assertEqual((1, 2), packet_processor.take(4))
        self.assertEqual((0, 4), packet_processor.take(5))

    def test_equal_packets(self):
        packet_processor = StandardParallelPacketProcessor(4)
        self.assertEqual((0, 0), packet_processor.take(1))
        self.assertEqual((1, 0), packet_processor.take(1))
        self.assertEqual((2, 0), packet_processor.take(1))
        self.assertEqual((3, 0), packet_processor.take(1))
        self.assertEqual((0, 1), packet_processor.take(1))
        self.assertEqual((1, 1), packet_processor.take(1))
        self.assertEqual((2, 1), packet_processor.take(1))
        self.assertEqual((3, 1), packet_processor.take(1))
        self.assertEqual((0, 2), packet_processor.take(1))
        self.assertEqual((1, 2), packet_processor.take(1))
        self.assertEqual((2, 2), packet_processor.take(1))
        self.assertEqual((3, 2), packet_processor.take(1))
        self.assertEqual((0, 3), packet_processor.take(1))
        self.assertEqual((1, 3), packet_processor.take(1))
        self.assertEqual((2, 3), packet_processor.take(1))
        self.assertEqual((3, 3), packet_processor.take(1))
        self.assertEqual((0, 4), packet_processor.take(1))
        self.assertEqual((1, 4), packet_processor.take(1))
        self.assertEqual((2, 4), packet_processor.take(1))
        self.assertEqual((3, 4), packet_processor.take(1))

    def test_zero_packets(self):
        packet_processor = StandardParallelPacketProcessor(2)
        self.assertEqual((0, 0), packet_processor.take(0))
        self.assertEqual((0, 0), packet_processor.take(0))
        self.assertEqual((0, 0), packet_processor.take(1))
        self.assertEqual((1, 0), packet_processor.take(0))
        self.assertEqual((1, 0), packet_processor.take(0))
        self.assertEqual((1, 0), packet_processor.take(0))
        self.assertEqual((1, 0), packet_processor.take(2))
        self.assertEqual((0, 1), packet_processor.take(1))
        self.assertEqual((0, 2), packet_processor.take(2))
        self.assertEqual((1, 2), packet_processor.take(3))
        self.assertEqual((0, 4), packet_processor.take(0))
        self.assertEqual((0, 4), packet_processor.take(0))
        self.assertEqual((0, 4), packet_processor.take(0))
        self.assertEqual((0, 4), packet_processor.take(2))
        self.assertEqual((1, 5), packet_processor.take(1))
