# Доработаем предыдущую задачу.(4)


from string import ascii_lowercase, digits
from random import choices, randint

def my_func(ext: str='txt', min_name: int=6, max_name: int=30, min_size: int=256, max_size: int=4096, count: int=42):
    
    for i in range(count):
        my_data = bytes(randint(0, 255) for i in range(min_size, max_size))
        name_of_file = "".join(choices(ascii_lowercase+digits, k=randint(min_name, max_name)))
        with open(f'{name_of_file}.{ext}', 'wb') as data:
            data.write(my_data)
            
# print(my_func(count=12))

# Создайте новую функцию которая генерирует файлы
# с разными расширениями. Расширения и количество файлов
# функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

def new_func(**kwargs):
    for key, value in kwargs.items():
        my_func(ext=key,count=value) 
    
    
new_func(txt=2, bin=3)

# def new_func(**kwargs):
#     for ext, count in kwargs.items():
#         my_funk(ext, count=count)


# new_func(txt=2, bin=3)





