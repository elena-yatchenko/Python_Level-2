# СРАВНЕНИЕ ЭКЗЕМПЛЯРОВ КЛАССА

"""Числа сравниваются по значению, строки посимвольно. Но при желании можно
сравнивать любые объекты Python реализовав перечисленные ниже дандер
методы - МЕТОДЫ РАСШИРЕННОГО СРАВНЕНИЯ."""

# object.__lt__(self, other),
# object.__le__(self, other),
# object.__eq__(self, other),
# object.__ne__(self, other),
# object.__gt__(self, other),
# object.__ge__(self, other):

"""Соответствие между символами операторов и именами методов следующее:

x < y: вызывает x.__lt__(y),
x <= y: вызывает x.__le__(y),
x == y вызывает x.__eq__(y),
x != y вызывает x.__ne__(y),
x > y вызывает x.__gt__(y),
x >= y вызывает x.__ge__(y)."""

"""пары методов
__lt__() И __gt__(),
__le__() И __ge__(), 
__eq__() И __ne__() 
являются взаимным отражением друг друга. 
Т.е. добавив в класс метод __eq__(), можем проводить как операции а == в,
так и а != в для экземпляров класса. Реализовав один из пары, второй Python попытается
получить инвертируя значение: Не истина — это ложь, а не ложь — это истина"""

"""При реализации метода обычно принято возвращать True или False. Если
возвращается другое значение в конструкциях вида if x == y:, Python применит
функцию bool() к результату для получения True или False.
Например, если возвращаем число, будет True (т.к. любой число, кроме 0 - True)
если пустой список - False, и т.п."""

# СРАВНЕНИЕ НА ИДЕНТИЧНОСТЬ, __EQ__

"""Создадим класс треугольник, который хранит длины трёх сторон. В первом
варианте не будем прописывать дандер __eq__ и попробуем сравнить экземпляры.
"""

# class Triangle:
    
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
        
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
    
# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# print(one == two) # True
# print(one == three) # False

"""Переменные one и two равны, т.к. ссылаются на один и тот же объект в памяти.
Дело в том, что Python по умолчанию добавляет метод __eq__ следующего
вида.
        def __eq__(self, other):
            return self is other
            
Как вы помните is сравнивает адреса объектов в памяти. Следовательно проверка
по умолчанию это: True if id(self) == id(other) else False.
"""
 
"""А теперь напишем свою проверку на идентичность. Допустим возможность
переворачивания треугольника перед сравнением. Например треугольники со
сторонами 3, 4, 5 и 4, 3, 5 будем считать равными."""

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
        
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b},{self.c}'
    
#     def __eq__(self, other):
#         first = sorted((self.a, self.b, self.c))
#         second = sorted((other.a, other.b, other.c))
#         return first == second
    
# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# four = Triangle(4, 3, 5)
# print(f'{one == two = }')
# # one == two = True

# print(f'{one == three = }')
# # one == three = True

# print(f'{one == four = }')
# # one == four = True

# print(f'{one != one = }')
# # one != one = False

"""Функция sorted получает кортеж из трёх сторон и возвращает их в упорядоченном
виде. Сравнив оба списка поэлементно определяем равны треугольники или нет.
Обратите внимание на последнюю строку. Проверка на неравенство не вызвала
ошибку. Python вызвал дандер __eq__, а к результату применил команду not."""

# СРАВНЕНИЕ НА БОЛЬШЕ ИЛИ МЕНЬШЕ

# from math import sqrt
# class Triangle:
    
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
        
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
    
#     def __repr__(self):
#         return f'Triangle({self.a}, {self.b}, {self.c})'
    
#     # def __eq__(self, other):
#     #     first = sorted((self.a, self.b, self.c))
#     #     second = sorted((other.a, other.b, other.c))
#     #     return first == second
    
#     def area(self):
#         p = (self.a + self.b + self.c) / 2
#         _area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#         return _area
    
#     def __lt__(self, other):
#         return self.area() < other.area()
    
# one = Triangle(3, 4, 5)
# two = Triangle(5, 5, 5)
# print(f'{one} имеет площадь {one.area():.3f} у.е.²')
# print(f'{two} имеет площадь {two.area():.3f} у.е.²')
# # Треугольник со сторонами: 3, 4, 5 имеет площадь 6.000 у.е.²
# # Треугольник со сторонами: 5, 5, 5 имеет площадь 10.825 у.е.²

