# МАТЕМАТИКА В PYTHON
"""математические модули - нужно импортировать перед началом работы

import math  - модуль математики
import decimal - модуль, который позволяет использовать вещественные числа высокой точности (28 знаков после запятой)
import fractions - для работы с дробями 

"""
# import math
# print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')

# 3.141592653589793
# 2.718281828459045
# inf
# nan
# 6.283185307179586

# print(dir(math))

# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 
#  'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 
#  'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 
#  'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 
#  'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

# print(help(math.gcd))
# gcd(*integers)
#    Greatest Common Divisor.

# import decimal # НЕ обезает вещественные числа, как обычно делает питон для float

# print(0.1 + 0.2) # 0.30000000000000004

# num = decimal.Decimal(1) / decimal.Decimal(3)
# print(num) # 0.3333333333333333333333333333

# decimal.getcontext().prec = 50 # prec позволяет задавать сколько символов после запятой хотим видеть (точность)
# pi = decimal.Decimal('3.141_592') 
# a = decimal.Decimal(input()) # decimal преобразует введенное строковое значение в вещественное число с указанной точностью (50)
# science = 2 * pi * a ** 2     # пусть a = 23.452346
# print(science) # точность 50 символов - 3455.8299465401014940069008657689390748882850815843


# модуль FRACTIONS - запись дробей без потери точности

# import fractions 

# f1 = fractions.Fraction(1, 3)
# print(f1) # 1/3

# f2 = fractions.Fraction(3, 5)
# print(f2) # 3/5
# print(f1 * f2) # 1/5

# ВСТРОЕННЫЕ МАТЕМАТИЧЕСКИЕ ФУНКЦИИ (без вызова спец.модуля)

"""
abs(x) возвращает абсолютное число, по модулю
divmod(a, b) - возвращает частное и остаток от целочисленного деления. Аналогично
вычислению a // b и a % b
pow(base, exp[, mod]) - при передаче 2 аргументов возводит base в степень exp. При 
передаче 3 аргументов, результат возведения в степень еще делится по модулю на значение mod
и выводится остаток этого деления

round(number[, ndigits]) - округляет число number до ndigits цифр после запятой. 
Если второй аргумент не передать, округляет до ближайшего целого.

"""

x = -42
print(abs(x)) # 42

a = 42
b= 5
print(divmod(a, b)) # (8, 2) - 42 // 5 = 8; 42 % 5 = 2

print(pow(a, b)) # 130691232 - возведение 42 ** 5, 
print(pow(a, b, 10)) # 2 Т.к. (42 ** 5) % 10 = 2 (остаток)

print(round(3.141_592_653_589_793, 3)) # 3.142








