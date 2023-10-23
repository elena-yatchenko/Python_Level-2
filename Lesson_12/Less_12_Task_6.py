
"""
📌 Изменяем класс прямоугольника.
📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
"""
class Validation:
    
    def __init__(self, name):
        self.name = name
        
    def  __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        setattr(instance, self.name, abs(value))
        

class Rectangle:
    width = Validation('_width')
    lenght = Validation('_lenght')
    
    def __init__(self, lenght, width=None):
        self._lenght = abs(lenght)
        if not width:
            self._width = abs(lenght)
        else:
            self._width = abs(width)
            
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

print(r.perimeter())
print(r.square())