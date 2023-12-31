# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так,
# чтобы у самого длинного слова был один пробел между ним и номером строки
 
lst = (input('Введите строку: ').split()) # сразу выведем введенную пользователем строку в список из слов строки через split()

# print(lst)

max_word = (max(lst, key=len)) # нашли максимальное слово. Задаем атрибут key, чтобы искать максимальное не по значению, а по длине слова.
# print(max_word)
max_word_len = len(max(lst, key=len)) # нашли длину максимального слова
# print(max_word_len)


for position, elem in enumerate(lst, 1):
    print(f'{position}  {elem:>{max_word_len}}') 

# печатаем каждое слово из списка слов строки с отступом, равным длине самого длинного слова
    
# Введите строку: Статусное содержание — это страницы, удовлетворяющие некоторым критериям качества и предназначенные быть образцом для написания других страниц Википедии
# ['Статусное', 'содержание', '—', 'это', 'страницы,', 'удовлетворяющие', 'некоторым', 'критериям', 'качества', 'и', 'предназначенные', 'быть', 'образцом', 'для', 'написания', 'других', 'страниц', 'Википедии']
# удовлетворяющие
# 15
# 1        Статусное
# 2       содержание
# 3                —
# 4              это
# 5        страницы,
# 6  удовлетворяющие
# 7        некоторым
# 8        критериям
# 9         качества
# 10                и
# 11  предназначенные
# 12             быть
# 13         образцом
# 14              для
# 15        написания
# 16           других
# 17          страниц
# 18        Википедии

