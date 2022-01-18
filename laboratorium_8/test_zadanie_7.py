from zadanie_7 import isPrime, euklides
import unittest


class primeTest(unittest.TestCase):
    def test_primacy(self):
        self.assertFalse(isPrime(1))
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(127))
        self.assertFalse(isPrime(1000000))

    def test_euklides(self):
        self.assertEqual(euklides(1, 100), 1)
        self.assertEqual(euklides(1024, 81), 1)
        self.assertEqual(euklides(70, 65), 5)
        self.assertEqual(euklides(100000, 2), 2)
