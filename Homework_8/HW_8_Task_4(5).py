# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import json
import pickle


def rename_json(directory):
    for i in os.listdir(directory):   
        root, ext = os.path.splitext(i)
        # print(root, ext)
        if ext == '.json':
            print(i)
            with open(i, 'r', encoding='utf-8') as f_read:
                json_file = json.load(f_read)
            with open(f'{root}.pickle', 'wb') as f_write:
                pickle.dump(json_file, f_write)


rename_json(r'D:\My Documents\docs\Geek Brains\Python_Level-2\Homework_8')
