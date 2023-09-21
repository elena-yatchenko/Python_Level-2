# СЛОВАРИ - DICT

"""
Словарь - набор пар ключ-значение. Где КЛЮЧ - НЕИЗМЕНЯЕМАЯ структура. Ключом может быть
целое число, вещественное число (редко), строка текста или неизменяемая коллекция
(tuple, frozenset). Неизменяемый ключ словаря ссылается на значение (может быть 
изменяемое или неизменяемое).

Ключи внутри словаря УНИКАЛЬНЫ (не могут повторяться), а значения могут. 
"""
# СОЗДАНИЕ СЛОВАРЯ

# dict(x) - создаем словарь
# {key: value} - тоже создаем словарь

# a = {'one': 42, 'two': 3.14, 'ten': 'Hello world'}
# b = dict(one=42, two=3.14, ten='Hello world')
# c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world')])
# # т.е. если имеем последовательность из кортежей по 2 элемента, можем сформировать из них словарь
# print(a)
# print(b)
# print(c)
# # {'one': 42, 'two': 3.14, 'ten': 'Hello world'}
# # {'one': 42, 'two': 3.14, 'ten': 'Hello world'}
# # {'one': 42, 'two': 3.14, 'ten': 'Hello world'}

# print(a == b == c) # True

""" 
НЕЛЬЗЯ использовать зарезервированные слова в качестве ключей словаря. 
Если очень надо, то использовать 1-й или 3-й варианты создания словаря 
(из показанных выше)
"""
# ДОБАВЛЕНИЕ НОВОГО ЭЛЕМЕНТА в словарь

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# x = 10
# my_dict['ten'] = x
# print(my_dict)  # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}

# ДОСТУП К ЗНАЧЕНИЮ СЛОВАРЯ

# dict[key] - доступ через квадратные скобки
# dict.get(key, [default]) - доступ через метод get
""" 
Используя ключ, можно получить доступ к значению, используя значение получить доступ к ключу - нет.
В обратную сторону это не работает
"""

# TEN = 'ten'
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}

# print(my_dict['two']) # 2
# print(my_dict[TEN]) # 10
# print(my_dict[1]) # KeyError: 1

# через метод get()

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}

# print(my_dict.get('two')) # 2
# print(my_dict.get('five')) # None - такого ключа нет в словаре (None, но не ошибка)
# print(my_dict.get('five', 5)) # 5. Тут второй передаваемый аргумент - значение по 
# # умолчанию (default). Т.е. метод не находит такого ключа (а значит и значения для него), 
# # и возвращает значение, заданное по умолчанию
# print(my_dict.get('ten', 5)) # 10 - тут находит такой ключ и его значение, значит значение
# по умолчанию не понадобилось, метод его игнорирует.

# МЕТОДЫ РАБОТЫ СО СЛОВАРЯМИ

"""
* SETDEFAULT() - возвращает значение и добавляет ключ в словарь
* KEYS() - возвращает объект-итератор dict_keys
* ITEMS() - возвращает объект-итератор dict_items
* VALUES() - возвращает объект-итератор dict_values
* POPITEM() - удаляет последнюю пару ключ-значение
* POP() - удаляет пару ключ-значение по ключу
* UPDATE()- расширяет исходный словарь новыми парами
"""
# SETDEFAULT()

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.setdefault('five')
# print(f'{spam = }\t{my_dict=}')
# # spam = None     my_dict={'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'five': None}
# '''Вернул ключ None, т.к. такого значения не было, после добавил это значение в словарь'''

# eggs = my_dict.setdefault('six', 6)
# print(f'{eggs = }\t{my_dict=}')
# # eggs = 6        my_dict={'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'five': None, 'six': 6}
# """Здесь в аргументах метода задали значение default (по умолчанию) для ключа "six" - 6 и метод его добавил и вернул это значение в переменную eggs """

# new_spam = my_dict.setdefault('two')
# print(f'{new_spam = }\t{my_dict=}')
# # new_spam = 2    my_dict={'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'five': None, 'six': 6}
# """Значение для такого ключа есть, оно попадает в переменную new_spam, содержимое словаря не меняется"""

# new_eggs = my_dict.setdefault('one', 1000)
# print(f'{new_eggs = }\t{my_dict=}')
# # new_eggs = 1    my_dict={'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'five': None, 'six': 6}
"""Обращаемся к существующему ключу, у него есть значение - 1, это значение выводится в переменную new_eggs
и содержимое словаря не изменяется. Т.к. добавление значения, указанного в аргументе default (у нас это 1000)
происходит только тогда, когда указанный ключ в словаре отсутствует"""

""" Что за символ \t?
'\t' — табуляция (отступ в несколько пробелов); 
'\r' — возврат каретки (перевод курсора в первую позицию текущей строки); 
'\b' — возврат курсора на один символ назад с удалением этого символа."""

