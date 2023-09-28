# СОЗДАНИЕ СОБСТВЕННЫХ ГЕНЕРАТОРОВ
"""пишем формулу для определения факториала числа обычным способом (создаем list). 
Факториал - произведение чисел от 1 до N"""

# def factorial(n):
#     number = 1
#     result = []
#     for i in range(1, n + 1):
#         number *= i
#         result.append(number)
#     return result
# print(factorial(10))

# for i, num in enumerate(factorial(10), start = 1):
#     print(f'{i}! = {num}')

# # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
# # 1! = 1
# # 2! = 2
# # 3! = 6
# # 4! = 24
# # 5! = 120
# # 6! = 720
# # 7! = 5040
# # 8! = 40320
# # 9! = 362880
# # 10! = 3628800

"""НО: зачем хранить целый список, если фактически нам нужно итерироваться по нему
последовательно. Значит, нужно СОЗДАТЬ ГЕНЕРАТОР"""

"""
КОМАНДА YIELD работает аналогично return(возврат значения), но вместо 
завершения функции ЗАПОМИНАЕТ ее СОСТОЯНИЕ (в какой строке (итерации цикла) какое значения). 
Повторный вызов продолжает код после yield.

def gen(*args, **kwargs):
    ...
    yield result
"""

# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
# print(factorial(10))

# for i, num in enumerate(factorial(10), start = 1):
#     print(f'{i}! = {num}')

# # <generator object factorial at 0x000001FC694D1120>

# # 1! = 1
# # 2! = 2
# # 3! = 6
# # 4! = 24
# # 5! = 120
# # 6! = 720
# # 7! = 5040
# # 8! = 40320
# # 9! = 362880
# # 10! = 3628800

"""
Если нужно будет оперировать с данными, мы будем знать алгоритм, согласно 
которому генерируются данные и будем знать, что очередной элемент зависит от 
предыдущего, то мы можем помещать весь алгоритм внутрь такой функции-генератора, 
чтобы не хранить все данные, а задействовать их по мере необходимости
"""

"""
!!! Функции iter() и next() одинаково работают как с генераторами 'из коробки', 
так и с созданными самостоятельно
"""
# Хотим получить объект-итератор для факториала 4. Используем функцию-генератор
# факториалов, и далее применяем iter() и next()

# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number

# my_iter = iter(factorial(4))
# print(my_iter)  # <generator object factorial at 0x0000017DADE01210>
# print(next(my_iter)) # 1
# print(next(my_iter)) # 2
# print(next(my_iter)) # 6
# print(next(my_iter)) # 24
# print(next(my_iter)) # StopIteration

# TEST 

# def gen(a: int, b: int) -> str:
#     if a > b:
#         a, b = b, a
#     for i in range(a, b + 1):
#         yield str(i)

# for item in gen(10, 1):
#     print(f'{item = }')

# # item = '1'
# # item = '2'
# # item = '3'
# # item = '4'
# # item = '5'
# # item = '6'
# # item = '7'
# # item = '8'
# # item = '9'
# # item = '10'