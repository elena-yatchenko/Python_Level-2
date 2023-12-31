# Задание №1

# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

text = sorted(input('Введите строку: ').split()) # сортировка по значению
print(text)

# text = sorted(input('Введите строку: ').split(), key=len) # сортировка по длине
# print(text)

max_word_len = len(max(text, key=len))

def printed(list):
    for pos, word in enumerate(text, 1):
        print (f'{pos} {word:>{max_word_len}}')
   
printed(text)

# Введите строку: Вывести функцией каждое слово с новой строки.
# ['Вывести', 'каждое', 'новой', 'с', 'слово', 'строки.', 'функцией']
# 1  Вывести
# 2   каждое
# 3    новой
# 4        с
# 5    слово
# 6  строки.
# 7 функцией