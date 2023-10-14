# Задание №6
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированиЯ возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

# pickle_file = 'results.pickle'

import pickle
import csv
from pathlib import Path

# для списка словарей

def pickle_to_csv(sourse_file, target_file):
    with open(sourse_file, 'rb') as f:
        my_dict = pickle.load(f)
        # print(my_dict) # список словарей, где все нужные заголовки - ключи словаря


    with open(target_file, 'w', newline='', encoding='utf-8') as f_write:
        write_file = csv.writer(f_write, dialect='excel', delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
        data_list = []
        for i, dict_row in enumerate(my_dict):
            if i == 0:
                title_list =[]
                for key in dict_row.keys():
                    title_list.append(key)
                write_file.writerow(title_list)

            data_list.append(dict_row.values())
        # print(data_list)
        write_file.writerows(data_list)
        print(f'Выполнена запись в файл {target_file}')



# pickle_to_csv('results.pickle ', 'task_5_1.csv')

# решение преподавателя (для списка словарей)
# def pickle_to_csv(file_name):
#     with (open(file_name, 'rb') as f_pickle,
#           open(f'{file_name.stem}.csv', "w", newline='', encoding='utf-8') as f_csv):
#         new_dict = pickle.load(f_pickle)

#         csv_write = csv.DictWriter(
#             f_csv,
#             fieldnames=["size", "type", "path"],
#             dialect='excel',
#             delimiter=',',
#             quoting=csv.QUOTE_NONNUMERIC)

#         csv_write.writeheader()
#         csv_write.writerows(new_dict)


# pickle_to_csv(Path('results.pickle'))


""" когда заданный файл - не список словарей, а словарь с вложенными (тут не вытаскиваю названия ключей, сразу задаю их) """

def pickle_to_csv(sourse_file, target_file):
    with open(sourse_file, 'rb') as f:
        my_dict = pickle.load(f)
        # print(my_dict) # словарь с вложенными словарями

    with open(target_file, 'w', newline='', encoding='utf-8') as f_write:
        write_file = csv.DictWriter(
            f_write, 
            dialect='excel', 
            fieldnames=["level", "id", "name", "hash"],
            delimiter='|', 
            quoting=csv.QUOTE_NONNUMERIC)
        data_list = []
        for level, include_dict in my_dict.items():
            for _id, value_list in include_dict.items():
                name, hash = value_list
                data_list.append({'level': level, 'id': _id, 'name': name, 'hash': hash})
        #print(data_list)
        write_file.writeheader()
        write_file.writerows(data_list)
        print(f'Выполнена запись в файл {target_file}')



pickle_to_csv('json_names.pickle', 'task_5_2.csv')