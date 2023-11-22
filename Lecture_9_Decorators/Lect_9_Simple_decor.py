# ДЕКОРАТОРЫ

"""Декоратор — это функция, которая принимает в качестве аргумента другую функцию и изменяет ее поведение, не изменяя саму функцию"""

import time
from typing import Callable

def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат фукнции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result
    
    return wrapper

def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

# print(f'{factorial(10) = }')
# # factorial(10) = 3628800

# control = main(factorial)
# print(f'{control.__name__} = ')
# # wrapper = 

# print(f'{control(10) = }')

# # Запуск функции factorial в 1697375625.0983198
# # Результат фукнции factorial: 3628800
# # Завершение функции factorial в 1697375625.099319
# # control(10) = 3628800

"""
* Функция main пинимает на вход другую  функцию. Внутри main определена другая фунцкия - wrapper, которая возврвщается функцией main
* Создаем переменную (функцию) control, в которую помещается wrapper с замкнутой внутри функции func нашей декорируемой функцией factorial.
При вызове control помимо результата поиска факториала получаем вывод (принт), прописанный внутри  wrapper

Замыкание переданной в качестве аргумента функции внутри другой функции называется ДЕКОРИРОВАНИЕМ функции. В нашем примере main - декоратор, 
которым мы декорировали функцию factorial
"""

# СИНТАКСИЧЕСКИЙ САРАХ PYTHON, @

import time
from typing import Callable

def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат фукнции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result
    
    return wrapper

"""декорируем фунцкию, без присвоение отдельной переменной"""

@main
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

# print(f'{factorial(10) =}')

# # Запуск функции factorial в 1697376254.809228
# # Результат фукнции factorial: 3628800
# # Завершение функции factorial в 1697376254.8102267
# # factorial(10) =3628800

"""
!!! фукнция -декоратор должна быть определена в коде раньше, чем использована. Иначе будет ошибка NameError
"""
# МНОЖЕСТВЕННОЕ ДЕКОРИРОВАНИЕ

# from typing import Callable

# def deco_a(func: Callable):
#     def wrapper_a(*args, **kwargs):
#         print('Старт декоратора А')
#         print(f'Запуск функции {func.__name__}')
#         result = func(*args, **kwargs)
#         print('Завершение декоратора А')
#         return result
    
#     print("Возвращаем wrapper A")
#     return wrapper_a

# def deco_b(func: Callable):
#     def wrapper_b(*args, **kwargs):
#         print('Старт декоратора B')
#         print(f'Запуск функции {func.__name__}')
#         result = func(*args, **kwargs)
#         print('Завершение декоратора B')
#         return result
    
#     print("Возвращаем wrapper B")
#     return wrapper_b

# def deco_c(func: Callable):
#     def wrapper_c(*args, **kwargs):
#         print('Старт декоратора C')
#         print(f'Запуск функции {func.__name__}')
#         result = func(*args, **kwargs)
#         print('Завершение декоратора C')
#         return result
    
#     print("Возвращаем wrapper C")
#     return wrapper_c

# @deco_c
# @deco_b
# @deco_a
# def main():
#     print('Вот здесь работает ОСНОВНАЯ фукнция')
    
# main()

# # Возвращаем wrapper A
# # Возвращаем wrapper B    
# # Возвращаем wrapper C    
# # Старт декоратора C      
# # Запуск функции wrapper_b
# # Старт декоратора B      
# # Запуск функции wrapper_a
# # Старт декоратора А
# # Запуск функции main
# # Вот здесь работает ОСНОВНАЯ фукнция
# # Завершение декоратора А
# # Завершение декоратора B
# # Завершение декоратора C

"""
Мы создали три одинаковых декоратора, которые сообщают о начале и завершении работы и о моменте декорирования: А, В, С
Ближайший к функции - декоратор А. Декоратор С - самый дальний от основной фукнции. 
При запуске кода процесс декорирования начинается снизу вверх, т.е. А, потом В, после С (т.е. декораторы возвращаются в таком порядке). 
Прежде чем выполнить код основной фукнции, запускается код верхнего декоратора (С), далее В, в конце нижний А и в нем уже код фукнции main/
После того, как декорированная фукнция завершила работу и вернула результат, декораторы завершают работу в обратном старту порядке,снизу вверх. 
В зависимости от решаемых задач, порядок декорирования может привести к различным результатам
"""

# ДОПОЛНИТЕЛЬНЫЕ ПЕРЕМЕННЫЕ В ДЕКОРАТОРЕ

def cache(func:Callable):
    _cache_dict = {}
    
    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]
    
    return wrapper

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
# # factorial(10) = 3628800  - в этом случае факториал был уже вычислен (значение было в кэше), поэтому функция не вызывалась, а значит и принта нет. Просто село из кэша значение
# # Вычисляем факториал для числа 20
# # factorial(20) = 2432902008176640000
# # factorial(10) = 3628800
# # factorial(20) = 2432902008176640000

# TEST

import random
from typing import Callable

def cache(func:Callable):
    _cache_dict = {}
    
    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]
    
    return wrapper

@cache
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)

print(f'{rnd(1, 10) =}')
print(f'{rnd(1, 10) =}')
print(f'{rnd(1, 10) =}')

# rnd(1, 10) =3
# rnd(1, 10) =3
# rnd(1, 10) =3

""" Выводит одно и то же значение, т.к. в обертке идет проверка, и если введенные аргументы уже есть в словаре, фунцкия не выполняется, 
а выводится уже имеющееся 
значение предыдущего запуска функции с этими аргументами"""

