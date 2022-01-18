from zadanie_6 import isSpecial
import unittest


class SpecialNumbersTest(unittest.TestCase):
    def test_values(self):
        self.assertRaises(ValueError, isSpecial, 120)

    def test_values_test(self):
        self.assertRaises(AssertionError, self.test_values)


if __name__ == '__main__':
    unittest.main()
