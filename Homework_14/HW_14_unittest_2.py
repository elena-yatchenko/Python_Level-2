import unittest
from HW_14_Rectangle import Rectangle, NegativeValueError


class TestRectangle(unittest.TestCase):
    def test_width(self):
        # self.r1 = Rectangle(5)
        # т.к. здесь экземпляр создаем свой в каждом месяце, не нужно делать self для каждого экземпляра
        r1 = Rectangle(5)
        self.assertEqual(r1.width, 5)

    def test_height(self):
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.height, 4)

    def test_perimeter(self):
        r1 = Rectangle(5)
        self.assertEqual(r1.perimeter(), 20)

    def test_area(self):
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.area(), 12)

    def test_addition(self):
        r1 = Rectangle(5)
        r2 = Rectangle(3, 4)
        r3 = r1 + r2
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 9)

    def test_subtraction(self):
        r1 = Rectangle(10)
        r2 = Rectangle(3, 4)
        r3 = r1 - r2
        self.assertEqual(r3.width, 7)
        self.assertEqual(r3.height, 6)

    def test_negative_width(self):
        with self.assertRaises(NegativeValueError):
            r1 = Rectangle(-5)

    def test_negative_height(self):
        with self.assertRaises(NegativeValueError):
            r1 = Rectangle(5, -4)

    def test_set_width(self):
        r1 = Rectangle(5)
        r1.width = 10
        self.assertEqual(r1.width, 10)

    def test_set_negative_width(self):
        r1 = Rectangle(5)
        with self.assertRaises(NegativeValueError):
            r1.width = -10

    def test_set_height(self):
        r1 = Rectangle(3, 4)
        r1.height = 6
        self.assertEqual(r1.height, 6)

    def test_set_negative_height(self):
        r1 = Rectangle(3, 4)
        with self.assertRaises(NegativeValueError):
            r1.height = -6

    def test_subtraction_negative_result(self):
        r1 = Rectangle(3, 4)
        r2 = Rectangle(10)
        with self.assertRaises(NegativeValueError):
            r3 = r1 - r2

    def test_subtraction_same_perimeter(self):
        r1 = Rectangle(5)
        r2 = Rectangle(4, 3)
        r3 = r1 - r2
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

#     FAIL: test_subtraction_negative_result (__main__.TestRectangle.test_subtraction_negative_result)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\User\Documents\PC_Data\Study\Python_Level-2\Homework_14\HW_14_Unittest_2.py", line 71, in test_subtraction_negative_result
#     with self.assertRaises(NegativeValueError):
# AssertionError: NegativeValueError not raised

# ----------------------------------------------------------------------
# Ran 14 tests in 0.010s

# FAILED (failures=1)
