# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы
# с разными расширениями. Расширения и количество файлов
# функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from string import ascii_lowercase, digits
from random import choices, randint

def my_func(ext: str='txt', min_name: int=6, max_name: int=30, min_size: int=256, max_size: int=4096, count: int=42):
    
    for i in range(count):
        my_data = bytes(randint(0, 255) for i in range(min_size, max_size))
        name_of_file = "".join(choices(ascii_lowercase+digits, k=randint(min_name, max_name)))
        with open(f'{name_of_file}.{ext}', 'wb') as data:
            data.write(my_data)
            
# print(my_func(count=12))

# def new_func(**kwargs):
#     for key, value in kwargs.items():
#         my_func(ext=key,count=value) 
    
    
# new_func(txt=2, bin=3)

# def new_func(**kwargs):
#     for ext, count in kwargs.items():
#         my_funk(ext, count=count)


# new_func(txt=2, bin=3)

# 6
# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию - отдельный параметр функции.
# Отсутствие/наличие директории не должно
# вызывать ошибок в работе функции (добавьте проверки).
# Существующие файла не должны удаляться/изменяться в случае совпадения имён.

from pathlib import Path
import os


def new_func(direct, **kwargs):
    if not os.path.exists(direct):
        os.mkdir(direct)
    os.chdir(direct)  
    for key, value in kwargs.items():
            my_func(ext=key,count=value)
    
new_func(r'D:\My Documents\docs\Geek Brains\Python_Level-2\Homework_1', txt=2, bin=3)       


# if os.path   name_of_file in 





# from random import choices, randint
# from string import ascii_lowercase, digits
# from pathlib import Path
# import os


# def my_funk(
#         ext: str = "txt",
#         min_name: int = 6,
#         max_name: int = 30,
#         min_size: int = 256,
#         max_size: int = 4096,
#         count: int = 42
# ):
#     for i in range(count):
#         my_data = (bytes(randint(0, 255) for i in range(randint(min_size, max_size))))
#         name_of_file = "".join(choices(ascii_lowercase + digits, k=randint(min_name, max_name)))
#         if os.path.exists(f"{name_of_file}.{ext}"):
#             continue
#         with open(f"{name_of_file}.{ext}", 'wb') as data:
#             data.write(my_data)


# # my_funk(count=2)


# def new_func(direct, **kwargs):

#     if not os.path.exists(direct):
#         os.mkdir(direct)
#     os.chdir(direct)
#     for ext, count in kwargs.items():
#         my_funk(ext, count=count)


# new_func(r'C:\Users\79853\PycharmProjects\pythonProject5\123', txt=2, bin=3)