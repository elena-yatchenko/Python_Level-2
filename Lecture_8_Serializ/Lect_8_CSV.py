# CSV - ФОРМАТ - текстовый формат, предназначенный для представления табличных данных
# !!!! import csv

# import csv

# ЧТЕНИЕ CSV - csv.reader()
"""По умолчанию при чтении CSV любое значение превращается в СТРОКУ"""

# with open('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f)
#     for line in csv_file:
#         print(line)
#         print(type(line))

# # ['Name', 'Sex', 'Age', 'Heihgt (in)', 'Weight (lbs)']
# # <class 'list'>
# # ['Alex', 'M', '41', '74', '170']
# # <class 'list'>
# # ['Bert', 'M', '42', '68', '166']
# # <class 'list'>
# # ['Elly', 'F', '30', '66', '124']
# # <class 'list'>
# # [' '] -  !!! в любом случае список, даже если там пустая строка или 1 элемент
# # <class 'list'>

# ДОПОЛНИТЕЛЬНЫЕ ПАРАМЕТРЫ ДЛЯ READER() - на примере csv, где в качестве разделителя - символ табуляции

"""
dialect='excel-tab' - т.к. табуляция вместо разделителя (по умолчанию dialect='excel', где разделитель запятая)
quoting=csv.QUOTE_NONNUMERIC - числа без кавычек нужно преобрезовать в тип float (как-то не сработало, проверить дома)
"""
# import csv

# with open('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line}\t{type(line)}')

# # ['Name', 'Sex', 'Age', 'Heihgt (in)', 'Weight (lbs)']   <class 'list'>
# # ['Alex', 'M', 41.0, 74.0, 170.0]        <class 'list'>
# # ['Bert', 'M', 42.0, 68.0, 166.0]        <class 'list'>
# # ['Elly', 'F', 30.0, 66.0, 124.0]        <class 'list'>

# ЗАПИСЬ CSV - CSV.WRITER(). Доп.параметры, аналогичные reader()

# import csv

# with (
#     open('biostats.csv', 'r', newline='') as f_read,
#     open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
# ):
#     csv_read = csv.reader(f_read, dialect='excel',quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.writer(f_write, dialect='excel-tab', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     all_data = []
#     for i, line in enumerate(csv_read):
#         if i == 0:
#             csv_write.writerow(line) # записываем первую строку с заголовками сразу, остальные обрабатываем
#         else:
#             line[2] += 1    # +1 к возрасту
#             for j in range(2, 4 + 1): 
#                 line[j] = int(line[j]) # преобразование значений в 3-5 столбцах (индексы 2-4) от float к int
#             all_data.append(line)
#     csv_write.writerows(all_data) # запись оставшегося списка разом

"""
что видим в новом созданном файле  new_biostats.csv:
Name Sex Age |Heihgt (in)| |Weight (lbs)|
Alex M 42 74 170
Bert M 43 68 166
Elly F 31 66 124
"""

# ЧТЕНИЕ CSV В СЛОВАРЬ - csv.DictReader() - итерируется ПОСТРОЧНО, КАЖДАЯ СТРОКА - СЛОВАРЬ. Ключи - названия столбцов (или fieldnames).

import csv

# with open ('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=['name', 'sex', 'age', 'height', 'weight', 'office'], restkey='new',restval="Main Office",
#                               dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line =}')
#         print(f'{line["name"] =}\t{line["age"] = }')

# # line ={'name': 'Name', 'sex': 'Sex', 'age': 'Age', 'height': 'Heihgt (in)', 'weight': 'Weight (lbs)', 'office': 'Main Office'}
# # line["name"] ='Name'    line["age"] = 'Age'
# # line ={'name': 'Alex', 'sex': 'M', 'age': 41.0, 'height': 74.0, 'weight': 170.0, 'office': 'Main Office'}
# # line["name"] ='Alex'    line["age"] = 41.0
# # line ={'name': 'Bert', 'sex': 'M', 'age': 42.0, 'height': 68.0, 'weight': 166.0, 'office': 'Main Office'}
# # line["name"] ='Bert'    line["age"] = 42.0
# # line ={'name': 'Elly', 'sex': 'F', 'age': 30.0, 'height': 66.0, 'weight': 124.0, 'office': 'Main Office'}
# # line["name"] ='Elly'    line["age"] = 30.0

"""пример использования RESTKEY. Всегда в качестве значения содержит СПИСОК, даже если в нем один элемент"""

# with open ('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=['name', 'sex', 'age'], restkey='new',restval="Main Office",
#                               dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line =}')
#         print(f'{line["name"] =}\t{line["age"] = }')

# # line ={'name': 'Name', 'sex': 'Sex', 'age': 'Age', 'new': ['Heihgt (in)', 'Weight (lbs)']}
# # line["name"] ='Name'    line["age"] = 'Age'
# # line ={'name': 'Alex', 'sex': 'M', 'age': 41.0, 'new': [74.0, 170.0]}
# # line["name"] ='Alex'    line["age"] = 41.0
# # line ={'name': 'Bert', 'sex': 'M', 'age': 42.0, 'new': [68.0, 166.0]}
# # line["name"] ='Bert'    line["age"] = 42.0
# # line ={'name': 'Elly', 'sex': 'F', 'age': 30.0, 'new': [66.0, 124.0]}
# # line["name"] ='Elly'    line["age"] = 30.0

# ЗАПИСЬ ИЗ СЛОВАРЯ В CSV

# import csv

# with (
#     open('biostats.csv', 'r', newline='') as f_read,
#     open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
# ):
#     csv_read = csv.DictReader(f_read, fieldnames=['name', 'sex', 'age', 'height', 'weight', 'office'], restval="Main Office",
#                                dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.DictWriter(f_write, ['id', 'name', 'office', 'sex', 'age', 'height', 'weight'], dialect='excel-tab', quoting=csv.QUOTE_ALL)
#     csv_write.writeheader()  # сразу записали заголовки
#     all_data = []
#     for i, dict_row in enumerate(csv_read):
#         if i != 0: # пропускаем первый словарь, где в значениях - заголовки из файла biostats.csv
#             dict_row['id'] = i
#             dict_row['age'] += 1
#             all_data.append(dict_row) # добавляем в список словарь {key1: value1, key2: value2, ....}
#     csv_write.writerows(all_data)

"""
в файле new_biostats.csv получаем следующее

"id"	"name"	"office"	"sex"	"age"	"height"	"weight"
"1"	"Alex"	"Main Office"	"M"	"42.0"	"74.0"	"170.0"
"2"	"Bert"	"Main Office"	"M"	"43.0"	"68.0"	"166.0"
"3"	"Elly"	"Main Office"	"F"	"31.0"	"66.0"	"124.0"
"""

import csv

with open('quest.csv', 'w', newline='', encoding='utf-8') as f_write:
    csv_write = csv.DictWriter(f_write, fieldnames=["numbers", "names", "data"], restval='Hello world', dialect='excel', 
                               delimiter='#', quotechar='=', quoting=csv.QUOTE_NONNUMERIC)
    csv_write.writeheader()
    dict_row = {}
    for i in range(10):
        dict_row["numbers"] = i
        dict_row["names"] = str(i)
        csv_write.writerow(dict_row)



