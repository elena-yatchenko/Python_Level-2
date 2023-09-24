# В Пайтон все - объект.
# Строгая динамическая типизация.
# Строгая типизация: тип объекта изменить невозможно
# Динамическая типизация: переменная может ссылаться на объекты разных типов и это не будет ошибкой в Пайтон

# a = 5 # <class 'int'>
# print(type(a))
# a = "Hello world" # <class 'str'>
# print(type(a))
# a = 42.8 * 96 / 2.47 # <class 'float'>
# print(type(a))
# объект - коробка на складе, а переменная - стикер, который говорит что лежит в коробке

# a = 5
# print(type(a), id(a))#class'int'> 140719759025064
# a = "Hello world"
# print(type(a), id(a)) # <class 'str'> 1445362371440
# a = 42.8 * 96 / 2.47
# print(type(a), id(a)) # <class 'float'> 1445361466512

# ISINSTANCE(object, classinfo) функция - когда хотим убедиться, является ли объект объектом нужного нам типа
# data = 42
# print(isinstance(data, int)) # True
#
# data = True
# print(isinstance(data, int)) # True (True == 1) В Пайтон логические типы True/False относятся к подклассу целых чисел
#
# data = 3.14
# print(isinstance(data, (int, float, complex))) # True
# # complex - комплексное число

# ОПЕРАТОР IS - сравнивает объекты по их идентичности, т.е. являются ли они одними и теми же объектами

# num = 2 + 2 * 2 # 6
# digit = 36 / 6 # 6.0
# print(num, digit)  # 6 6.0
# print(num == digit) # True т.к. сравниваются значения
# print(num is digit) # False т.к. в первом случае целочисленое 6, а во втором - вещественное 6 (6,0)



