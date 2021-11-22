from unittest import TestCase

from src.packet_processor import PacketProcessor


class TestPacketProcessor(TestCase):

    def test_one_smallest_packet(self):
        packet_processor = PacketProcessor(1)
        self.assertEqual(0, packet_processor.take(0, 0))

    def test_one_medium_packet(self):
        packet_processor = PacketProcessor(1)
        self.assertEqual(0, packet_processor.take(0, 1))

    def test_two_simultaneous_packets(self):
        packet_processor = PacketProcessor(1)
        self.assertEqual(0, packet_processor.take(0, 1))
        self.assertEqual(-1, packet_processor.take(0, 1))

    def test_two_subsequent_packets(self):
        packet_processor = PacketProcessor(1)
        self.assertEqual(0, packet_processor.take(0, 1))
        self.assertEqual(1, packet_processor.take(1, 1))

    def test_many_packets(self):
        packet_processor = PacketProcessor(2)
        self.assertEqual(2, packet_processor.take(2, 9))
        self.assertEqual(11, packet_processor.take(4, 8))
        self.assertEqual(-1, packet_processor.take(10, 9))
        self.assertEqual(19, packet_processor.take(15, 2))
        self.assertEqual(21, packet_processor.take(19, 1))

    def test_many_smallest_packets(self):
        packet_processor = PacketProcessor(2)
        self.assertEqual(0, packet_processor.take(0, 0))
        self.assertEqual(0, packet_processor.take(0, 0))
        self.assertEqual(0, packet_processor.take(0, 0))
        self.assertEqual(1, packet_processor.take(1, 0))
        self.assertEqual(1, packet_processor.take(1, 0))
        self.assertEqual(1, packet_processor.take(1, 1))
        self.assertEqual(2, packet_processor.take(1, 2))
        self.assertEqual(-1, packet_processor.take(1, 3))

    def test_full_buffer(self):
        packet_processor = PacketProcessor(2)
        self.assertEqual(0, packet_processor.take(0, 0))
        self.assertEqual(0, packet_processor.take(0, 0))
        self.assertEqual(0, packet_processor.take(0, 0))
        self.assertEqual(1, packet_processor.take(1, 1))
        self.assertEqual(2, packet_processor.take(1, 0))
        self.assertEqual(-1, packet_processor.take(1, 0))
        self.assertEqual(-1, packet_processor.take(1, 2))
        self.assertEqual(-1, packet_processor.take(1, 3))

    def test_long_delay(self):
        packet_processor = PacketProcessor(1)
        self.assertEqual(999999, packet_processor.take(999999, 1))
        self.assertEqual(1000000, packet_processor.take(1000000, 0))
        self.assertEqual(1000000, packet_processor.take(1000000, 1))
        self.assertEqual(-1, packet_processor.take(1000000, 0))
        self.assertEqual(-1, packet_processor.take(1000000, 0))
