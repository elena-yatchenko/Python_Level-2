# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и все вложенные директории. 
# Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:

# Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория. 
# Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах. Важные детали:

# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.

# Для файлов сохраните их размер в байтах.

# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории, и вложенных директорий.

# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.

# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.

# Для обхода файловой системы вы можете использовать модуль os.

# Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и 
# возвращать результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle) 
# с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.

import os
import json
import csv
import pickle

def size_of_dir(start_path='.'): # по умолчанию путь - текущая папка
    total_size = 0
    for path, dirs, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(path, file) # т.к. функция getsize() берет на вход путь к файлу, размер которого хотим определить
            total_size += os.path.getsize(file_path)
        for dir in dirs:
            dir_path = os.path.join(path, dir)
            total_size += size_of_dir(dir_path) # проходим функцией рекурсивно по папкам (и далее по вложенным в них), чтобы собрать размеры вложенных файлов
    return total_size
        


def save_results_to_json(results, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
      json.dump(results, f, indent=2)  
      

def save_results_to_csv(results, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=['path', 'type', 'size'], dialect='excel', delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        csv_write.writeheader()
        csv_write.writerows(results)
        

def save_results_to_pickle(results, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(results, f)


def traverse_directory(directory) -> list[dict]:
    results = []
    for path, dir, file in os.walk(directory):
        for each_dir in dir:
            path_dir = os.path.join(path, each_dir)
            size_dir = size_of_dir(path_dir)
            results.append({'path': path_dir, 'type': 'directory', 'size': size_dir})
        for each_file in file:
            path_file = os.path.join(path, each_file)
            size_file = os.path.getsize(path_file)
            results.append({'path': path_file, 'type': 'file', 'size': size_file})

    return results

# save_results_to_json(traverse_directory(r'D:\My Documents\docs\Geek Brains\Python_Level-2\Homework_7'), 'results.json')

# save_results_to_csv(traverse_directory(r'D:\My Documents\docs\Geek Brains\Python_Level-2\Homework_7'), 'results_csv')

# save_results_to_pickle(traverse_directory(r'D:\My Documents\docs\Geek Brains\Python_Level-2\Homework_7'), 'results.pickle')


# # решение системы

# import os
# import json
# import csv
# import pickle


# def get_dir_size(start_path='.'):
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(start_path):
#         for f in filenames:
#             fp = os.path.join(dirpath, f)
#             total_size += os.path.getsize(fp)
#         for d in dirnames:
#             dp = os.path.join(dirpath, d)
#             total_size += get_dir_size(dp)
#     return total_size


# def save_results_to_json(results, file_name):
#     with open(file_name, 'w') as f:
#         json.dump(results, f)


# def save_results_to_csv(results, file_name):
#     with open(file_name, 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Path', 'Type', 'Size'])
#         for result in results:
#             writer.writerow([result['Path'], result['Type'], result['Size']])


# def save_results_to_pickle(results, file_name):
#     with open(file_name, 'wb') as f:
#         pickle.dump(results, f)


# def traverse_directory(directory):
#     results = []
#     for root, dirs, files in os.walk(directory):
#         for name in files:
#             path = os.path.join(root, name)
#             size = os.path.getsize(path)
#             results.append({'Path': path, 'Type': 'File', 'Size': size})
#         for name in dirs:
#             path = os.path.join(root, name)
#             size = get_dir_size(path)
#             results.append({'Path': path, 'Type': 'Directory', 'Size': size})
#     return results

save_results_to_json(traverse_directory(r'D:\My Documents\docs\Geek Brains\Python_Level-2\Homework_7'), 'shablon.json')