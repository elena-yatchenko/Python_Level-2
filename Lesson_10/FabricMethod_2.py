from enum import Enum

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

# объявление точки в декартовых координатах
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

"""Если хотим объявлять и в полярных координатах, но повторно определять метод инициализации
(__init__) для одного и того же класса запрещено.
Значит, должны перестроить конструктор. В первую очередь, добавить индикатор - параметр, 
который будет указывать, какую систему координат мы хотим использовать"""      

from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2
    
class Point:
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * cos(b)
            self.y = a * sin(b)
            
"""тоже плохой код, т.к. если захотим добавить еще одну систему координат, придется 
добавлять ее в оба класса, добавлять условие. Кроме того, не очень понятно что такое а, 
а что такое b у нас в параметрах"""

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2
    
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
        
@staticmethod
def new_cartesion_point(x, y): # метод, который создает точку из декартовых координат
    return Point(x, y)

@staticmethod
def new_polar_point(rho, theta): # метод, который создает точку из полярных координат
    return Point(rho * cos(theta), rho * sin(theta))

if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p, p2)
    
    

