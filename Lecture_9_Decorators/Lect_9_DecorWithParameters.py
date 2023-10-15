# ДЕКОРАТОР С ПАРАМЕТРАМИ

import time
from typing import Callable

def count(num: int = 1):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result
        
        return wrapper
    
    return deco

@count(10) # ТУТ УЖЕ УКАЗЫВАЕМ АРГУМЕНТ (В ОТЛИЧИЕ ОТ ПРОСТОГО ДЕКОРАТОРА, ГДЕ АРГУМЕНТОМ БЫЛА САМА ФУКНЦИЯ)
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

# print(f'{factorial(10) = }')
# print(f'{factorial(10) = }')

# # Результаты замеров [4.4000043999403715e-06, 2.3999964469112456e-06, 1.4999968698248267e-06, 1.0999938240274787e-06, 1.1000010999850929e-06, 1.400003384333104e-06, 1.0999938240274787e-06, 1.3000026228837669e-06, 1.2999953469261527e-06, 1.0000003385357559e-06]
# # factorial(10) = 3628800
# # Результаты замеров [5.000001692678779e-06, 2.6999987312592566e-06, 2.1999949240125716e-06, 2.2000021999701858e-06, 2.1000014385208488e-06, 2.0999941625632346e-06, 2.1000014385208488e-06, 2.1000014385208488e-06, 2.1999949240125716e-06, 2.1000014385208488e-06]
# # factorial(10) = 3628800

"""
Каждый из двух запусков фукнции делает по 10 замеров, т.е. перед каждым новым запуском список time_for_count очищается. Если бы список time_for_count был создан 
на уровень выше, в фукнции deco, произошло бы его замыкание. В результате каждый новый запуск функции factorial дополнял бы уже существующий список, 
а не создавал новые 10 значений

!!! Для оценки быстродействия рекомендуется использовать модуль timeit из 'батареек Python', а не созданный выше декоратор
"""

# TEST

import random
from typing import Callable

def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter
        
        return wrapper
    
    return deco

@count(10)
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)

# print(f'{rnd(1, 10) =}')
# print(f'{rnd(1, 100) =}')
# print(f'{rnd(1, 1000) =}')

# # rnd(1, 10) =[7, 10, 5, 3, 4, 9, 1, 1, 10, 2]
# # rnd(1, 100) =[7, 10, 5, 3, 4, 9, 1, 1, 10, 2, 48, 14, 47, 36, 10, 88, 71, 14, 43, 100]
# # rnd(1, 1000) =[7, 10, 5, 3, 4, 9, 1, 1, 10, 2, 48, 14, 47, 36, 10, 88, 71, 14, 43, 100, 948, 914, 874, 278, 380, 721, 339, 104, 744, 977]  

# ДЕКОРАТОРЫ FUNCTOOLS

# ДЕКОРАТОР WRAPS

""" смотрим код из главы выше"""

@count(10) 
def factorial(n: int) -> int:
    """ Returns the factorial of the number n"""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

# print(f'{factorial(10) = }')
# # factorial(10) = [3628800, 3628800, 3628800, 3628800, 3628800, 3628800, 3628800, 3628800, 3628800, 3628800]

# print(f'{factorial.__name__ = }')
# # factorial.__name__ = 'wrapper'

# help(factorial)
# # Help on function wrapper in module __main__:

# # wrapper(*args, **kwargs)

"""т.е. получили инфомрацию об обертке, а не о самой функции factorial, т.к. фактически работает обертка"""

# исправляем

import random
from typing import Callable
from functools import wraps

def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        
        @wraps(func)   # ДОБАВЛЕНИЕ ДЕКОРАТОРА WRAPS ДЕЛАЕТСЯ ПРЯМО ПЕРЕД ОПРЕДЕЛЕНИЕМ ФУНКЦИИ WRAPPER (т.е. к самой глубоко вложенной функции)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter
        
        return wrapper
    
    return deco

"""!!! В качестве аргумента wraps должен получить параметр декларируемой функции"""

@count(10) 
def factorial(n: int) -> int:
    """ Returns the factorial of the number n"""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

"""Теперь factorial возвращает свои название и строку документации"""

# print(f'{factorial(10) = }')
# # factorial(10) = [3628800, 3628800, 3628800, 3628800, 3628800, 3628800, 3628800, 3628800, 3628800, 3628800]

# print(f'{factorial.__name__ = }')
# # factorial.__name__ = 'factorial'

# help(factorial)
# # Help on function factorial in module __main__:

# # factorial(n: int) -> int
# #     Returns the factorial of the number n

# ДЕКОРАТОР CACHE (ИЗ КОРОБКИ)

from functools import cache

@cache
def factorial(n: int) -> int:
    print(f'Вычисляем факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

# print(f'{factorial(10) = }')
# print(f'{factorial(15) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')

# # Вычисляем факториал для числа 10
# # factorial(10) = 3628800
# # Вычисляем факториал для числа 15
# # factorial(15) = 1307674368000
# # factorial(10) = 3628800
# # Вычисляем факториал для числа 20
# # factorial(20) = 2432902008176640000
# # factorial(10) = 3628800
# # factorial(20) = 2432902008176640000