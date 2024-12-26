import unittest
from unittest.mock import patch
from src.calculator import NumCalculator


# test for calculating plus
class CCalcTestPlus(unittest.TestCase):
    # create tests case fixture
    def setUp(self):
        self.result = NumCalculator()

    def tearDown(self):
        self.result = None

    # test plus cases
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

    # mocking plus
    @patch("src.calculator.NumCalculator.plus", return_value=11)
    def test_positive_plus_mock(self, plus):
        self.assertEqual(plus(6, 5), 11)

    # example of skipping decorator
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        pass


# test for calculating minus
class CCalcTestMinus(unittest.TestCase):
    # create tests case fixture
    def setUp(self):
        self.result = NumCalculator()

    def tearDown(self):
        self.result = None

    # test minus cases
    def test_minus_positive(self):
        self.assertEqual(self.result.minus(189, 11), 178)

    def test_minus_negative(self):
        self.assertEqual(self.result.minus(-189, -11), -178)

    def test_minus_zero(self):
        self.assertEqual(self.result.minus(0, 0), 0)

    def test_minus_neg_pos(self):
        self.assertEqual(self.result.minus(-68, 58), -126)

    def test_minus_float(self):
        self.assertEqual(self.result.minus(1.5, 3.8), -2.3)

    def test_minus_string(self):
        with self.assertRaises(TypeError):
            self.result.minus(1, "asd")

    # mocking minus
    @patch("src.calculator.NumCalculator.minus", return_value=1)
    def test_positive_minus_mock(self, minus):
        self.assertEqual(minus(6, 5), 1)


# test for calculating mult
class CCalcTestMult(unittest.TestCase):
    # create tests case fixture
    def setUp(self):
        self.result = NumCalculator()

    def tearDown(self):
        self.result = None

    # test mult cases
    def test_mult_positive(self):
        self.assertEqual(self.result.mult(8, 9), 72)

    def test_mult_negative(self):
        self.assertEqual(self.result.mult(-8, -9), 72)

    def test_mult_zero(self):
        self.assertEqual(self.result.mult(5, 0), 0)

    def test_mult_neg_pos(self):
        self.assertEqual(self.result.mult(-8, 9), -72)

    def test_mult_float(self):
        self.assertEqual(self.result.mult(1.5, 2), 3)

    def test_mult_string_y(self):
        with self.assertRaises(TypeError):
            self.result.mult(1, "asd")

    def test_mult_string_x(self):
        with self.assertRaises(TypeError):
            self.result.mult("asd", 24)

    # mocking mult
    @patch("src.calculator.NumCalculator.mult", return_value=30)
    def test_positive_mult_mock(self, mult):
        self.assertEqual(mult(6, 5), 30)


# test for calculating div
class CCalcTestdiv(unittest.TestCase):
    # create tests case fixture
    def setUp(self):
        self.result = NumCalculator()

    def tearDown(self):
        self.result = None

    # test div cases
    def test_div_positive(self):
        self.assertEqual(self.result.div(8, 2), 4)

    def test_div_negative(self):
        self.assertEqual(self.result.div(-8, -2), 4)

    def test_div_neg_pos(self):
        self.assertEqual(self.result.div(-8, 2), -4)

    def test_div_float(self):
        self.assertEqual(self.result.div(3.2, 2), 1.6)

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.result.div(5, 0)

    def test_div_string_y(self):
        with self.assertRaises(TypeError):
            self.result.div(1, "asd")

    def test_div_string_x(self):
        with self.assertRaises(TypeError):
            self.result.div("asd", 24)

    # mocking div
    @patch("src.calculator.NumCalculator.div", return_value=2)
    def test_positive_div_mock(self, div):
        self.assertEqual(div(6, 3), 2)


# test for calculating full_div
class CCalcTestFullDiv(unittest.TestCase):
    # create tests case fixture
    def setUp(self):
        self.result = NumCalculator()

    def tearDown(self):
        self.result = None

    # test full_div cases
    def test_full_div_positive(self):
        self.assertEqual(self.result.full_div(9, 2), 4)

    def test_full_div_negative(self):
        self.assertEqual(self.result.full_div(-9, -2), 4)

    def test_full_div_neg_pos(self):
        self.assertEqual(self.result.full_div(-9, 2), -5)

    def test_full_div_float(self):
        self.assertEqual(self.result.full_div(3.2, 2), 1.0)

    def test_full_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.result.full_div(5, 0)

    def test_full_div_string_y(self):
        with self.assertRaises(TypeError):
            self.result.full_div(1, "asd")

    def test_full_div_string_x(self):
        with self.assertRaises(TypeError):
            self.result.full_div("asd", 24)

    # mocking full_div
    @patch("src.calculator.NumCalculator.full_div", return_value=2)
    def test_positive_full_div_mock(self, full_div):
        self.assertEqual(full_div(8, 3), 2)


# test for calculating end_div
class CCalcTestEndDiv(unittest.TestCase):
    # create tests case fixture
    def setUp(self):
        self.result = NumCalculator()

    def tearDown(self):
        self.result = None

    # test end_div cases
    def test_end_div_positive(self):
        self.assertEqual(self.result.end_div(9, 2), 1)

    def test_end_div_negative(self):
        self.assertEqual(self.result.end_div(-9, -2), -1)

    def test_end_div_neg_pos(self):
        self.assertEqual(self.result.end_div(-9, 2), 1)

    def test_end_div_pos_neg(self):
        self.assertEqual(self.result.end_div(9, -2), -1)

    def test_end_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.result.end_div(5, 0)

    def test_end_div_float(self):
        with self.assertRaises(TypeError):
            self.result.end_div(3.2, 1.3)

    def test_end_div_string_y(self):
        with self.assertRaises(TypeError):
            self.result.end_div(1, "asd")

    def test_end_div_string_x(self):
        with self.assertRaises(TypeError):
            self.result.end_div("asd", 24)

    # mocking end_div
    @patch("src.calculator.NumCalculator.end_div", return_value=2)
    def test_positive_end_div_mock(self, end_div):
        self.assertEqual(end_div(8, 3), 2)


if __name__ == '__main__':
    unittest.main()