# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json  

def csv_to_json(source_file, target_file):
    with open(source_file, 'r', newline='') as f:
        lst = []
        for i, line in enumerate(f):
            dict_row = {}
            level, _id, name = line.split(',')   
            if i != 0:
                dict_row['level'] = level
                dict_row['id'] = f'{int(_id):010}'
                dict_row['name'] = name.title()
                dict_row['hash'] = f'{hash(_id + name)}'    
                lst.append(dict_row)
        
    with open(target_file, 'w') as f:
        for each_dict in lst:
            json.dump(each_dict, f, indent=2)

csv_to_json('file_name.csv', 'json_names.json')

# как-то СТРАННО словари выводятся ((((


