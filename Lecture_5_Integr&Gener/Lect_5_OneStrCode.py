# ОДНОСТРОЧНИКИ

# Классика пайтон - ОБМЕН ПЕРЕМЕННЫМИ в 1 строку
# # a,b = b, a

# a = 42
# b = 73
# a,b = b, a
# print(f'{a = }\t{b = }')  # a = 73  b = 42
"""Обычно в коде, когда есть знак =, сначала выполняется код справа от знака равно, 
потом тот, что слева. Т.е. сначала создается кортеж (b, a), потом он распаковывается 
в переменные a и b. Обменивать можно более 2 переменных. 
!!! Главное, количество переменных справа и слева от знака равно(=) должно СОВПАДАТЬ"""

# РАСПАКОВКА

"""
- Обычная распаковка a, b, c = последовательность
- Распаковка с упаковкой a, *b, c = последовательность - в звездочку(*) упакуется все лишнее
- Распаковка со звездочкой  *последовательность
"""

# a,b,c = input('Три символа: ')
# print(f'{a = } {b = } {c = }')
# # Три символа: 258
# # a = '2' b = '5' c = '8'
# # Три символа: 2489  - ValueError: too many values to unpack (expected 3)

# a,b,c = ('один', 'два', 'три',)
# print(f'{a=} {b=} {c=}') # a='один' b='два' c='три'

# a,b,c = ('один', 'два', 'три', 'четыре', 'пять')
# print(f'{a=} {b=} {c=}') # ValueError: too many values to unpack (expected 3)

# как избежать ошибки соответствия количества переменных - распаковка с упаковкой *
# !!! звездочкой можно пометить ТОЛЬКО ОДНУ переменную. Иначе получим ошибку
# data = ('один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь',)
# a, b, c, *d = data
# # a='один' b='два' c='три', ['четыре', 'пять', 'шесть', 'семь']
# print(f'{a=} {b=} {c=} {d=}')

# a, b, *c, d = data
# # a='один' b='два' c=['три', 'четыре', 'пять', 'шесть'], семь
# print(f'{a=} {b=} {c=} {d=}')

# a, *b, c, d = data
# # a='один' b=['два', 'три', 'четыре', 'пять'] c='шесть', семь
# print(f'{a=} {b=} {c=} {d=}')

# *a, b, c, d = data
# # a=['один', 'два', 'три', 'четыре'] b='пять' c='шесть', семь
# print(f'{a=} {b=} {c=} {d=}')

# *_ распаковка/упаковка. * говорит запаковать сюда все, что осталось, а _ - что эта переменная нам не нужна в будущем

# link = 'https://icgroups.bitrix24.ru/company/personal/user/11/tasks/task/view/189'
# prefix, *_, suffix = link.split('/')
# # в префикс попадает самый первый элемент полученного списка http or https
# # в суффикс - самая последняя ее часть
# print(prefix, suffix) # https: 189

""" Распаковка   *последовательность. Тут звездочка - аналоги цикла for in, т.е. говорит 
распаковать последовательность и передать символы по одному """

# data = [2, 4, 6, 8, 10, ]
# for item in data:
#     print(item, end='\t') # 2       4       6       8       10
# print()

# data = [2, 4, 6, 8, 10, ]
# print(*data, sep='\t') # 2       4       6       8       10

# МНОЖЕСТВЕННОЕ ПРИСВАИВАНИЕ И СРАВНЕНИЕ - объединяем несколько операций в одну

"""
-Присваивание: a = b = c = 0, 
a, b, c = 1, 2, 3
- Cравнение: a == b == c
a < b < c
!!! Множественное присваивание допустимо ТОЛЬКО ДЛЯ НЕИЗМЕНЯЕМЫХ типов данных
"""

""" МНОЖЕСТВЕННОЕ ПРИСВАИВАНИЕ """

# a = b = c = 0 # хорошо
# a += 42
# print(f'{a=} {b=} {c=}') # a=42 b=0 c=0

# a = b = c = {1, 2, 3} # плохо - потому что используем множественное присваивание множественной коллекции
# # поэтому изменяются все переменные при изменении одной из них
# a.add(42)
# print(f'{a=} {b=} {c=}') # a={1, 2, 3, 42} b={1, 2, 3, 42} c={1, 2, 3, 42}

# ЧАСТНЫЙ случай обмена переменными

# a, b, c = 1, 2, 3 # количество переменных справа и слева совпадает, в итоге каждой переменной - свое значение
# print(f'{a=} {b=} {c=}') # a=1 b=2 c=3

# t = 1, 2, 3 # слева от знака "=" одна переменная, справа несколько - получаем кортеж значений
# print(f'{t=}, {type(t)}') # t=(1, 2, 3), <class 'tuple'>

""" МНОЖЕСТВЕННОЕ СРАВНЕНИЕ """

# a = b = c = 42
# # if a == b and b == c:
# if a == b == c:
#     print('Полное совпадение')
# if a < b < c:
#     print('b больше a и меньше c')

""" ПЛОХИЕ ОДНОСТРОЧНИКИ """

# a = 12; b = 42; c = 73
# if a < b < c: b = None; print('Ужасный код')

""" ';' не используется в питоне, плохо читаемый код без отступов"""

# TEST

# data = {10, 9, 8, 1, 6, 3}
# a, b, c, *d, e = data
# print(a, b, c, d, e) # 1 3 6 [8, 9] 10
"""внутри множества для хранения элементов используется механизм хэширования, где для каждого из 
элементов вычисляется хэш, который по сути является индексом, согласно которому элементы располагаются
внутри множества. Т.о. на выходе у нас элементы множества в переменные разложатся по возрастанию (т.к. возрастает и хэш)"""


