# a = 42
# print(id(a))  # 140719512348744
# a = 'Hello world'
# print(id(a))  # 2051906031472
# a = 3.14 / 5
# print(id(a))  # 1579858701328

# name = 'Alex'
# age = None

# print(name, age, a, 456, 'test')  # Alex None 0.628 456 test

# # Alex (=^.^=) None (=^.^=) 0.628 (=^.^=) 456 (=^.^=) test
# print(name, age, a, 456, 'test', sep=' (=^.^=) ')

# # Alex @ None @ 0.628 @ 456 @ test#
# print(name, age, a, 456, 'test', sep=' @ ', end='#')

# print(name, age, a, 456, 'test', sep=' @ ', end='#')
# print('Any text')  # Alex @ None @ 0.628 @ 456 @ test#Any text

# res = input('Print your text: ')
# print('Ты написал', res)

# МАГИЧЕСКИЕ ЧИСЛА

# плохой код (с магическим числом)
# age = int(input('Сколько тебе лет? '))
# how_old = 18 - age
# print(how_old, 'осталось до совершеннолетия') # 10 осталось до совершеннолетия

# # хороший код (магическое число заменили константой)
# ADULT = 18 # константа
# age = int(input('Сколько тебе лет? '))
# how_old = ADULT - age
# print(how_old, 'осталось до совершеннолетия') # 10 осталось до совершеннолетия

# pwd = 'text'
# res = input('Input password: ')
# if res == pwd:
#     print('Доступ разрешен')
#     my_math = int(input('2 + 2 = ')) # доп.условие проверки (ВЛОЖЕННЫЕ БЛОКИ)
#     if 2 + 2 == my_math:
#         print('Вы в нормальном мире')
#     else:
#         print('Но будьте осторожны')
# else:
#     print('Доступ запрещён')
# print('Работа завершена')

# MATCH / CASE

# color = input('Your favorite colour: ')
# match color:
#     case 'red'| 'orange':
#         print('1')
#     case 'green':
#         print('2')
#     case 'blue'| 'light blue':
#         print('3')
#     case _:
#         print('4')

# ЛОГИЧЕСКИЕ ОПЕРАТОРЫ

# Определяем високосный ли год: если остаток от деления года на 4 равен 0 или остаток от деления на 100 = 0 и остаток от деления на 400 = 0.
# year = int(input('Введите год в формате уууу'))
# if year % 4 != 0:
#     print('Обычный')
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print('Високосный')
#     else:
#         print('Обычный')
# else:
#     print('Високосный')

# ex. 2100 % 4 = 0, 2100 % 100 = 0, но 2100 % 400 = 100, т.е. не високосный.

# year = int(input('Введите год в формате уууу: '))
# if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
#     print('Обычный')
# else:
#     print('Високосный')

# !!! если в условие не ввести year % 100 == 0, то 2008 год, к примеру, покажет как обычный

# ЛЕНИВЫЙ IF  - особенности операторов or (если хоть 1 True, то все True) и and (если хоть 1 False, то все False)

# ПРОВЕРКА НА ВХОЖДЕНИЕ

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# num = int(input('Enter number: '))
# if num in data:
#     print('Относится к ряду Фибоначчи')

# можно проверять, что число не входит в последовательность (через not): if num not in data

# ТЕРНАРНЫЙ ОПЕРАТОР

# my_math = int(input('2 + 2 = '))
# if 2 + 2 == my_math:
#     print('True')
# else:
#     print('Are you sure?')

# my_math = int(input('2 + 2 = ')) - тернарный ОПЕРАТОР
# print('True' if 2 + 2 == my_math else 'Are you sure?')

# ЦИКЛЫ

# num = float(input('Enter number: '))
# count = 0
# while count < num:
#     print(count)
#     count += 2

# num++ - в Python не работает

# num //= 2
# num -= 2
# num *=
# и т.д. По такому принципу работают все арифметические операции, если они введены без пробела со знаком "="

# CONTINUE

# num = float(input('Enter number: '))
# STEP = 2
# limit = num - STEP
#
# count = -STEP # (чтобы начать счетчик с нуля, вместо записи count = 0, т.к. шаг мы задали через константу.)

# while count < limit:
#     count += STEP
#     # шаг, который позволяет проскочить (не выводить на печать) значение 12
#     if count % 12 == 0:
#         continue
#     print(count)

# num = 16
# 2
# 4
# 6
# 8
# 10
# 14 - число 12 пропущено

# BREAK

# min_limit = 0
# max_limit = 10
# while True: # бесконечный цикл. Останавливается через break
#     print('Введи число между', min_limit, 'и', max_limit, '? ')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Wrong')
#     else:
#         break
# print('Было введено число ', num)

# ELSE в КОНЦЕ ЦИКЛА

# min_limit = 0
# max_limit = 10
# count = 3
# num = None # смотреть коммент ниже

# while count > 0:
#     print('Попытка ', count)
#     count -= 1

#     print('Введи число между', min_limit, 'и', max_limit, '? ')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Wrong')
#     else:
#         break

# else:
#     print('Были исчерпаны все попытки. Сожалею.')
#     quit() # встроенная функция выхода, завершающая работу кода. В скобках можно передавать текст ошибки
# print('Было введено число ', num)

### else Находится на одном уровне с циклом и сработает, если цикл завершится естественным образом. В данном случае, когда исчерпаны все
### попытки, т.е. count стал < 0.


# num = None добавляем в код, т.к. последняя строка print('Было введено число ', num) запрашивает на вывод
# переменную num. Но если кто-то изменит в начале кода значение переменной count (например, сделает -5), то
# код даже не войдет в цикл while, а значит переменная num  и не будет задана. В итоге код выдаст ошибку, что
# такой переменной не существует. num = None позволяет избежать этой ошибки, т.к. мы эту переменную обозначили,
# но пока указали, что она равна "ничего"

# ЦИКЛ FOR IN

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# if item in data:
#     print(item)

# num = int(input('enter number'))
# for i in range(0, num, 2): # от 0 до num (не включая num), с шагом 2
#     print(i)

# Имена переменных в цикле

# count = 10
# for i in range(count):
#     for j in range(count):
#         for k in range(count):
#             print(i, j, k)

# 0 0 0
# 0 0 1
# 0 0 2
# 0 0 3
# 0 0 4
# 0 0 5
# 0 0 6
# 0 0 7
# 0 0 8
# 0 0 9
# 0 1 0
# 0 1 1
# 0 1 2
# 0 1 3
# ...
# ...
# ...
# 9 9 4
# 9 9 5
# 9 9 6
# 9 9 7
# 9 9 8
# 9 9 9

# ключевое слово start позволяет задать значение, с которого хотим начать. Иначе начнет с индекса 0

# animals = ['cat', 'dog', 'wolf', 'rate', 'dragon']
# for i, animal in enumerate(animals):
#     print(i, animal)

# 0 cat
# 1 dog
# 2 wolf
# 3 rate
# 4 dragon

# animals = ['cat', 'dog', 'wolf', 'rate', 'dragon']
# for i, animal in enumerate(animals, start=4):
#     print(i, animal)

# 4 cat
# 5 dog
# 6 wolf
# 7 rate
# 8 dragon

# Task

data = 0
while data < 100:
    data += 3
    if data % 19 == 0:
        continue
    # print(data)
    data += 1
    if data % 40 == 0:
        break
    # print(data)

else:
    data += 5

print(data)  # 80
