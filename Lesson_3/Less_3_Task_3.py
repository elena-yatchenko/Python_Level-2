# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков,
# где ключ - тип элемента,
# а значение - список элементов данного типа.

my_tuple = (123, 2.5, 32, 3.5, 'game', True, 'computer',)

my_dict = {}

for elem in my_tuple:
    count = my_dict.setdefault(type(elem), [])
    count.append(elem)
print(count)

??????

my_tuple = (123, 2.5, 32, 3.5, 'game', True, 'computer',)

my_dict = {}

for i in my_tuple:
    count = my_dict.setdefault(type(i), [])
    count.append(i)

print(my_dict)

