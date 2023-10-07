""" функция для группового переименования файлов """

import os

__all__ = ['file_rename', 'file_list', 'full_new_name']

def file_rename(new_name: str='new', num_count: int=5, ext_curr: str='bin', ext_new: str='txt', rest: list=None):
    file_list = os.listdir()
    n = 1
    for obj in file_list:
        if os.path.isfile(obj):
            if obj.split('.')[-1] == ext_curr:
                if rest != None:
                    full_new_name = f'{obj[rest[0]:rest[1]+1]}-{new_name}_{n:0{num_count}}.{ext_new}'
                else:
                    full_new_name = f'{new_name}_{n:0{num_count}}.{ext_new}'
                os.rename(obj, full_new_name)
                n += 1


if __name__ == '__main__':
    file_rename('data', 7, 'txt', 'doc', [5, 7])