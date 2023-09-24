# Часто встречающиеся слова

# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов.
# Пример

# На входе:

# text = 'Hello world. Hello Python. Hello again.'

# На выходе: 

# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]

import string

text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum "\
    "and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of " \
        "significant whitespace. Its language constructs and object-oriented approach aim to help programmers write "\
        "clear, logical code for small and large-scale projects."
text = text.split("'")
text = " ".join(text)
text = text.split("-")
text = " ".join(text)
text1 = (text.translate(str.maketrans("", "", string.punctuation))).lower().split()

for elem in text1:
    if elem.isdigit():
        text1.remove(elem)

# print(text.translate(str.maketrans("", "", string.punctuation)))
# print((text.translate(str.maketrans("", "", string.punctuation))).lower())
# print(text1)

# Hello world Hello Python Hello again
# hello world hello python hello again
# ['hello', 'world', 'hello', 'python', 'hello', 'again']


my_dict = {}

for word in text1:
    my_dict.setdefault(word, 0)
    my_dict[word] += 1

# print(my_dict)
# {'hello': 3, 'world': 1, 'python': 1, 'again': 1}

sorted_list = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
#print(sorted_list)
result_list = []
count = 0
for elem in sorted_list:
    if count < 10:
        result_list.append(elem)
        count += 1
    else:
        break
print(result_list)

# ИЛИ ЧЕРЕЗ СРЕЗ БЕРЕМ ПЕРВЫЕ 10 ЭЛЕМЕНТОВ!!!
sorted_list = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:10]
print(sorted_list)

# Для сортировки словаря сначала получаем список кортежей (key, val) методом словаря dict.items(). Далее сортирвока по ключу или значению
# key=lambda x: x[1] - ключ сортировки, который говорит сортировать пару "ключ-значение" по значению (в кортеже у значения индекс 1)
# key=lambda x: x[0] - ключ сортировки, который говорит сортировать пару "ключ-значение" по ключу (в кортеже у ключа индекс 0)

# >>> d = {'b': 9, 'a': 3, 'c': 7}
# # получаем итерацию кортежей `(key, val)`
# >>> d.items()
# # dict_items([('b', 9), ('a', 3), ('c', 7)]) # то что нужно
# # исходный словарь
# >>> d = {'b': 9, 'a': 3, 'c': 7}
# # собственно сама сортировка
# >>> sorted_tuple = sorted(d.items(), key=lambda x: x[0])
# # получили отсортированный список кортежей, 
# # отсортированных по первому значению
# >>> sorted_tuple
# # [('a', 3), ('b', 9), ('c', 7)]
# # преобразовываем обратно в словарь
# dict(sorted_tuple)
# # {'a': 3, 'b': 9, 'c': 7}
# >>> d = {'b': 9, 'a': 3, 'c': 7}
# >>> sorted_tuple = sorted(d.items(), key=lambda x: x[1])
# >>> sorted_tuple
# # [('a', 3), ('c', 7), ('b', 9)]
# # преобразовываем обратно в словарь
# >>> dict(sorted_tuple)
# # {'a': 3, 'c': 7, 'b': 9}

# РЕШЕНИЯ СИСТЕМЫ

# import re
# from collections import Counter

# # Удаляем знаки препинания и приводим текст к нижнему регистру
# cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# # Разбиваем текст на слова и считаем их количество
# words = cleaned_text.split()
# word_counts = {}

# for word in words:
#     if word not in word_counts:
#         word_counts[word] = 1
#     else:
#         word_counts[word] += 1

# # Получаем 10 самых часто встречающихся слов
# top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# print(top_words)