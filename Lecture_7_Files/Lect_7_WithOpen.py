# МЕНЕДЖЕР КОНТЕКСТА WITH OPEN (может работать не только с функцией open())

"""
with open('text_data.txt', 'r+', encoding='utf-8') as f:
    print(list(f))

!!! with гарантирует закрытие файла и сохранение информации

f - файловый дескриптор, переданный в переменную f (аналогично как f = open()). 
Называть переменную можно произвольно
"""


"""!!! запись в файл начинается с места остановки курсора при его чтении перед записью."""