# ТИПЫ ДАННЫХ (неизменяемые и изменяемые)
# a = 5
# print(a, id(a)) # 5 140719766758312
# a += 1
# print(a, id(a)) # 6 140719766758344

# txt = 'Hello world'
# txt[5] = "_" # 'str' object does not support item assignment (нельзя менять неизменяемый объект)

# txt = 'Hello world'
# print(txt, id(txt)) # Hello world 2400743033968
# txt = txt.replace(' ', '_') # заменяет, но при этом это уже другой объект, лежащий в другом месте оперативной памяти
# print(txt, id(txt)) # Hello_world 2400744471600

# a = c = 2
# b = 3
# print(a, id(a), b, id(b), c, id(c)) # тут а и с в одном и том же месте
# a = b + c
# print(a, id(a), b, id(b), c, id(c)) # а и с - уже в разных местах (ящиках на складе)

# 2 140719766758216 3 140719766758248 2 140719766758216
# 5 140719766758312 3 140719766758248 2 140719766758216

# !!! Для ИЗМЕНЯЕМЫХ ОБЪЕКТОВ изменение объекта, на который ссылается переменная а, автоматически приведет
# к изменению объекта, на который ссылается переменная с

# ХЭШ - проверка на неизменяемость (контрольная сумма)
# Хэш - это криптографическая фукнция хеширования, которую обычно называют просто хэшем.

# Хеш-функция - алгоритм, который может преобразовать произвольный массив данных в набор бит фиксированной длины

# Функция hash (object) - возвращает hash объекта в виде целого числа

# Если объект изменяемый - ХЭШ не вычисляется, если неизменяемый - можем вычислить хэш

# x = 42
# y = 'text'
# z = 3.415
# print(hash(x), hash(y), hash(z))
# # 42 -1388434390889119205 956924848823683075
# my_list = [x, y, z]
# print(hash(my_list))
# unhashable type: 'list'

# TEST
a = input()
print(type(a)) # <class 'str'>
print(id(a)) # 1986274674560
print(hash(a)) # -5164578921824827800








