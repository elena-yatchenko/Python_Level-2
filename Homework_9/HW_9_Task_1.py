
# Генерация случайных данных и нахождение корней квадратного уравнения
# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке, 
# от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

import csv
from random import randint
import os
import math

def generate_csv_file(file_name, rows):
    os.chdir(r'C:\Users\User\Documents\PC_Data\Study\Python_Level-2\Homework_9')
    n = 3
    min_num = -5
    max_nam = 5
    all_data = []
    for i in range(rows):
        line = []
        for j in range(n):
            line.append(randint(min_num, max_nam))
        all_data.append(line)
    with open (file_name, 'w', newline='', encoding='utf-8') as f:      
        csv_write = csv.writer(f, dialect='excel', quoting=csv.QUOTE_MINIMAL) # delimiter
        csv_write.writerows(all_data)

# generate_csv_file('random_numbers.csv', 10)

# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0. 
# Функция принимает три аргумента:

# a, b, c (целые числа) - коэффициенты квадратного уравнения.

# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).


def find_roots(a, b, c):
    pass
    discrim = pow(b,2) - 4 * a * c 
    sq_root = pow(discrim, 0.5) # находим квадратный корень дискриминанта
    """Она принимает два параметра: какое число возводить и в какую степень возводить. 
    Если вызывать pow() без параметров, то Python выдаст следующее: 
    "TypeError: pow expected at least 2 arguments, got 0" ."""
    if discrim > 0:
        print((-b + sq_root) / (2 * a)) 
        print((-b - sq_root) / (2 * a))
    elif discrim == 0:
        print((-b -sq_root) / (2 * a))  # фактически, формула -b / 2*a, т.к. корень 0 - ноль.
    else: # при отрицательном дискриминанте уравнение не имеет действительных корней, но Питон по умолчанию считает
        # в этом случае в комплексных числах (когда есть мнимая единица, которая позволяет брать корень из отрицательного числа)
        print((-b + sq_root) / (2 * a))
        print((-b - sq_root) / (2 * a))



# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

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