import unittest

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        self.assertEqual(2 - 1, 1)

    def test_multiply(self):
        self.assertEqual(2 * 3, 6)

    def test_divide(self):
        self.assertEqual(6 / 2, 3)

if __name__ == '__main__':
    unittest.main()