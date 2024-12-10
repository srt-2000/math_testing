import unittest
from src.fcalc import Fcalc

#test for calculating
class FCalcTest(unittest.TestCase):
#create tests case fixture
    def setUp(self):
        self.result = Fcalc()
        print("\nstart FCalcTest")

    def tearDown(self):
        self.result = None
        print("stop FCalcTest")
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

#test for errors and raises
class FErrorTest(unittest.TestCase):
#create tests case fixture
    def setUp(self):
        self.result = Fcalc()
        print("\nstart FErrorTest")

    def tearDown(self):
        self.result = None
        print("Stop FErrorTest")
#test cases
    def test_string_type(self):
        with self.assertRaises(TypeError):
            self.result.factor("1")

    def test_float_type(self):
        with self.assertRaises(RecursionError):
            self.result.factor(1.5)

if __name__ == '__main__':
    unittest.main()