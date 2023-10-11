# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
import shutil
from pathlib import Path

"""сортированные папки находятся в том же каталоге (Homework_7), что и папка со смешанными файлами (Mix). Если их нет - создаем по ключу.
Если в целевой папке уже существует файл с таким именем, перемещение все равно делаем, но добавляем перед именем 
нового файла слово 'another_' 
В функцию передаем абсолютный путь к папке, где находятся файлы, которые нужно рассортировать"""

"""можно добавить в функцию параметр sort_dict: dict[Path, list[str]]=None, и составить шаблон словаря, чтобы пользователь 
сам задавать параметр словаря, какие форматы файлов и в какие папки хочет распределять. Если не задал (т.е. sort_dict будет None, 
то поставить условие, чтобы использовался встроенный шаблон, который составим для функции по умолчанию
"""

def file_sort(sort_dir: str):

    sort_dict = {'video': ['mp4', 'mp3', 'mkv'], 'image': ['jpeg', 'png'], 'text': ['txt', 'doc']}

    # mix_dir = 'D:\My Documents\docs\Geek Brains\Python_Level-2\Homework_7\Mix'

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
        

# for key, value in sort_dict.items():
#     print(os.path.abspath((os.path.join('.', key)))) # получение абсолютного пути по относительному

if __name__ == '__main__':
    file_sort('D:\My Documents\docs\Geek Brains\Python_Level-2\Homework_7\Mix')

"""
В chdir()
"""