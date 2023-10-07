"""автоматическая генерация файлов заданной длины, расширения, в заданном количестве и в заданную директорию"""

__all__ = ['my_func', 'generate_to_destination']

from random import choices, randint
from string import ascii_lowercase, digits
from pathlib import Path
import os

def my_func(ext: str='txt', min_name: int=6, max_name: int=30, min_size: int=256, max_size: int=4096, count: int=42):
    
    for i in range(count):
        my_data = bytes(randint(0, 255) for i in range(min_size, max_size))
        name_of_file = "".join(choices(ascii_lowercase + digits, k=randint(min_name, max_name)))
        if os.path.exists(f"{name_of_file}.{ext}"): # проверка, если в текущей папке уже есть файл с таким именем, тогда пропускаем
            continue
        with open(f'{name_of_file}.{ext}', 'wb') as data:
            data.write(my_data)
            
def generate_to_destination(direct, **kwargs):
    # Отсутствие/наличие директории не должно
    # вызывать ошибок в работе функции (добавьте проверки).
    if not os.path.exists(direct): # если путь не существует, создаем нашу целевую папку (mkdir)
        os.mkdir(direct)
    os.chdir(direct)  # переходим в нашу целевую папку
    for key, value in kwargs.items():
        my_func(ext=key, count=value) # генерируем в целевой папке файлы (задачи 4-5)

if __name__ == '__main__':   
    generate_to_destination(r'D:\My Documents\docs\Geek Brains\Python_Level-2\Task_checking', txt=2, bin=3)   