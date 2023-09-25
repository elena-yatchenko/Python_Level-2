# ФУНКЦИИ
""" 
Фукнция - это фрагмент кода, к которому можно обратиться из другого
места программы. 
Данные на вход - Функция - Результат (Данные на выход)

ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА - функция, которая принимает функцию-объект как аргумент
или возвращает функцию-объект в виде выходного значения
"""
# a = 42
# # вызываем функцию id
# print(type(a), id(a))  # <class 'int'> 140707942295624
# # передаем функцию id как аргумент
# print(type(id))  # <class 'builtin_function_or_method'>

# """Когда функция вызывается, у нее есть всегда (), когда передается в
# другую функкцию в качестве аргумента, то без скобок"""

# very_bad_programming_style = sum
# # плохой стиль, т.к. используем другое имя для уже существующей функции
# print(very_bad_programming_style([1, 2, 3]))  # 6

# СОЗДАНИЕ ФУНКЦИЙ

# def - от define (определять)

# def my_func():
#     pass

"""Чтобы функция работала, ее нужно не забывать ВЫЗВАТЬ

Зарезервированное слово pass нужно для того, чтобы "ничего не делать".
Т.е. иногда мы обязаны написать какую-то строку кода, но он ничего не делает, тогда используем pass
Например, создаем функцию, но внутренний блок пока не заполнен (тело фукнции), 
или в ООП, когда создаем классы, но пока не прописываем внутри логику
"""
# плохо
# if a != S:
#     pass
# else:
#     a += 1

# # лучше (в некоторых ЯП else является обязательным при if, тогда pass помогает)
# if a == S:
#     a += 1
# else:
#     pass

# # отлично
# if a == S:
#     a += 1

# АРГУМЕНТЫ ФУНКЦИИ - указываются через запятую в круглых скобках после имени функции
# * когда мы определяем функцию аргументы называются параметрами функции, при ее вызове
# и работе - это уже аргументы

# def quadratic_equations(
#     a: int | float, b: int | float, c: int | float
# ) -> tuple[float, float] | float | str:
#     d = b**2 - 4 * a * c
#     if d > 0:
#         return (-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
#     return "Нет решений"

