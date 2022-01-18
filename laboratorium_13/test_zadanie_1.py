from zadanie_1 import getNumber, organize
import unittest


class NWDTest(unittest.TestCase):
    def test_number_getting(self):
        self.assertRaises(ValueError, getNumber)

    def test_organizing(self):
        self.assertEqual(organize(5, 10), (10, 5))
        self.assertEqual(organize(7, 7), (7, 7))


if __name__ == '__main__':
    unittest.main()