# print(f'{one > two = }\n{one < two = }')
# # one > two = False
# # one < two = True

# data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4),
# Triangle(3, 5, 3)]
# result = sorted(data)
# print(result)
# # [Triangle(3, 5, 3), Triangle(6, 2, 5), Triangle(3, 4, 5), Triangle(4, 4, 4)]

# print(', '.join(f'{item.area():.3f}' for item in result))
# # 4.146, 4.684, 6.000, 6.928

"""● дандер __lt__ вызывает для каждого из сравниваемых экземпляров метод
area и возвращает результат сравнения площадей: True или False.
В основном коде создали пару треугольников, посмотрели на их площадь и
убедились, что сравнения на больше так же работает и возвращает обратное от
сравнения на меньше.
Далее создали список треугольников и отсортировали их. Визуальная проверка
площадей подтверждает, что треугольники были упорядочены именно на основе их
сравнения (т.е. сравнения площадей, как и прописано в методе __lt__).
"""

# НЕИЗМЕНЯЕМЫЕ ЭКЗЕМПЛЯРЫ, ХЕШИРОВАНИЕ. ДАНДЕР __HASH__

"""Как вы помните ключом dict и элементами set и frozenset могут быть только
неизменяемые типы данных. А для проверки на неизменяемость используется
функция hash(). Она должна возвращать целое число в 4 или 8 байт в зависимости
от разрядности интерпретатора Python. И это число должно быть неизменным на
всём протяжении работы программы.
Попробуем сложить наши треугольники из примера выше в множество не изменяя
код"""

# from math import sqrt

# triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4,
# 4, 4), Triangle(3, 5, 3)}
# print(triangle_set)  # TypeError: unhashable type: 'Triangle'

"""попробуем закомментировать метод проверки на равенство def __eq__(self, other) и
и запустить код снова."""

# print(triangle_set)
# # {Triangle(3, 5, 3), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 4, 5)}
# print(', '.join(f'{hash(item)}' for item in triangle_set))
# # 160341654757, 160341654753, 160341654761, 160341654749

"""Экземпляры треугольника стали хэшируемыми. 

Правило следующее.
● нет __eq__, нет __hash__ - неизменяемый объект. Python сам реализует оба
дандера
● есть __eq__, нет __hash__ - изменяемый объект. Python устанавливает
__hash__ = None
● есть __eq__, есть __hash__ - неизменяемый объект реализованный
разработчиком
● нет __eq__, есть __hash__ - запрещённая комбинация! Разработчик допустил
ошибку
Если вы хотите явно отключить поддержку хэширования, в определение класса
добавляется строка __hash__ = None
        class Triangle:
            __hash__ = None
            ....
"""

# ПРОСТЕЙШАЯ РЕАЛИЗАЦИЯ ХЭША

"""При желании реализовать собственный метод __hash__ рекомендуется сделать все
свойства класса неизменяемыми. Внутри дандер метода возвращается результат
работы функции hash(). На вход функция получает кортеж из всех свойств класса"""

# from math import sqrt

# class Triangle:
    
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
        
#     def __str__(self):
#         return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'
    
#     def __repr__(self):
#         return f'Triangle({self._a}, {self._b}, {self._c})'
    
#     def __eq__(self, other):
#         first = sorted((self._a, self._b, self._c))
#         second = sorted((other._a, other._b, other._c))
#         return first == second
    
#     def area(self):
#         p = (self._a + self._b + self._c) / 2
#         _area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
#         return _area
    
#     def __lt__(self, other):
#         return self.area() < other.area()
    
#     def __hash__(self):
#         return hash((self._a, self._b, self._c))
    
# triangle_set = {Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4,
# 4, 4), Triangle(3, 5, 3)}
# print(triangle_set)
# print(', '.join(f'{hash(item)}' for item in triangle_set))

# {Triangle(4, 4, 4), Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(3, 5, 3)}
# 5958266269407395088, 4003026094496801395, 7248620568795758028, -7050955881463073020

"""Свойства класса получили символ подчёркивания в начале имени. Сообщаем
коллегам по коду, что они защищённые и не должны изменяться.
"""

# TEST

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + b
        
    def __str__(self):
        return f'MyClass(a={self.a}, b={self.b}, c={self.c})'
    
    def __eq__(self, other):
        return (sum((self.a, self.b)) - self.c) == (sum((other.a, other.b)) - other.c)

x = MyClass(42, 2)
y = MyClass(73, 3)
print(x == y)  # True

