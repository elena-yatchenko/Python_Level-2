# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. 
# При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога (только с этим расширением).
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


"""
файлы для теста собраны в папке Files_for_HW
"""

import os

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
    print('Выполнено')

# можно дополнительно сделать проверку, если нет файлов с таким расширением, чтобы программа дала сообщение 
# (если заданное расширение НЕ в списке имеющихся в файле, к примеру)        


if __name__ == '__main__':
    file_rename('data', 7, 'txt', 'doc', [5, 7])
# file_rename()


# решение семинара

# import os


# def group_rename(desired_name, num_digits, source_ext, target_ext, name_range=None):
#     files = [f.split(source_ext)[0] for f in os.listdir('.')
#              if os.path.isfile(f) and f.endswith(source_ext)]

#     if not files:
#         print("Файлы с заданным расширением не найдены.")
#         return

#     for i, file in enumerate(files, 1):
#         base = ""
#         if name_range:
#             start, end = name_range
#             base = file[start - 1:end]

#         new_name = base + desired_name + f"{i:0{num_digits}}" + target_ext

#         os.rename(f'{file}{source_ext}', new_name)
#         print(f"Переименован файл {file} в {new_name}")


# group_rename("_new", 6, ".txt", ".doc", name_range=[3, 6])


