# Проверка корректности даты

# Вы работаете над разработкой программы для проверки корректности даты, введенной 
# пользователем. На вход будет подаваться дата в формате "день.месяц.год". Ваша задача 
# - создать программу, которая проверяет, является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" 
# (дата некорректна) в зависимости от результата проверки.

# Пример использования На входе:
# date_to_prove = '15.4.2023'
# На выходе:
# True

# На входе:
date_to_prove = '28.02.2023'
# На выходе:
# False

from datetime import date

const1 = 4
const2 = 100
const3 = 400
list30 = [4, 6, 9, 11]

def _check_year(year: int):
    # проверка года на високосность. 1 - обычный, 0 - високосный
    if year % const1 != 0 or year % const2 == 0 and year % const3 != 0:
        return 1
    else:
        return 0  
 
         
my_date = (date_to_prove).split('.')
year, month, day = map(int, reversed(my_date))
if 0 <= year <= 9999:
    if 1 <= month <= 12:
        if month != 2:
            if (month in list30 and 0 < day <= 30) or (month not in list30 and 0 < day <= 31):
                print(True)
            else:
                print(False)
        else:
            if (_check_year(year) == 1 and day == 28) or (_check_year(year) == 0 and day == 29):
                print(True)
            else:
                print(False)
    else:
        print(False)
else:
    print(False)    

# print(month)
# print(month in list30 and day <= 30)     
# print(list(map(int, reversed(my_date))))   
# print(year, month, day)  

# Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную
# защищённую функцию.

# РЕШЕНИЕ СИСТЕМЫ

# from sys import argv

# def is_leap(year: int) :
#     return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

# def valid(full_date: str) :
#     date, month, year = (int(item) for item in full_date.split('.'))
#     if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
#         return False
#     if month in (4, 6, 9, 11) and date > 30:
#         return False
#     if month == 2 and is_leap(year) and date > 29:
#         return False
#     if month == 2 and not is_leap(year) and date > 28:
#         return False
#     return True

# if len(argv) > 1:
#     print(valid(argv[1]))
# else:
#     print(valid(date_to_prove ))