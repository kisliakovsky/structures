from unittest import TestCase

from src.hash_table import HashTable, IntKey, PolynomialHashing


class TestHashTable(TestCase):

    def test_put(self):
        hash_table = HashTable[IntKey, str](10000, PolynomialHashing[IntKey]())
        key = IntKey(76213)
        hash_table.put(key, 'Mom')
        another_hash_table = HashTable[IntKey, str](10000, PolynomialHashing[IntKey]())
        another_hash_table.put(key, 'Mom')
        self.assertEqual('Mom', hash_table.get(key))
        self.assertEqual('Mom', another_hash_table.get(key))
        self.assertTrue(hash_table == another_hash_table)
        hash_table.put(key, 'Dad')
        self.assertEqual('Dad', hash_table.get(key))
        self.assertFalse(hash_table == another_hash_table)

    def test_bucket(self):
        hash_table = HashTable[IntKey, str](10000, PolynomialHashing[IntKey]())
        key = IntKey(76213)
        hash_table.put(key, 'Mom')
        self.assertEqual([(key, 'Mom')], hash_table.bucket(6213))

    def test_get(self):
        hash_table = HashTable[IntKey, str](10000, PolynomialHashing[IntKey]())
        key = IntKey(76213)
        hash_table.put(key, 'Mom')
        self.assertEqual('Mom', hash_table.get(IntKey(76213)))
        self.assertIsNone(hash_table.get(IntKey(1)))

    def test_delete(self):
        hash_table = HashTable[IntKey, str](10000, PolynomialHashing[IntKey]())
        key = IntKey(76213)
        hash_table.put(key, 'Mom')
        del hash_table[key]
        self.assertIsNone(hash_table.get(key))
