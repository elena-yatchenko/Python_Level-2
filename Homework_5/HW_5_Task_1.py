# Информация о файле

# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# Пример использования.
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt') 


def get_file_info(file_path: str) -> tuple:
    
    *a, b = file_path.split('/')
    *c, d = b.split('.')
    if file_path.count('/') > 0:
        return f"{'/'.join(a)}/", f"{'.'.join(c)}", f".{d}" 
    else:
        return  f"{'/'.join(a)}", f"{'.'.join(c)}", f".{d}"

print(get_file_info(file_path = 'file_in_current_directory.txt'))

# file_path = '/home/user/docs/my.file.with.dots.txt'
# file_path = 'file_in_current_directory.txt')
# file_path = "C:/Users/User/Documents/example.txt"

# РЕШЕНИЕ СИСТЕМЫ: (НА ПРИМЕРЕ file_path = '/home/user/docs/my.file.with.dots.txt'))


def get_file_info(file_path):
    file_name = file_path.split("/")[-1] # взяли элемент с индексом [-1] получившегося словаря
    print(file_path.split("/"))   # ['', 'home', 'user', 'docs', 'my.file.with.dots.txt']
    print(file_name) # my.file.with.dots.txt
    file_extension = file_name.split(".")[-1] 
    print(file_name.split("."))  # ['my', 'file', 'with', 'dots', 'txt']
    print(file_extension)  # txt
    path = file_path[:-len(file_name)] # срез от начала строки до индекса, равного минус длина file_namе (-21)
    print(path)   # /home/user/docs/
    print(-len(file_name))  # -21
    print(file_name[:-len(file_extension)-1]) # срез от начала строки file_name до элемента с индексом [-4], где доп. -1 - чтобы не включать точку (.txt) 
    
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)

print(get_file_info(file_path = '/home/user/docs/my.file.with.dots.txt'))

