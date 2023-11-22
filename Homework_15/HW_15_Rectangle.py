from datetime import datetime
import argparse
import logging

parser = argparse.ArgumentParser(prog="rectangle", description="HW parser")

parser.add_argument(
    "-width",
    metavar="W",
    type=int,
    help="введите ширину первого прямоугольника(целое число)",
    default="1",
)
parser.add_argument(
    "-height",
    metavar="H",
    type=int,
    help="введите высоту первого прямоугольника (целое число)",
    default=None,
)
parser.add_argument(
    "-width_2",
    metavar="W",
    type=int,
    help="введите ширину второго прямоугольника(целое число)",
    default="1",
)
parser.add_argument(
    "-height_2",
    metavar="H",
    type=int,
    help="введите высоту второго прямоугольника (целое число)",
    default=None,
)
args = parser.parse_args()
print(f"В скрипт передано: {args}")

logging.basicConfig(level=logging.INFO, filename="rectangle.log", encoding="utf-8")
logger = logging.getLogger(__name__)


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            logger.error(f"Ширина должна быть положительной, а не {width}")
            raise NegativeValueError

        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                logger.error(f"Высота должна быть положительной, а не {height}")
                raise NegativeValueError
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f"Высота должна быть положительной, а не {value}")

    def perimeter(self):
        perimeter = 2 * (self._width + self._height)
        logger.info(
            f"Периметр прямоугольника с шириной {self._width} и высотой {self._height} равен {perimeter}"
        )
        return perimeter

    def area(self):
        area = self._width * self._height
        logger.info(
            f"Площадь прямоугольника с шириной {self._width} и высотой {self._height} равна {area}"
        )
        return area

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        logger.info(f"Результат сложения - прямоугольник {Rectangle(width, height)}")
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = abs(perimeter / 2 - width)
        logger.info(f"Результат вычитания - прямоугольник {Rectangle(width, height)}")
        return Rectangle(width, height)


r1 = Rectangle(args.width, args.height)
r2 = Rectangle(args.width_2, args.height_2)
print(r1.perimeter(), r2.perimeter())
r3 = r1 - r2
r1.width = 7
print(r1.width)
print(r3.width, r3.height)

# python HW_15_Rectangle.py -width 5 -width_2 4 -height_2 3
# python HW_15_Rectangle.py -width -5 -width_2 8
