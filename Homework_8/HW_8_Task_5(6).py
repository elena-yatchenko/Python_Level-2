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

def pickle_to_csv(sourse_file, target_file):
    with open(sourse_file, 'rb') as f:
        my_dict = pickle.load(f)

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
        print(data_list)
        write_file.writerows(data_list)
        print(f'Выполнена запись в файл {target_file}')



pickle_to_csv('results.pickle', 'task_5.csv')

