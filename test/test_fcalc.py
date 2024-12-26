import unittest
from unittest.mock import patch
from src.fcalc import Fcalc

class FCalcTest(unittest.TestCase):
#create tests case fixture
    def setUp(self):
        self.result = Fcalc()
    def tearDown(self):
        self.result = None

#test cases
    def test_num10(self):
        self.assertEqual(self.result.factor(10), 3628800)

    def test_num1(self):
        self.assertEqual(self.result.factor(1), 1)

    def test_zero(self):
        self.assertEqual(self.result.factor(0), 1)

    def test_negative(self):
        self.assertEqual(self.result.factor(-1), None)
#example of skipping decorator
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        pass
#mocking plus
    @patch("src.fcalc.Fcalc.factor", return_value=479001600)
    def test_fcalc_mock(self, factor):
        self.assertEqual(factor(12), 479001600)
#test for errors and raises
    def test_string_type(self):
        with self.assertRaises(TypeError):
            self.result.factor("1")

    def test_float_type(self):
        with self.assertRaises(RecursionError):
            self.result.factor(1.5)

if __name__ == '__main__':
    unittest.main()