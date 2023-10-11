# Задание №7
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

# sourse_file = 'csv_name.csv'
import csv
import pickle
import json

def csv_to_pickleStr(sourse_file):
    with open(sourse_file, 'r', newline='', encoding='utf-8') as f_read:
        lst = []
        for i, line in enumerate(f_read):
            meanings = line.strip().split(',')
            #list_dict = {}
            if i == 0:
                keys = meanings
            else:
                values = meanings
                list_dict = {}
                for j in range(len(keys)):
                    key = keys[j]
                    list_dict[key] = values[j]
                #print(list_dict) 
                lst.append(list_dict)
        return lst

my_dict = str(csv_to_pickleStr('csv_name.csv'))
res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
print(res)

"""был еще вариант
str_for_pickle = ''
for elem in csv_to_pickleStr('csv_name.csv'):
    str_for_pickle += str(elem)
res = pickle.dumps(str_for_pickle, protocol=pickle.DEFAULT_PROTOCOL)
print(res)
"""
# НЕ ПОНИМАЮ ПО РЕЗУЛЬТАТУ print(res) ПРАВИЛЬНО ЭТО ИЛИ НЕТ. одинаково не то что-то :)
# зато в json симпатично записалось вроде

with open('Task_6.json', 'w') as f:
    json.dump(csv_to_pickleStr('csv_name.csv'), f, indent=2)