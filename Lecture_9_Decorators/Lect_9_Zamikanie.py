# ЗАМЫКАНИЕ (CLOSURE)

"""
Замыкание (closure) - функция первого класса, в теле которой присутствуют ссылки на переменные, объявленные вне тела этой функции в окружающем 
коде и не являющиеся ее параметрами
"""

# def add_str(a: str, b: str) -> str:
#     return a + ' ' + b

# print(add_str('Hello', 'world'))

# запишем иначе

from typing import Callable   # тип данных, характеризующий фукнцию

def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    
    return add_two_str

# print(add_one_str('Hello')('world'))
"""
* фунцкия add_one_str принимает на вход один параметр в качестве начала строки и возвращает локальную функцию add_two_str (без скобок, т.к. функцию передаем, а не вызываем)
* фукнция add_two_str принимает вторую часть строки, соединяет ее с первой и возвращает ответ
* часть строки add_one_str('Hello') возвращает функцию add_two_str  и уже она вызывается и принимает аргумент во вторых скобках
"""

# ЗАМЫКАЕМ ФУНКЦИЮ С ПАРАМЕТРАМИ

from typing import Callable   # тип данных, характеризующий фукнцию

def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    
    return add_two_str

hello = add_one_str('Hello')
bye = add_one_str('Good bye')

""" в переменные hello и bye поместили результат работы функции add_one_str с разными аргументами. Т.о. они фактически уже являются двумя разными экзмеплярами функции add_two_str"""

# print(hello('world'))
# print(hello('friends'))
# print(bye('wonderful world'))

# # Hello world
# # Hello friends
# # Good bye wonderful world

# print(f'{type(add_one_str) = }, {add_one_str.__name__ = }, {id(add_one_str) = }')
# print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
# print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')

# # type(add_one_str) = <class 'function'>, add_one_str.__name__ = 'add_one_str', id(add_one_str) = 2100200632736
# # type(hello) = <class 'function'>, hello.__name__ = 'add_two_str', id(hello) = 2100196369696
# # type(bye) = <class 'function'>, bye.__name__ = 'add_two_str', id(bye) = 2100200633856

# ЗАМЫКАЕМ ИЗМЕНЯЕМЫЕ И НЕИЗМЕНЯЕМЫЕ ОБЪЕКТЫ

from typing import Callable

# изменяемый тип данных - list

def add_one_str(a: str) -> Callable[[str], str]:
    names = []
    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)
    
    return add_two_str

hello = add_one_str('Hello')
bye = add_one_str('Good bye')

# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))

# # Hello, Alex
# # Hello, Alex, Karina
# # Good bye, Alina
# # Hello, Alex, Karina, John
# # Good bye, Alina, Neo

""" У каждой из фукнций hello и bye оказыается свой список имен. Они не связаны между собой, но каждый хранит список имен до конца работы программы"""

# неизменяемый тип данных - str

def add_one_str(a: str) -> Callable[[str], str]:
    text = ""
    def add_two_str(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text
    
    return add_two_str

hello = add_one_str('Hello')
bye = add_one_str('Good bye')

# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))

# # Hello, Alex
# # Hello, Alex, Karina
# # Good bye, Alina
# # Hello, Alex, Karina, John
# # Good bye, Alina, Neo

"""без добавления строчки NONLOCAL TEXT была бы получена ошибка UnboundLocalError:local variable 'text' referenced before assignment
Как можно изменить неизменяемое? Мы создаем новый объект и присваиваем ему старое имя. А команда nonlocal сообщает Python, что изменения ссылки на объект должны затронуть
область видимости за пределами функции add_two_str
"""

# TEST

def main(x: int) -> Callable[[int], dict[int, int]]: # говорим, что функция main возвращает фунцкию, которая на вход получает число int, а выводит словарь, где ключ и значение тоже являются целыми числами int
    d = {}
    
    def loc(y: int) -> dict[int, int]:
        for i in range (y):
           d[i] = x ** i
        return d
    
    return loc

small = main(42)
big = main(73)
print(small(7))
print(big(7))
print(small(3))

# {0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744}
# {0: 1, 1: 73, 2: 5329, 3: 389017, 4: 28398241, 5: 2073071593, 6: 151334226289}
# {0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744} # т.к. в словаре уже ключи до 6 включительн, то значения ключей от 0 до 2 просто перезапишутся. В итоге словарь не изменится
 