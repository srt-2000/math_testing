import unittest
from src.calculator import NumCalculator

#test for calculating
class CCalcTest(unittest.TestCase):
#create tests case fixture
    def setUp(self):
        self.result = NumCalculator()

    def tearDown(self):
        self.result = None
#test plus cases
    def test_plus_positive(self):
        self.assertEqual(self.result.plus(189, 11), 200)
    def test_plus_negative(self):
        self.assertEqual(self.result.plus(-189, -11), -200)
    def test_plus_zero(self):
        self.assertEqual(self.result.plus(0, 0), 0)
    def test_plus_neg_pos(self):
        self.assertEqual(self.result.plus(-68, 58), -10)
    def test_plus_float(self):
        self.assertEqual(self.result.plus(1.5, 3.8), 5.3)
    def test_plus_string(self):
        with self.assertRaises(TypeError):
            self.result.plus(1, "asd")


#example of skipping decorator
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        pass

#test for errors and raises
class CErrorTest(unittest.TestCase):
#create tests case fixture
    def setUp(self):
        self.result = NumCalculator()

    def tearDown(self):
        self.result = None
#test cases
    # def test_string_type(self):
    #     with self.assertRaises(TypeError):
    #         self.result.factor("1")
    #
    # def test_float_type(self):
    #     with self.assertRaises(RecursionError):
    #         self.result.factor(1.5)

if __name__ == '__main__':
    unittest.main()
