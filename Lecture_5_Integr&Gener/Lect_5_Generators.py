# ГЕНЕРАТОРЫ

"""Генератор - некая функция, которая получает данные на вход и на основании этих 
данных генерирует какую-то последовательность. При каждом вызове функции генератор
создает определенный элемент последовательности, согласно прописанному алгоритму, 
возвращает его и ждет следующего вызова

Основное НАЗНАЧЕНИЕ генераторов - ИСПОЛЬЗОВАНИЕ ИХ ВНУТРИ ЦИКЛОВ в частности
for in.

Особенность генератора - он не хранит сразу все значения, а генерирует их последовательно, 
поэтому не занимает много места в памяти."""

# RANGE(start, stop, step) - генератор из коробки

# a = range(0, 10, 2)
# print(f'{a = }, {type(a) = }, {a.__sizeof__()}, {len(a)}')
# # a = range(0, 10, 2), type(a) = <class 'range'>, 48, 5  (len - 5 значений)
# b = range(-1_000_000, 1_000_000, 2)
# print(f'{b = }, {type(b) = }, {b.__sizeof__()}, {len(b)}')
# # b = range(-1000000, 1000000, 2), type(b) = <class 'range'>, 48, 1000000

# ГЕНЕРАТОРНЫЕ ВЫРАЖЕНИЯ - в Python позволяют создать собственный генератор, перебирающий
# значения.

"""Общий вид генераторного выражения
gen = (expression for expr in sequence1 if condition1
        for expr in sequence2 if condition2
        for expr in sequence3 if condition3
        ... 
        for expr in sequenceN if conditionN)
"""
"""Аналог генераторного выражения на Питон
for expr in sequence1:
    if not conditon:
        continue
    for expr in sequence2: 
        if not conditon:
            continue
            ...
        for expr in sequenceN: 
            if not conditon:
                continue
                
Количество вложенных циклов и любые входящие проверки - могут быть различными
"""

# my_gen = (chr(i) for i in range(97, 123))
# print(my_gen) # <generator object <genexpr> at 0x0000027CA525D700>
# for char in my_gen:
#     print(char)
# a
# b
# c
# d
# e и т.д.   

# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)= }\t{len(y) =}') # len(x)= 7       len(y) =6
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# res = list(mult)
# print(f'{len(res) = }\n{res}')

# len(res) = 25
# [3, 7, 25, 121, 721, 3, 7, 25, 121, 721, 5, 9, 27, 123, 723, 7, 11, 29, 
# 125, 725, 15, 19, 37, 133, 733]

# LIST COMPREHENSION (похоже на генератор, но таковым не является)

"""
list_comp = [expression for expr in aequence1 in condition1 ...]

Генератор списков формирует list, заполненный данными, и присваивает его переменной
Аналогично может быть несколько вложенных циклов и несколько условий
!!!! Отличие от генератора - квадратные скобки вместо круглых. 
Т.е. тут получаем на выходе объект СПИСОК, а для генератора объект - ГЕНЕРАТОР
"""

# my_listcomp = [chr(i) for i in range(97, 102)]
# print(my_listcomp)
# for char in my_listcomp:
#     print(char)
# ['a', 'b', 'c', 'd', 'e']
# a
# b
# c
# d
# e    

# data = [2, 5, 1, 42, 65, 76, 24, 77]
# res = []
# for item in data:
#     if item % 2 == 0:
#         res.append(item)
# print(f'{res = }') # res = [2, 42, 76, 24]

# data = [2, 5, 1, 42, 65, 76, 24, 77]
# res = [item for item in data if item % 2 == 0]
# print(f'{res = }') # res = [2, 42, 76, 24]

""" 
??? 
!!!! COMPREHENTION (ЛИСТ,СЛОВАРЬ ИЛИ МНОЖЕСТВО) НЕ РАВНО (!=) ГЕНЕРАТОР
Когда выбирать генераторные выражения, а когда генератор списка
- Если на выходе нужен ГОТОВЫЙ список - ГЕНЕРАТОР СПИСКА (квадратные скобки).
Например, нужно обращаться к элементам по индексу или использовать их не 
последовательно, а в каком-то случайном порядке.
- Если элементы нужны ПОСЛЕДОВАТЕЛЬНО - ГЕНЕРАТОРНОЕ ВЫРАЖЕНИЕ (круглые скобки)
Генераторное выражение сразу все элементы не хранит, в итоге - экономия памяти
# """
# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)= }\t{len(y) =}') 
# res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
# print(f'{len(res) = }\n{res}')

# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# for item in mult:
#     print(f'{item =}')

# len(x)= 7       len(y) =6
# len(res) = 25
# [3, 7, 25, 121, 721, 3, 7, 25, 121, 721, 5, 9, 27, 123, 723, 7, 11, 29, 125, 725, 15, 19, 37, 133, 733]
# item =3
# item =7
# item =25
# ...
# item =133
# item =733    

# ГЕНЕРАЦИЯ МНОЖЕСТВ И СЛОВАРЕЙ

"""
!!! НИКОГДА НЕ ГОВОРИТЬ НА РУССКОМ ГЕНЕРАТОРЫ СПИСКОВ ИЛИ МНОЖЕСТВ (ОСОБЕННО НА СОБЕСЕДОВАНИЯХ), ЭТО НЕПРАВИЛЬНО. ЛУЧШЕ НАЗЫВАТЬ ЭТО 
COMPREHENTION ДЛЯ СЛОВАРЕЙ И ДЛЯ МНОЖЕСТВ

!!! Условие ПЕРЕД ЦИКЛОМ пишется только если используется запись в виде тернарного оператора
Например, развернутое ниже условие записано в виде List comprehention с использованием тернарного оператора

# развернутое решение
fizzbuzz = []
for i in range(1, 101):
    if i % 15 == 0:
        fizzbuzz.append('FizzBuzz')
    elif i % 3 == 0:
        fizzbuzz.append('Fizz')
    elif i % 5 == 0:
        fizzbuzz.append('Buzz')
    else:
        fizzbuzz.append(i)
print(fizzbuzz)

my_dig = ['Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else 'FissBuzz' if i % 3 == 0 and i % 5 == 0 else i for i in range(1, 101)]
print(my_dig)
"""

"""
- Set comprehentions
set_comp = {expression for expr in sequence1 if condition1...}
- Dict comprehensions
dict_comp = {key: value for expr in sequence1 if condition1...}

Сходства и различия: 
* {используются фигурные скобки для выражения}
* словарь подставляет ключ и значение через двоеточие
"""
# my_setcomp = {chr(i) for i in range(97, 101)}
# print(my_setcomp)
# for char in my_setcomp:
#     print(char)

# # {'a', 'b', 'd', 'c'}
# # a
# # b
# # d
# # c

# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)= }\t{len(y) =}') 
# res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
# print(f'{len(res) = }\n{res}')

# # len(x)= 7       len(y) =6
# # len(res) = 19
# # {3, 5, 133, 7, 9, 11, 15, 19, 25, 27, 29, 37, 721, 723, 725, 733, 121, 123, 125}  

"""на выходе получаем не 25, как в списке, а 19 элементов. Т.к. множество хранит только
уникальные значения. 
Кроме того, порядок элементов в множестве распределяется согласно хэшу, что не совпадает 
с порядком в списке"""

# my_dictcomp = {i: chr(i) for i in range(97, 101)}
# print(my_dictcomp)
# for number, char in my_dictcomp.items():
#     print(f'dict[{number}] = {char}')

# # {97: 'a', 98: 'b', 99: 'c', 100: 'd'}
# # dict[97] = a
# # dict[98] = b
# # dict[99] = c
# # dict[100] = d

# TEST

# data = {2, 4, 4, 6, 8, 10, 12}
# res1 = {None: item for item in data if item > 4}
# res2 = (item for item in data if item > 4)
# res3 = [[item] for item in data if item > 4]
# print(res1) # {None: 12}
"""ключ словаря всегда уникален, т.о. по факту 4 раза перезаписываем значение для одного
и того же ключа и сохраняется то, что было записано последним"""
# print(res2) # <generator object <genexpr> at 0x00000224D185C040>
"""получили объект-генератор"""
# print(res3) # [[6], [8], [10], [12]]
"""список из вложенных списков, состоящих из 1 элемента. Т.е. матрица 4 х 1"""