# print(quadratic_equations(2, -3, -9))  # (3.0, -1.5)
"""
минус такой записи: на выходе придется проверять, мы получили строку
или числа. Чтобы это исключить, можно скорректировать функцию, добавив
вместо строки - None для варианта, когда нет корней. Это более универсальный
подход, чем сочетание разных типов данных
"""
def quadratic_equations(
    a: int | float, b: int | float, c: int | float
) -> tuple[float, float] | float | None:
    d = b**2 - 4 * a * c
    if d > 0:
        return (-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None

# ИЗМЕНЯЕМЫЕ И НЕИЗМЕНЯЕМЫЕ АРГУМЕНТЫ
"""
При передаче объекта в фукнцию нужнопомнить, изменяемого типа объект или нет
Неизменяемый аргумент - при изменении внутри функции остается прежним вне функции
Изменяемый аргумент - при изменении внутри функции изменяется и за ее пределами

!!! В Python аргументы передатся внутри функции по ссылке на объект
"""


# def no_mutable(a: int) -> int:
#     a += 1
#     print(f"In func {a = }")  # для демонстрации работы, но не для привычки принтить из фукнции
#     return a

# a = 42
# print(f"In main {a = }")  # In main a = 42
# z = no_mutable(a)  # In func a = 43
# print(f"{a = }\t{z = }")  # a = 42  z = 43

# def mutable(data: list[int]) -> list[int]:
#     for i, item in enumerate(data):
#         data[i] = item + 1
#     print(f'In func {data = }')
#     return data

# my_list = [2, 4,6, 8]
# print(f'in main {my_list = }') # in main my_list = [2, 4, 6, 8]
# new_list = mutable(my_list) # In func data = [3, 5, 7, 9]
# print(f'{my_list = }\t{new_list = }') 
# # my_list = [3, 5, 7, 9] new_list = [3, 5, 7, 9]

# ВОЗВРАТ ЗНАЧЕНИЯ ИЗ ФУНКЦИИ, RETURN
"""
print внутри функции - не лучший вариант, обычно не используют
обычно использование - return (возврат значения). При этом:
- если указан один объект после return - возвращается именно этот объект
- если указано несколько значений через запятую после return - возвращается 
кортеж с перечисленными значениями
- если не указано ничего после return - возвращается None
- если return отсутствует, Python 'мысленно' дописывает в качестве последней
строки функции return None
!!!! Когда срабатывает return функции, если там были другие строки кода, они уже не
принимаются в работу
"""
# для примера рассмотрим ту же функцию, которая считает квадр.уравнения

# print(quadratic_equations(2, -3, -9)) # (3.0, -1.5)

# def no_return(data: list[int]):
#     for i, item in enumerate(data):
#         data[i] = item + 1
#     print(f'In func {data = }')
    
# my_list = [2, 4, 6, 8]
# print(f'In main {my_list = }')
# new_list = no_return(my_list)
# print(f'{my_list = }\t{new_list = }')

# ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ

"""
Зачастую в функции предусмотрены значения по умолчанию, которые указываются после параметров.
Это нужно для того, что если вы забыли внести параметр или функция не находит
какой-то элемент, она подставляет значение по умолчанию
def quadratic_equations(a, b=0, c=0):
Значения по умолчанию указываются с помощью знака равно (=), БЕЗ ПРОБЕЛОВ

"""

# def quadratic_equations(a, b=0, c=0):
#     d = b ** 2 - 4 * a * c
#     if d > 0: 
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
    
# print(quadratic_equations(2, -9)) # (4.5, 0.0). В качестве переменной "с" хранится 0

"""
!!! В качестве значения по умолчанию НЕЛЬЗЯ указывать изменяемые типы: списки, 
словари, множества и т.п.
"""

# def from_one_to_n(n, data=[]):
#     for i in range(1, n + 1):
#         data.append(i)
#     return data

# new_list = from_one_to_n(5)
# print(f'{new_list = }')
# other_list = from_one_to_n(7)
# print(f'{other_list = }')

# # new_list = [1, 2, 3, 4, 5]
# # other_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7]

"""
В этом случае Python при следующем вызове функции взял не пустой список, а 
уже измененный предыдущим вызовом, и дополнил его согласно заданному алгоритму

Чтобы этого избежать, нужно явно показать программе, что когда нужно
брать пустой список, когда нет. Используем переменную None. Т.е. если data =None 
(пользователь не задал список в параметр data), то мы создаем пустой список и
заполняем его. Код ниже: 
!!! ЭТО РЕКОМЕНДУЕМЫЙ ПРИЕМ В ПИТОН. Т.е. при любых изменяемых 
коллекциях мы указываем в качестве значения по умолчанию None и используем проверку
if data is None (можно и ==, но is предпочтительнее для питона)
"""

# def from_one_to_n(n, data=None):
#     if data is None:
#         data = []
#     for i in range(1, n + 1):
#         data.append(i)
#     return data

# new_list = from_one_to_n(5)
# print(f'{new_list = }')
# other_list = from_one_to_n(7)
# print(f'{other_list = }')

# # new_list = [1, 2, 3, 4, 5]
# # other_list = [1, 2, 3, 4, 5, 6, 7]

# ПОЗИЦИОННЫЕ И КЛЮЧЕВЫЕ ПАРАМЕТРЫ

"""
Косая черта / и звездочка * разделяют позиционные и ключевые параметры

def func(positional_only, /, positional_or_keyword, *, keyword_only):
   pass

Ключевые параметры принимают значение ТОЛЬКО ПРИ ЯВНОМ УКАЗАНИИ КЛЮЧА
(через присваивание, т.е. знак "=" без пробелов)
Позиционные параметры принимают значение по позиции
"""
# def standart_arg(arg):
#     print(arg) # принтим для примера, а не для привычки
# """Пример обычной фукнции. Нет ни косой черты, ни звездочки в параметрах, 
# т.е. параметры могут быть и позиционными, и ключевыми"""
    
# standart_arg(42) # 42 
# standart_arg(arg=42) # 42

# def pos_only_arg(arg, /):
#     """ Пример только позиционной функции """
#     print(arg) # принтим для примера, а не для привычки
    
# pos_only_arg(42) # 42
# pos_only_arg(arg=42) # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

# def kwd_only_arg(*, arg):
#     """Пример только ключевой функции"""
#     print(arg) # принтим для примера, а не для привычки
    
# kwd_only_arg(42) # TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
# kwd_only_arg(arg=42) # 42

# def combinated_example(pos_only, /, standart, *, kwd_only):
#     """Пример функции со всеми вариантами параметров"""
#     print(pos_only, standart, kwd_only)
    
# # combinated_example(1, 2, 3) # TypeError: combinated_example() takes 2 positional arguments but 3 were given
# combinated_example(1, 2, kwd_only=3) # 1 2 3
# combinated_example(1, standart=2, kwd_only=3) # 1 2 3
# combinated_example(pos_only=1, standart=2, kwd_only=3) # combinated_example() got some positional-only arguments 
# # passed as keyword arguments: 'pos_only'

# ПАРАМЕТРЫ *ARGS И **KWARGS

"""
Имена args и kwargs - общепринятое соглашение, а так питон смотрит именно на * или **, а называться могут как угодно
- def func(*args): принимает любое число позиционных аргументов
- def func(**kwargs): принимает любое число ключевых аргументов
- def func(*args, **kwargs): принимает любое число позиционных и ключевых аргументов, 

!!! т.е. все позиционные аргументы попадают в args как КОРТЕЖ. А все ключевые попадают в qwargs как СЛОВАРЬ
"""

# def mean(args): # находим среднее арифметическое (сумма элементов на их количество)
#     return sum(args) / len(args) 

# print(mean([1, 2, 3])) # 2.0
# # print(mean(1, 2, 3)) # TypeError: mean() takes 1 positional argument but 3 were given

# def mean (*args):
#     return sum(args) / len(args)

# print(mean(*[1, 2, 3])) # 2.0
# # здесь говорим: РАСПАКУЙ МНЕ СПИСОК И КАЖДЫЙ ЭЛЕМЕНТ ПЕРЕДАЙ КАК ОТДЕЛЬНОЕ ЗНАЧЕНИЕ
# print(mean(1, 2, 3)) # 2.0

# def school_print(**kwargs):
#     for key, value in kwargs.items():
#         print(f'По предмету "{key}" получена оценка {value}')
        
# school_print(химия=5, физика=4, математика=5, физра=5)

# # По предмету "химия" получена оценка 5
# # По предмету "физика" получена оценка 4
# # По предмету "математика" получена оценка 5
# # По предмету "физра" получена оценка 5

# ОБЛАСТИ ВИДИМОСТИ
"""
ЛОКАЛЬНАЯ - код внутри самой функции, т.е. переменные заданные в теле функции существуют
в этой функции, но не существуют за ее пределами
ГЛОБАЛЬНАЯ - все переменные внешнего кода, т.е. переменные, заданные в файле.ру содержащем
функцию
НЕ ЛОКАЛЬНАЯ, nonlocal - код внешней функции, исключающий доступ к глобальным переменным
Т.е. переменные заданы во вложенных функциях,мы можем выходить во внешние функции, чтобы их 
получить, но не доходим до глобальной области видимости, т.е. внешнего кода

!!! Доступ к глобальной КОНСТАНТЕ из тела функции - нормально
"""

# Локальные переменные

# def func(y: int) -> int:
#     x = 100
#     # x += 100
#     print(f'In func {x = }')
#     return y + 1

# x = 42
# print(f'In main {x = }') # In main x = 42
# z = func(x) # In func x = 100
# print(f'{x = }\t{z = }') # x = 42  z = 43

# def func(y: int) -> int:
#     # x = 100
#     x += 100
#     print(f'In func {x = }')
#     return y + 1

# При запуске даст ошибку, UnboundLocalError: cannot access local variable 'x' 
# where it is not associated with a value, т.к. внутри функции локальная 
# переменная х не задана

# Глобальные переменные:

# def func(y: int) -> int:
#     global x # зарезервированное слово, которое говорит, что переменная является глобальной, т.е. берем ее из внешнего кода
#     x += 100
#     print(f'In func {x = }')
#     return y + 1

# x = 42
# print(f'In main {x = }') # In main x = 42
# z = func(x) # In func x = 142
# print(f'{x = }\t{z = }') # x = 142 z = 43
# z1 = func(x) # In func x = 242
# print(z1) # 143

# НЕ локальные переменные

# def  main(a):
#     x = 1
    
#     def func(y):
#         nonlocal x
#         x += 100
#         print(f'In func {x = }')
#         return y + 1
    
#     return x + func(a)

# x = 42
# print(f'In main {x = }') # In main x = 42
# z = main(x) # In func x = 101
"""запустилась функция main(), где мы присвоили х = 1, далее фунцкия func(), в которой мы указали, что х - нелокальная переменна, функция вышла на уровень выше, нашла там  х = 1 и использовала его (1 + 100), дальше искать не пошла"""
# print(f'{x = }\t{z = }') # x = 42  z = 44
""" тут внутрення функция func() вернула return (y + 1) 1 + 1 = 2 (использовав х = 1 из внешней функции main()) + внешняя функция вернула (return x + func(a)) - 42 + 2 = 44."""

# КОНСТАНТЫ - неизменяемый тип данных, мы их не меняем, но можем просто прочитать
# и использовать их внутри функции. Т.е. изнутри функции можно обратиться к константе, 
# заданной во внешнем коде. 
# Константа используется на ЧТЕНИЕ, но НЕ НА ЗАПИСЬ


# LIMIT = 1_000

# def func(x, y):
#     result = x ** y % LIMIT
#     return result

# print(func(42, 73)) # 112

# Анонимная функция LAMBDA (ЛЯМБДА)
"""
запись: lambda parameters: action

Анонимные функции, они же лямбда фукнции - синтаксический сахар для обычных питоновских
фукнций с рядом ограничений. Они позволяют задать функцию в одну строку кода без 
использования других ключевых слов.
"""

# def add_two_def(a, b):
#     return a+ b

# add_two_lambda = lambda a, b: a + b # не совсем правильно, т.к. лямбда - анонимная функция, 
# # и ей не нужно присваивать имя

# print(add_two_def(42, 3.14)) # 45.14
# print(add_two_lambda(42, 3.14)) # 45.14

# my_dict = {'two': 2, 'one': 1, 'four': 4, 'ten': 10}
# s_key = sorted(my_dict.items())
# s_value = sorted(my_dict.items(), key=lambda x: x[1])
# print(f'{s_key = }\n{s_value = }')

# # s_key = [('four', 4), ('one', 1), ('ten', 10), ('two', 2)]
# # s_value = [('one', 1), ('two', 2), ('four', 4), ('ten', 10)]

### ДОКУМЕНТИРОВАНИЕ КОДА функций

"""
Документация пишется сразу после определения функции
ПОяснения к однострочной стоке документации:
- тройные кавычки используются, даже если строка помещается на одной строке. 
Это позволяет леко расширить ее позже
- Закрывающие кавычки находятся на той же строке, что и открывающие, это выгля
дит лучше для однострочников
- Нет пустой строки ни до, ни после строки документации
- Строка документации - это фраза, заканчивающаяся точкой. Она описывает действие
функции или метода как команду
- Однострочная строка документации не должна повторять параметры функции
- Дополнительную информацию, помимо краткого описания функции, добавляют ниже, 
делая отступ в 1 строку
"""

# def max_before_handred(*args):
#     """Return the maximum number not exceeding 100.
    
#     : param args: tuple of int or float numbers
#     : return: int or float number from the tuple args""" 
    
    
#     m = float('-inf')
#     for item in args:
#         if m < item < 100:
#             m = item
#     return m

# print(max_before_handred(-42, 73, 256, 0)) # 73

# # При правильной записи документации указанную информацию о функции можно 
# # получить через help

# help(max_before_handred)

# # Help on function max_before_handred in module __main__:

# # max_before_handred(*args)
# #     Return the maximum number not exceeding 100.

# #     : param args: tuple of int or float numbers
# #     : return: int or float number from the tuple args

    