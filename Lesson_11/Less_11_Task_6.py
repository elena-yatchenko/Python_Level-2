"""
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""

# __eq__ - равно, ==
# __ne__ - не равно, !=
# __gt__ - больше, >
# __ge__ - не больше, меньше или равно, <=
# __lt__ - меньше, <
# __le__ - не меньше, больше или равно, >=

class Rectangle:
    
    def __init__(self, lenght, width=None):
        self.lenght = lenght
        if not width:
            self.width = lenght
        else:
            self.width = width
            
    def perimeter(self):
        return (self.lenght + self.width) * 2
    
    def square(self):
        return self.lenght * self.width
    
    def __add__(self, other):
        return Rectangle(self.perimeter() + other.perimeter())
    
    def __sub__(self, other):
        return Rectangle(abs(self.perimeter() - other.perimeter()))
    
    def __eq__(self, other):
        return self.square() == other.square()
    
    def __gt__(self, other):
        return self.square() > other.square()
    
    def __ge__(self, other):
        return self.square() >= other.square()


r1 = Rectangle(12, 4)   
r2 = Rectangle(12)
# print(r1 == r2)
# print(r1 != r2)
print(r1 > r2)

# print(r1 <= r2)

print(r1 < r2)
# print(r1 >= r2)

print(r1.square())
print(r2.square())