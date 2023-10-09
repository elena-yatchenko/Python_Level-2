# def func(path_numb: str, path_name: str, path_result: str):
#     with (
#         open(path_numb, 'r', encoding='utf-8') as data_numbers,
#         open(path_name, 'r', encoding='utf-8') as data_name,
#         open(path_result, 'a', encoding='utf-8') as result,
        
#     ):
#         len_numb = sum(1 for i in data_numbers) 
#         len_name = sum(1 for i in data_name)
#         # data_numbers.seek(0)
#         # data_name.seek(0)
        
#         for i in range(max(len_numb, len_name)): 
#             numb = string_step(data_numbers)
#             name = string_step(data_name)
#             num_i, num_f = numb.split('|') 
#             mult = int(num_i) * float(num_f)
#             if mult < 0:
#                 result.write(f'{name.lower()} {-mult}\n')
#             if mult > 0:
#                 result.write(f'{name.upper()} {mult: .0f}\n') 
                                
        
      
# def string_step(name_file): 
#     text = name_file.readline()
#     if text == "":
#         name_file.seek(0) 
#         text = name_file.readline()
#     return text.strip() 
        
# func('text.txt', 'text_name.txt', 'text_result.txt')

# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо
# именами и произведением чисел.
# Напишите функцию, которая создаёт из
# созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import os
import json

with open('text_result.txt', 'r', encoding='utf-8') as f:
    new_dict = {}
    for line in f:
        name, number = line.split()
        new_dict[name.capitalize()] = float(number)
        
with open('json_result.json', 'w', encoding='utf-8') as f:
     json.dump(new_dict, f, indent=2, ensure_ascii=False)
     