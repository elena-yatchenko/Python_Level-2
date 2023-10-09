# PICKLE МОДУЛЬ - !!! ТОЛЬКО ДЛЯ PYTHON
"""
преобразование объектов Питон в набор(строку) байт или в бинарный файл (для более удобной передачи и хранения)
"""
# В СТРОКУ - DUMPS()

# import pickle

# my_dict = {
#     "first_name": "Джон",
#     "last_name": "Смит",
#     "hobbies": ["кузнечное дело", "программирование", "путешествия"],
#     "age": 35,
#     "children": [
#         {
#             "first_name": "Алиса",
#             "age": 5
#         },
#         {
#             "first_name": "Маруся",
#             "age": 3
#         }
#     ]
# }

# print(my_dict)
# res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
# print(f'{res =}')


# # {'first_name': 'Джон', 'last_name': 'Смит', 'hobbies': ['кузнечное дело', 'программирование', 'путешествия'], 'age': 35, 'children': [{'first_name': 'Алиса', 'age': 5}, 
# # {'first_name': 'Маруся', 'age': 3}]}

# # res =b'\x80\x04\x95\xe3\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\nfirst_name\x94\x8c\x08\xd0\x94\xd0\xb6\xd0\xbe\xd0\xbd\x94\x8c\tlast_name\
# x94\x8c\x08\xd0\xa1\xd0\xbc\xd0\xb8\xd1\x82\x94\x8c\x07hobbies\x94]\x94(\x8c\x1b\xd0\xba\xd1\x83\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd0\
# xbe\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\x94\x8c \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\
# xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\x94\x8c\x16\xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f\x94e\
# x8c\x03age\x94K#\x8c\x08children\x94]\x94(}\x94(h\x01\x8c\n\xd0\x90\xd0\xbb\xd0\xb8\xd1\x81\xd0\xb0\x94h\nK\x05u}\x94(h\x01\x8c\x0c\xd0\x9c\xd0\
# xb0\xd1\x80\xd1\x83\xd1\x81\xd1\x8f\x94h\nK\x03ueu.'

# В БИНАРНЫЙ ФАЙЛ - DUMP() 

# import pickle

# def func(a, b, c):
#     return a + b + c

# my_dict = {
#     "numbers": [42, 4.1415, 7 + 3j],
#     "functions": (func, sum, max),
#     "others": {True, False, 'Hello world'},
# }

# with open('my_dict.pickle', 'wb') as f:
#     pickle.dump(my_dict, f)

# ДЕСЕРИАЛИЗАЦИЯ (ИЗ БИНАРНОГО ФАЙЛА/СТРОКИ БАЙТ - В ПИТОН)
"""из строки байт"""

# import pickle

# data = b'\x80\x04\x95\xe3\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\nfirst_name\x94\x8c\x08\xd0\x94\xd0\xb6\xd0\xbe\xd0\xbd\x94\x8c\tlast_name\x94\x8c\x08\xd0\xa1\xd0\xbc\xd0\xb8\xd1\x82\x94\x8c\x07hobbies\x94]\x94(\x8c\x1b\xd0\xba\xd1\x83\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\x94\x8c \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\x94\x8c\x16\xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f\x94e\x8c\x03age\x94K#\x8c\x08children\x94]\x94(}\x94(h\x01\x8c\n\xd0\x90\xd0\xbb\xd0\xb8\xd1\x81\xd0\xb0\x94h\nK\x05u}\x94(h\x01\x8c\x0c\xd0\x9c\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd1\x8f\x94h\nK\x03ueu.'

# new_dict = pickle.loads(data)
# print(f'{new_dict = }')

# # new_dict = {'first_name': 'Джон', 'last_name': 'Смит', 'hobbies': ['кузнечное дело', 'программирование', 'путешествия'], 'age': 35, 'children': [{'first_name': 'Алиса', 
# # 'age': 5}, {'first_name': 'Маруся', 'age': 3}]}

"""из бинарного файла"""

# import pickle

# def func(a, b, c):
#     return a * b * c

# with open('my_dict.pickle', 'rb') as f:
#     new_dict = pickle.load(f)
# print(f'{new_dict = }')
# print(f'{new_dict["functions"][0](2, 3, 4) = }')


# # new_dict = {'numbers': [42, 4.1415, (7+3j)], 'functions': (<function func at 0x000001F9A0D404A0>, <built-in function sum>, 
# # <built-in function max>), 'others': {False, True, 'Hello world'}}

# # new_dict["functions"][0](2, 3, 4) = 24 - при восстановлении pickle увидел другую функцию func, не с суммой, которая была в файле, 
# # из которого сохраняли словарь my_dict. Чтобы восстановилась исходная функция, она должна присутствовать в файле, в который восстанавливаются данные

# TEST

import pickle

my_dict = {'numbers': [42, 4.1415, (7+3j)],
           'functions': (sum, max),
           'others': {True, False, 'Hello world'}
           }
res = pickle.dumps(my_dict)
print(res)
with open('quest.pickle', 'wb') as f:
    pickle.dump(f'{res =}', f) 

""" в последней строке pickle.dump(f'{res =}', f) говорим: возьми результат res (набор байт), представь этот набор байт в виде строки текста,
полученную строку (где есть уже и текст,и байты) надо сериализовать и записать в файл. Т.е. по сути сделали двойную сериализацию: в первый раз словарь - 
в набор байт, второй раз - строку текста - в бинарный файл"""

