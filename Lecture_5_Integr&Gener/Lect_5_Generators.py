# ГЕНЕРАТОРЫ

"""Генератор - некая функция, которая получает данные на вход и на основании этих 
данных генерирует какую-то последовательность. При каждом вызове функции генератор
создает определенный элемент последовательности, согласно прописанному алгоритму, 
возвращает его и ждет следующего вызова

Основное назначение генераторов - использование их внутри циклов, в частности
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
??? Когда выбирать генераторные выражения, а когда генератор списка
- Если на выходе нужен готовый список - ГЕНЕРАТОР СПИСКА (квадратные скобки)
- Если элементы нужны последовательно - ГЕНЕРАТОРНОЕ ВЫРАЖЕНИЕ (круглые скобки)
"""



