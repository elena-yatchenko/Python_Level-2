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

res = pickle.dumps(csv_to_pickleStr('csv_name.csv'), protocol=pickle.DEFAULT_PROTOCOL)
print(res)

# b'\x80\x04\x95D\x01\x00\x00\x00\x00\x00\x00]\x94(}\x94(\x8c\x05level\x94\x8c\x011\x94\x8c\x02id\x94\x8c\x03224\x94\x8c\x04name\x94\x8c\x05elena\x94u}
# \x94(h\x02h\x03h\x04\x8c\x03221\x94h\x06\x8c\x06ruslan\x94u}\x94(h\x02\x8c\x012\x94h\x04\x8c\x0252\x94h\x06\x8c\x06fgdfgd\x94u}\x94(h\x02h\x0ch\x04\x8c\x03999
# \x94h\x06\x8c\x06mixail\x94u}\x94(h\x02\x8c\x013\x94h\x04\x8c\x0274\x94h\x06\x8c\x07frfegrg\x94u}\x94(h\x02h\x13h\x04\x8c\x03312\x94h\x06\x8c\x04alex\x94u}
# \x94(h\x02h\x13h\x04\x8c\x03334\x94h\x06\x8c\x07dmitriy\x94u}\x94(h\x02\x8c\x014\x94h\x04\x8c\x03111\x94h\x06\x8c\x05masha\x94u}\x94(h\x02\x8c\x015\x94h\x04
# \x8c\x03668\x94h\x06\x8c\x07dmitriy\x94u}\x94(h\x02h!h\x04\x8c\x03989\x94h\x06\x8c\x07irishka\x94u}\x94(h\x02h!h\x04\x8c\x03661\x94h\x06\x8c\x06serega\x94ue.'

# with open('Task_6.json', 'w') as f:
#     json.dump(csv_to_pickleStr('csv_name.csv'), f, indent=2)