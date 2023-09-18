# decimal.getcontext().prec = 50

# Напишите программу, которая вычисляет площадь круга и
# длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math

import decimal

# decimal.getcontext().prec = 42 # задали точность

# diameter = decimal.Decimal(input(f"не более тысячи: ")) # переводит строку в число с плавающей запятой и указанной точностью

# s = Pi * r ** 2
# с = pi * diameter

# PI = decimal.Decimal(math.pi)
# s = PI * pow((diameter / 2), 2)
# print(s)

# C = PI * diameter
# print(C)

# не более тысячи: 858
# 578181.853559319114861381194714340381324291
# 2695.48649678004249352625265601091086864471

# Вариант семинара (через функции)

diameter = decimal.Decimal(input(f"не более тысячи :"))

decimal.getcontext().prec = 42

def circle_diameter(diam):
    return decimal.Decimal(math.pi) * pow((diam/2),2)

# длинна окруности C = 3.14 * D
def circumference (diam):
    return decimal.Decimal(math.pi) * diam
    
print(circle_diameter(diameter))
print(circumference(diameter))

# не более тысячи :858
# 578181.853559319114861381194714340381324291
# 2695.48649678004249352625265601091086864471