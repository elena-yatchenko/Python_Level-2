# Исключение NegativeValueError

# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError, которое выбрасывается при некорректных 
# значениях ширины и высоты, как при создании объекта, так и при установке их через сеттеры.

class NegativeValueError(ValueError):
    pass

class Rectangle:
    
    def __init__(self, lenght, width=None):
        if lenght <= 0:
            raise NegativeValueError('Введено отрицательное значение')
        self._lenght = lenght
        if width is None:
            self._width = lenght
        else:
            if width <= 0:
                raise NegativeValueError('Введено отрицательное значение')   
            self._width = width
            
    @property
    def width(self):
        return self._width
    
    @property
    def lenght(self):
        return self._lenght
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise NegativeValueError('Нельзя присваивать значение 0 или отрицательное число')
        self._width = abs(value)
        
    @lenght.setter
    def lenght(self, value):
        if value <= 0:
            raise NegativeValueError('Нельзя присваивать значение 0 или отрицательное число')
        self._lenght = abs(value)
            
    def perimeter(self):
        return (self._lenght + self._width) * 2
    
    def square(self):
        return self._lenght * self._width
    
    def __add__(self, other):
        return Rectangle(self.perimeter() + other.perimeter())
    
    def __sub__(self, other):
        return Rectangle(abs(self.perimeter() - other.perimeter()))

r = Rectangle(3)
r.width = 2
r.lenght = 4

print(r.width)
print(r.lenght)


# РЕШЕНИЕ СИСТЕМЫ

# class NegativeValueError(ValueError):
#     pass


# class Rectangle:
#     def __init__(self, width, height=None):
#         if width <= 0:
#             raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
#         self._width = width
#         if height is None:
#             self._height = width
#         else:
#             if height <= 0:
#                 raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
#             self._height = height

#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, value):
#         if value > 0:
#             self._width = value
#         else:
#             raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self, value):
#         if value > 0:
#             self._height = value
#         else:
#             raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

#     def perimeter(self):
#         return 2 * (self._width + self._height)

#     def area(self):
#         return self._width * self._height

#     def __add__(self, other):
#         width = self._width + other._width
#         perimeter = self.perimeter() + other.perimeter()
#         height = perimeter / 2 - width
#         return Rectangle(width, height)

#     def __sub__(self, other):
#         if self.perimeter() < other.perimeter():
#             self, other = other, self
#         width = abs(self._width - other._width)
#         perimeter = self.perimeter() - other.perimeter()
#         height = perimeter / 2 - width
#         return Rectangle(width, height) 