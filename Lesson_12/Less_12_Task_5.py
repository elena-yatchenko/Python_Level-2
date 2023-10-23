
"""
📌 Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.
"""
        

class Rectangle:
    
    __slots__ = ('_lenght', '_width')
    
    def __init__(self, lenght, width=None):
        self._lenght = abs(lenght)
        if not width:
            self._width = abs(lenght)
        else:
            self._width = abs(width)
            
    @property
    def width(self):
        return self._width
    
    @property
    def lenght(self):
        return self._lenght
    
    @width.setter
    def width(self, value):
        self._width = abs(value)
        
    @lenght.setter
    def lenght(self, value):
        self._lenght = abs(value)
            
    def perimeter(self):
        return (self._lenght + self._width) * 2
    
    def square(self):
        return self._lenght * self._width
    
    def __add__(self, other):
        return Rectangle(self.perimeter() + other.perimeter())
    
    def __sub__(self, other):
        return Rectangle(abs(self.perimeter() - other.perimeter()))
        
r = Rectangle(-3, 4)
r.width = -6
r.lenght = -2
print(r.width)
print(r.lenght)

print(Rectangle.__slots__)

print(r.perimeter())
print(r.square())