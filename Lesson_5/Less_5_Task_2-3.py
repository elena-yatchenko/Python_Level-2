# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ - буква,
# а значение - код буквы. Напишите преобразование в одну строку.

text = 'Самостоятельно сохраните в переменной строку'

dict_comp = {i: ord(i) for i in text}
print(dict_comp)

# Продолжаем развивать задачу 2.
# Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

iter_dict = iter(dict_comp.items())
for _ in range(5):
    print(next(iter_dict))
    