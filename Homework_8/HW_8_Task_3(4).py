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
                dict_row['name'] = f'{name.title().strip()}'
                dict_row['hash'] = f'{hash(_id + name)}'    
                lst.append(dict_row)
        print(dict_row)
    with open(target_file, 'w') as f:
        for each_dict in lst:
            json.dump(each_dict, f, indent=2)
        print(f'Выполнена запись в файл {target_file}')

csv_to_json('csv_name.csv', 'json_names.json')

# как-то СТРАННО словари выводятся. Некорректно записывает, если на запись даем список словарей. Как в этом случае быть? ((((

# {
#   "level": "1",
#   "id": "0000000224",
#   "name": "Elena",
#   "hash": "1281559312532992807"
# }{
#   "level": "1",
#   "id": "0000000221",
#   "name": "Ruslan",
#   "hash": "5614632612043429335"
# }{
#   "level": "2",
#   "id": "0000000052",
#   "name": "Fgdfgd",
#   "hash": "699102631603888891"
# }

""" читаем с DictReader  и пишем в json в разные словари """

def csv_to_json(source_file, target_file):
    with open(source_file, 'r', newline='') as f:
        csv_read = csv.DictReader(f, fieldnames=['level', 'id', 'name'], dialect='excel', quoting=csv.QUOTE_MINIMAL)
        lst = []
        for dict_row in csv_read:
            lst.append(dict_row)
        # print(lst)
    with open(target_file, 'w') as f:
        for each_dict in lst:
            json.dump(each_dict, f, indent=2)
        print('Записано в отдельные словари')

# csv_to_json('csv_name.csv', 'dict1.json')

""" читаем с DictReader  и пишем в json в один словарь, где по ключу 'level' значения - вложенные словари"""

def csv_to_json(source_file, target_file):
    with open(source_file, 'r', newline='') as f:
        csv_read = csv.DictReader(f, fieldnames=['level', 'id', 'name'], dialect='excel', quoting=csv.QUOTE_MINIMAL)
        dict_test = {str(i): {} for i in range(1, 8)}
        for i, dict_row in enumerate(csv_read):
            if i != 0:
                level, _id, name = dict_row.values()
                dict_test[level].update({_id: name})
        print(dict_test)            

    with open(target_file, 'w') as f:
        json.dump(dict_test, f, indent=2)
        print('Записано в 1 словарь с вложениями')

# csv_to_json('csv_name.csv', 'dict2.json')


