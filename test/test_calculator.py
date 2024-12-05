import unittest
from src.calculator import NumCalculator

class MyTestCase(unittest.TestCase):
    def test_plus(self):
        self.result = NumCalculator()
        self.assertEqual(self.result.plus(10, 567), 577)


if __name__ == '__main__':
    unittest.main()
