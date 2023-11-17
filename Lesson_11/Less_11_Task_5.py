"""
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр
прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""

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
        
    
r1 = Rectangle(12, 4)
print(r1.perimeter(), r1.square())

r2 = Rectangle(12)
print(r2.perimeter(), r2.square())
r2.lenght = 8
print(r2.lenght)
r3 = r1 + r2
r4 = r1 - r2

print(r3.lenght) # 80
print(r4.lenght) # 16