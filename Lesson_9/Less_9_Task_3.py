"""
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции
"""
import json 
import os

def deco(func):
    my_dict = {}
    def wrapper(*args, **kwargs):
        file_name = f'{func3.__name__}.json'
        if os.path.exists(file_name):
           with open(file_name, 'r', encoding='utf-8') as file_r:
               my_dict = json.load(file_r)
        my_dict[str(args)] = args # json не хочет в качестве ключа кортеж, а строка - точно неизменяемый
        my_dict.update(**kwargs)
       
       
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(my_dict, file, indent=2, ensure_ascii=False)
        return my_dict 
    return wrapper

@deco
def func3(*args, **kwargs): #  тут может быть хоть просто а
    return args, kwargs

print(func3(2, 5, 3, n=5, w='s', t=25))
# {(2, 5, 3): (2, 5, 3), 'n': 5, 'w': 's', 't': 25}
print(func3(x='x'))
# {(2, 5, 3): (2, 5, 3), 'n': 5, 'w': 's', 't': 25, (): (), 'x': 'x'}

print(func3(k='uyt'))


# import json
# import os


# def deco(func):
#     my_dict = {}

#     def wrapper(*args, **kwargs):
#         file_name = f'{func.__name__}.json'
#         if os.path.exists(file_name):
#             with open(file_name, 'r', encoding='utf-8') as file:
#                 my_dict = json.load(file)
#         my_dict[str(args)] = str(args)
#         my_dict.update(**kwargs)

#         with open(file_name, 'w', encoding='utf-8') as file:
#             json.dump(my_dict, file, indent=2, ensure_ascii=False)
#         return my_dict

#     return wrapper


# @deco
# def func(*args, **kwargs):
#     return args, kwargs


# # print(func(5, 2, 3, 4, n=5, w='s', t='y'))
# print(func(l='74'))