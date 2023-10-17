"""
Создайте класс окружность.
📌 Класс должен принимать радиус окружности при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def lenght(self):
        return 2 * 3.14 * self.radius
    
    def square(self):
        return 3.14 * self.radius ** 2
    
c1 = Circle(12)
print(c1.lenght(), c1.square())        