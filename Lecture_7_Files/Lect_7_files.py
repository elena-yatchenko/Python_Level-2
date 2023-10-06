# ФАЙЛЫ

"""
Директория, папка, каталог - по сути одно и то же
Файлы могут храниться не только в компе, где угодно. даже в оперативной памяти
"""
# ФУНКЦИЯ OPEN()
""" Для работы с файлами в питоне используют функцию Open()

open(file, mode='r', buffering=-1, encoding=None,
errors=None, newline=None, closed=True, opener=None)
mode - вид доступа, по умолчанию - чтение
!!! encoding='utf-8' - лучше указывать всегда по умолчанию
"""
f = open('text_data.txt')
# # прописываем такой путь, т.к. находимся в той же папке, 
# # где сам файл, т.е. не нужно указывать полный путь

# print(f)
# # <_io.TextIOWrapper name='text_data.txt' mode='r' encoding='cp1252'>

print(list(f))

# РЕЖИМЫ РАБОТЫ С ФАЙЛАМИ (их можно сочетать)
"""
* r - открыть для чтения (по умолчанию)
* w - открыть для записи, предварительно очистив файл
* x - открыть для эксклюзивного создания. Вернет ошибку, если файл уже существует
и там уже есть инфо (не затрет)
* a - открыть для записи в конец файла, если он существует (дописывает, не затирая)
* b - двоичный режим (добавляется к предыдущим буквам) - говорит, что работаем
не в текстовом, а в бинарном режиме (т.е. пишем не текст, а набор байт)
* t - текстовый режим (добавляется к предыдущим буквам) - говорит, что работаем
в текстовом режиме (по умолчанию указан)
* + - дополнительная запись (к чтению запись и к записи чтение). 
Например, r+ - можем читать и дописывать(не затирая), 
w+ - можем дописывать, но при этом и читать (сотрет сначала).
"""

# f = open('text_data.txt', 'a', encoding='utf-8')
# f.write('Окончание файла\n')
# f.close()

# МЕТОД CLOSE()

"""
f.close()

Если в коде отсутствует метод close(), то даже при успешном завершении
программы не гарантируется сохранение всех данных в файле (как выдернуть флешку 
в последнюю секунду записи)
"""
f = open('bin_data', 'wb', buffering=64)
# режим создания файла для записи, причем записи бинарных данных

f.write(b'X' * 1200)
# Х - один байт, *1200 - хотим получить 1200 таких байт
f.close()

# buffering=64 (определяет, какими порциями записывается информация) - лучше не передавать ничего, если точно не разбираешься что писать)
# пусть по умолчанию используется размер буферизации оперативной системы

""" 
Прочие необязательные параметры функции open()
* buffering - определяет режим буферизации
* errors - используется только в текстовом режиме и определяет поведение в случае
ошибок кодирования или декодирования (чтобы не получать ошибку, а получать доп.инфо, экранируя ошибки)
* newline - отвечает за преобразование окончания строки
*closefd - указывает оставлять ли файловый дескриптор открытым
при закрытии файла (рекомендуется его не трогать)
* opener - позволяет передавать пользовательскую функцию для открытия файла, лучше пока тоже не лезть
"""

# !!! при работе с бинарными данными кодировка не прописывается, она важна в текстовом режиме
f = open('data.txt', 'wb')
f.write('Привет'.encode('utf-8') + 'мир'.encode('cp1251'))
f.close()

# Привет��� - в нашем текстовом файле

# f = open('data.txt', 'r', encoding='utf-8')
# print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 12: invalid continuation byte, т.к. часть текста в одной кодировке, часть в другой
# f.close()

f = open('data.txt', 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()
# ['Привет���'] - смогли вывысти благодаря обработке ошибок errors='replace'
