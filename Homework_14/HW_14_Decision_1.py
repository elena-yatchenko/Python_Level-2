

class NegativeValueError(ValueError):
    pass

class Rectangle:

    def __init__(self, width, height=None):
        """
        >>> r1 = Rectangle(5)
        >>> r1.width
        5
        >>> r1.height
        5
        >>> r2 = Rectangle(3, 4)
        >>> r2.width
        3
        >>> r2.height
        4
        >>> r3 = Rectangle(-3, 4)
        Traceback (most recent call last):
         ...
        NegativeValueError: Ширина должна быть положительной, а не -3
        >>> r4 = Rectangle(2, -5)
        Traceback (most recent call last):
         ...
        NegativeValueError: Высота должна быть положительной, а не -5
        """
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.perimeter()
        20
        >>> r2 = Rectangle(3, 4)
        >>> r2.perimeter()
        14
        """
        return 2 * (self._width + self._height)

    def area(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.area()
        25
        >>> r2 = Rectangle(3, 4)
        >>> r2.area()
        12
        """
        return self._width * self._height

    def __add__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        9
        """
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = int(perimeter / 2 - width)
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r4 = r1 - r2
        >>> r4.width
        2
        >>> r4.height
        1
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = int(perimeter / 2 - width)
        return Rectangle(width, height)
    
# r1 = Rectangle(5)
# r2 = Rectangle(3, 4)
# r3 = r1 - r2
# print(r1.perimeter())
# print(r2.perimeter())
# print(r3.width)
# print(repr(r3))
# print(r3.height)
# r4 = r1 + r2
# print(r4.height)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

# 26 passed and 0 failed.
# Test passed.