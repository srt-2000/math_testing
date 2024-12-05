import unittest
from src.fcalc import Fcalc

class FCtest(unittest.TestCase):

    def test_result(self):
        self.result = Fcalc()
        self.assertEqual(self.result.factor(10), 3628800)

    def test_zero(self):
        self.result = Fcalc()
        self.assertEqual(self.result.factor(0), 1)

if __name__ == '__main__':
    unittest.main()
