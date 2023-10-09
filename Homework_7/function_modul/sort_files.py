# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки

import os
import shutil
from pathlib import Path

__all__ = ['file_sort', 'sort_dict']

def file_sort(sort_dir: str):

    sort_dict = {'video': ['mp4', 'mp3', 'mkv'], 'image': ['jpeg', 'png'], 'text': ['txt', 'doc']}

    os.chdir(sort_dir)

    for key, value in sort_dict.items():
        for file in os.listdir():
            if file.split('.')[-1] in value:
                
                # проверка, есть ли в каталоге уровнем выше папка, одноименная ключу. Если нет - создаем
                if not os.path.exists(os.path.join('..', key)): 
                    os.chdir('..')
                    os.mkdir(key) 
                    os.chdir(sort_dir)
                   
                curr_path = os.path.join(os.getcwd(), file)
                
                # проверка, существует ли файл с таким именем в папке назначения
                if not os.path.exists(os.path.join('..', key, file)):
                    target_path = os.path.join('..', key, file)
                else:
                    target_path = os.path.join('..', key, f'another_{file}')
                    
                shutil.move(curr_path, target_path)
        



if __name__ == '__main__':
    file_sort(r'C:\Users\User\Documents\PC_Data\Study\Python_Level-2\Homework_7\Mix')