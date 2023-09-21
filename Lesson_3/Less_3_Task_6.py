# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так,
# чтобы у самого длинного слова был один пробел между ним и номером строки

сразу выведем введенную пользователем строку в список

lst = sorted(input().split())

print(lst)

# max_word = (max(lst, key=len)) - нашли максимальное слово

max_word = len(max(lst, key=len)) # нашли длину максимального слова

for idx, elem in enumerate(lst, 1)
    print(f'{idx} {elem:>{count}}')
    


lst = sorted(input().split()) 
count = len(max(lst, key=len)) 
for k, v in enumerate(lst, 1): 
    print(f'{k} {v:>{count}}')