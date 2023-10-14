
# Генерация случайных данных и нахождение корней квадратного уравнения
# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке, 
# от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0. 
# Функция принимает три аргумента:

# a, b, c (целые числа) - коэффициенты квадратного уравнения.

# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах и результатах вычислений 
# для каждой строки данных из CSV-файла.

import csv
from random import randint
import os
import json

def generate_csv_file(file_name, rows):
    os.chdir(r'D:\My Documents\docs\Geek Brains\Python_Level-2\Homework_9')
    n = 3
    min_num = -5
    max_nam = 5
    all_data = []
    for i in range(rows):
        line = []
        while len(line) < n:
            a = randint(min_num, max_nam)
            if a == 0:  # исключаем из результата 0, т.к. a не может быть равно 0 в квадратном уравнении
                continue
            line.append(a)
        all_data.append(line)
    with open (file_name, 'w', newline='', encoding='utf-8') as f:      
        csv_write = csv.writer(f, dialect='excel', quoting=csv.QUOTE_MINIMAL) # delimiter
        csv_write.writerows(all_data)
        
# решение системы (лучше)
# def generate_csv_file(file_name, rows):
#     with open(file_name, 'w', newline='') as f:
#         writer = csv.writer(f)
#         for i in range(rows):
#          !!! здесь тоже нужно доработать, чтобы исключить 0 из результата рандомного подбора
#             row = [random.randint(1, 1000) for _ in range(3)]
#             writer.writerow(row)

"""
задаем изначально функцию поиска квадратных корней (декорируемая функция ) с параметрами a, b, c, но потом вызываем ее с параметром "имя файла", в который генерируются случайные числа.
в фунцкии обертке мы принимаем в качестве аргумента (*args) этот файл, считываем его, распаковываем на переменные a,b,c и вызываем нашу декорируемую функцию
уже с этими переменными
"""
def save_to_json(func):
    def wrapper(*args):
        with open(args[0], 'r', newline='') as f:  #пишем args[0], т.к. просто args - это кортеж, а мы подразумеваем, что будем открывать файл, т.е. д.б. строка - название
            csv_data = csv.reader(f)
            data_list = []
            for line in csv_data:
                a, b, c = map(int, line)
                result = func(a, b, c)
                curr_dict = {"parameters": [a, b, c], "result": result}
                data_list.append(curr_dict)
        with open('result.json', 'w') as write_f:
            json.dump(data_list, write_f, indent=2)
        return f'Данные записаны в "result.json" файл'               
    return wrapper


@save_to_json
def find_roots(a, b, c):
    pass
    discrim = pow(b,2) - 4 * a * c 

    if discrim < 0:
        return None
    elif discrim == 0:
        return (-b - discrim ** 0.5) / (2 * a)
    else: 
        x1 = (-b + discrim ** 0.5) / (2 * a)
        x2 = (-b - discrim ** 0.5) / (2 * a)
        return x1, x2  


# print(find_roots(-5, 2, 3))

generate_csv_file('random_numbers.csv', 15)
find_roots('random_numbers.csv')



# Пример

# На входе:


# generate_csv_file("input_data.csv", 101)
# find_roots("input_data.csv")

# with open("results.json", 'r') as f:
#     data = json.load(f)

# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

# print(len(data)==101)
# На выходе:


# True
# True

# Задача 1 (решение системы)

import csv
import json
import random

def save_to_json(func):
    def wrapper(*args):
        result_list = []
        with open(*args, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                data = {'parameters': [a, b, c], 'result': result}
                result_list.append(data)
            print(result_list)
        with open('test_file.json', 'w') as f:
            json.dump(result_list, f, indent=2)
    return wrapper

"""Решение квадратных уравнений Квадратное уравнение имеет вид: ах2+вх+с = 0, где а, в, с - действительные числа и а НЕ равно нулю."""

@save_to_json
def find_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

#generate_csv_file('test_file.csv', 10)
# find_roots('random_numbers.csv')