# KEYS

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.keys()) # dict_keys(['one', 'two', 'three', 'four', 'ten'])

# чаще используется в циклах
# for key in my_dict.keys():
#     print(key)

# one  
# two  
# three
# four 
# ten 

# если не указан конкретный метод, по умолчанию работает keys(). т.е. аналогично код ниже сработает без вызова .keys() 

# for key in my_dict:
#     print(key)

# # one  
# # two  
# # three
# # four 
# # ten

# VALUES() - работает аналогично, но со значениями, а не с ключами

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.values())

# for value in my_dict.values():
#     print(value)

# 1
# 2
# 3
# 4
# 10

# ITEMS()

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.items())

# # dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), ('ten', 10)])

# for tuple_data in my_dict.items(): # плохо
#     print(tuple_data)
#     print(f'{tuple_data[0] = } value before 100 - {100 - tuple_data[1]}')

# # ('one', 1)
# # tuple_data[0] = 'one' value before 100 - 99
# # ('two', 2)
# # tuple_data[0] = 'two' value before 100 - 98
# # ('three', 3)
# # tuple_data[0] = 'three' value before 100 - 97
# # ('four', 4)
# # tuple_data[0] = 'four' value before 100 - 96
# # ('ten', 10)
# # tuple_data[0] = 'ten' value before 100 - 90

# for key, value in my_dict.items(): # хорошо
#     print(f'{key = } value before 100 - {100 - value}')

# # key = 'one' value before 100 - 99
# # key = 'two' value before 100 - 98
# # key = 'three' value before 100 - 97
# # key = 'four' value before 100 - 96
# # key = 'ten' value before 100 - 90

# POPITEM() - удаление последней пары ключ-значение (при этом ВОЗВРАЩАЯ УДАЛЕННУЮ ПАРУ ключ-значение)
""" работает по методу LIFO: last input - first out, т.е. удаляется последняя пара 
(последней была добавлена в словарь). Питон запоминает в какой последовательности
были добавлены пары в словарь"""

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.popitem()
# print(f'{spam = }\t{my_dict = }')
# eggs = my_dict.popitem()
# print(f'{eggs = }\t{my_dict = }')

# # spam = ('ten', 10)      my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# # eggs = ('four', 4)      my_dict = {'one': 1, 'two': 2, 'three': 3}

# POP() - удаляет пару ключ-значение по ключу

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.pop('two')
# print(f'{spam = }\t{my_dict = }')

# # spam = 2        my_dict = {'one': 1, 'three': 3, 'four': 4, 'ten': 10}

# err = my_dict.pop('six') # KeyError: 'six' -  не смогли найти в словаре такого ключа и произвести удаление
# err = my_dict.pop() # TypeError: pop expected at least 1 argument, got 0

"""В случае со словарем метод pop() не может запускаться без аргумента (ключа, по которому нужно удалить).
Выдаст ошибку"""

# UPDATE() - расширение старого словаря значениями из нового словаря

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# my_dict.update(dict(six=6))
# print(my_dict)
# # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'six': 6}

# my_dict.update(dict([('five', 5), ('two', 42)]))
# print(my_dict)
# # {'one': 1, 'two': 42, 'three': 3, 'four': 4, 'ten': 10, 'six': 6, 'five': 5}

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
# print(new_dict)
# # {'one': 1, 'two': 42, 'three': 3, 'four': 4, 'ten': 10, 'five': 5, 'six': 6}

"""с версии Питона 3.10 появляется новый способ объединения (обновления) словарей, 
когда в новый словарь объединяются(апдейт) все словари, перечисленные через вертикальную 
черту "|". Причем словари могут быть записаны в разном формате. ОДИН И ТОТ ЖЕ КЛЮЧ, 
то в качестве ЗНАЧЕНИЯ для него будет добавлено то, КОТОРОЕ ВСТРЕТИЛОСЬ ПОЗЖЕ
"""
# TEST

# my_dict = {'one': 1,
#            'two': 2,
#            'three': 3,
#            'four': 4,
#            'ten': 10,
#            }
# print(my_dict.setdefault('ten', 555)) # 10
# print(my_dict.values()) # dict_values([1, 2, 3, 4, 10])
# print(my_dict.pop('one')) # 1 - вывел удаленное значение

# my_dict['one'] = my_dict['four']
# print(my_dict) 

# {'two': 2, 'three': 3, 'four': 4, 'ten': 10, 'one': 4} 
# заменяет значение ключа 'one' и добавляет его в конце, т.к. ранее мы удалили эту пару (через pop('one'))
# иначе просто заменил бы значение этого ключа, оставив его на своем месте.





