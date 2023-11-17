import pytest
from HW_14_Rectangle import Rectangle, NegativeValueError

def test_width():
    r1 = Rectangle(5)
    assert r1.width == 5

# def test_height(self):
#     r2 = Rectangle(3, 4)
#     self.assertEqual(r2.height, 4)

# def test_perimeter(self):
#     r1 = Rectangle(5)
#     self.assertEqual(r1.perimeter(), 20)

# def test_perimeter(self):
#     r1 = Rectangle(5)
#     self.assertEqual(r1.perimeter(), 20)

# def test_area(self):
#     r2 = Rectangle(3, 4)
#     self.assertEqual(r2.area(), 12)

# def test_addition(self):
#     r1 = Rectangle(5)
#     r2 = Rectangle(3, 4)
#     r3 = r1 + r2
#     self.assertEqual(r3.width, 8)
#     self.assertEqual(r3.height, 9)

# def test_subtraction(self):
#     r1 = Rectangle(10)
#     r2 = Rectangle(3, 4)
#     r3 = r1 - r2
#     self.assertEqual(r3.width, 7)
#     self.assertEqual(r3.height, 6)

# def test_negative_width(self):
#     with self.assertRaises(NegativeValueError):
#         r1 = Rectangle(-5)

# def test_negative_height(self):
#     with self.assertRaises(NegativeValueError):
#         r1 = Rectangle(5, -4)

# def test_set_width(self):
#     r1 = Rectangle(5)
#     r1.width = 10
#     self.assertEqual(r1.width, 10)

# def test_set_negative_width(self):
#     r1 = Rectangle(5)
#     with self.assertRaises(NegativeValueError):
#         r1.width = -10

# def test_set_height(self):
#     r1 = Rectangle(3, 4)
#     r1.height = 6
#     self.assertEqual(r1.height, 6)

# def test_set_negative_height(self):
#     r1 = Rectangle(3, 4)
#     with self.assertRaises(NegativeValueError):
#         r1.height = -6

# def test_subtraction_negative_result(self):
#     r1 = Rectangle(3, 4)
#     r2 = Rectangle(10)
#     with self.assertRaises(NegativeValueError):
#         r3 = r1 - r2

# def test_subtraction_same_perimeter(self):
#     r1 = Rectangle(5)
#     r2 = Rectangle(4, 3)
#     r3 = r1 - r2
#     self.assertEqual(r3.width, 1)
#     self.assertEqual(r3.height, 2.0)



if __name__ == '__main__':
    pytest.main(['-v'])