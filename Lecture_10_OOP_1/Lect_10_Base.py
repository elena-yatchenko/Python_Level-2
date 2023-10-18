"""
В Питон все объект. Объекты строятся на основании классов. Объекты так же называют 
экземплярами класса. 
Например, выполняя следующий код, мы создаем экземпляр класса list, обратившись к классу list
Т.е. привычные нам функции для создания базовых объектов Питон на самом деле являются классами: 
list, tuple, int, str и т.д.
"""

# data = list((1, 2, 3))
# print(data, type(data), type(list))

# # [1, 2, 3] <class 'list'> <class 'type'>

# class Person:
#     max_up = 3
    
# """для создания экземпляра класса нужно выполнить операцию присваивания, вызвав класс"""

# p1 = Person() # экзпемпляр класса Person
# # print(p1.max_up) # 3
# # print(Person.max_up) # 3

# p2 = Person()
# print(Person.max_up, p1.max_up, p2.max_up)
# # 3 3 3 - экзмепляры "не видят" у себя max_up и берут значение у класса

# p1.max_up = 12
# print(Person.max_up, p1.max_up, p2.max_up)
# # 3 12 3 - экземпляр р1 уже имеет свое значение, оно приоритетнее, чем общее значение класса

# Person.max_up = 42
# print(Person.max_up, p1.max_up, p2.max_up)
# # 42 12 42

# ДИНАМИЧЕСКАЯ СТРУКТУРА КЛАССА
"""мы можем создавать новые атрибуты класса и экземпляров прямо в коде, вне класса"""

# class Person:
#     max_up = 3
    
# p1 = Person()
# p2 = Person()


# Person.level = 1
# print(Person.level, p1.level, p2.level)
# # 1 1 1  - атрибут, добавленный для класса распространяется и на экземпляры

# p1.health = 100
# # print(Person.health, p1.health, p2.health)
# # # AttributeError - атрибут, добавленный для конкретного экземпляра, действует только для 
# # # этого экземпляра. Ни класс, ни экземпляр р2 не могут получить к нему доступ

# print(p1.health) # 100

"""
Возможность динамически и изменять класс может быть использована как аналог работы со словарями dict.
"""

# p1 = Person()
# p1.level = 1
# p1.health = 100

# dict_p1 = {}
# dict_p1['level'] = 1
# dict_p1['health'] = 100

# print(p1.health) # 100
# print({dict_p1['health']}) # {100}

# КОНСТРУКТОР ЭКЗЕМПЛЯРА

""" При создании класса обычно используют конструктор __init__. Два символа подчёркивания до и после
имени говорят о том, что это “магическое имя”. Подобные имена нужны для
добавления новых возможностей в работе класса и его экземпляров.
Внутри функции заданы две переменные level и health. Это атрибуты экземпляров.
Любой экземпляр получает заранее присвоенные значения. При этом сам класс не
имеет доступа к заданным атрибутам."""

# class Person:
#     max_up = 3
    
#     def __init__(self):
#         self.level = 1
#         self.health = 100
        
# p1 = Person()
# p2 = Person()
# print(p1.max_up, p1.level, p1.health) # 3 1 100
# print(p2.max_up, p2.level, p2.health) # 3 1 100

# # print(Person.max_up, Person.level, Person.health)
# # # AttributeError: type object 'Person' has no attribute 'level'. Аналогично как класс 
# # #Person не имеет и атрибута health

# Person.level = 100 # ввели и задали атрибут level для класса
# print(Person.level, p1.level, p2.level) 
# # 100 1 1. Т.е. для класса 100, а у атрибутов задано более приоритетное значение - 1

# ● Параметр SELF

""" Ещё раз посмотрим на код конструктора:
def __init__(self):
self.level = 1
self.health = 100
В качестве параметра указана переменная self. Далее мы не просто присваиваем
значения переменным, а указываем self с точечной нотацией. В работе с классами
self является указателем на тот экземпляр класса, к которому происходит
обращение. Например для p1 это p1.level = 1. Какое бы имя вы не дали экземпляру,
self подставляет его на своё место. """

# ● Передача аргументов в экземпляр
"""При создании экземпляра можно передать значения в конструктор и тем самым
добавить свойства, характерные для конкретного экземпляра."""

# class Person:
#     max_up = 3
    
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
        
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.name = }, {p1.race = }')
# print(f'{p2.name = }, {p2.race = }')
# print(f'{p3.name = }, {p3.race = }')

# # p1.name = 'Сильвана', p1.race = 'Эльф'
# # p2.name = 'Иван', p2.race = 'Человек'
# # p3.name = 'Грогу', p3.race = 'unknown'

# МЕТОДЫ КЛАССА

"""
Функция внутри класса называется методом.
Можно создавать любые методы внутри класса и обращаться к ним из экземпляра
через точечную нотацию. Различие между обращением к свойству и к методу -
круглые скобки после имени.
"""

# class Person:
#     max_up = 3
    
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#     def level_up(self):
#         self.level += 1
        
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.level = }, {p2.level = }, {p3.level = }')
# # p1.level = 1, p2.level = 1, p3.level = 1

# p3.level_up()
# p1.level_up()
# p3.level_up()
# print(f'{p1.level = }, {p2.level = }, {p3.level = }')
# # p1.level = 2, p2.level = 1, p3.level = 3

""" При желании можно передавать в метод аргументы. 
И так как в Python всё объект, можно передать даже экземпляр класса.
"""

# class Person:
#     max_up = 3
    
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100

#     def change_health(self, other, quantity):
#             self.health += quantity
#             other.health -= quantity
            
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')
# # p1.health = 100, p2.health = 100, p3.health = 100

# p1.change_health(p2, 10)
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')
# # p1.health = 110, p2.health = 90, p3.health = 100

"""
Чаще всего для указания на другой экземпляр того же класса
используют параметр other в имени метода. Соответственно записи other.name
аналогичны self.name, но изменяют другой, переданный экземпляр класса.
"""

# TEST

""" Перед вами несколько строк кода. Напишите что выведет программа, не запуская
код. У вас 3 минуты."""

class User:
    count = []
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
u1 = User('One', '123-45-67')
u2 = User('NoOne', '76-54-321')
u1.count.append(42)
u1.count.append(73)
u2.counter = 256
u2.count.append(u2.counter)
u2.count.append(u1.count[-1])

"""
u1 и u2 добавляют элементы в один и тот же список, т.к. он один для класса. 
Т.о. u1.count[-1] берет -1-й элемент с конца списка [42, 73, 256], который 
до того момента был создан хранился в классе
"""

print(f'{u1.name = }, {u1.phone = }, {u1.count = }')
# u1.name = 'One', u1.phone = '123-45-67', u1.count = [42, 73, 256, 256]

print(f'{u2.name = }, {u2.phone = }, {u2.count = }')
# u2.name = 'NoOne', u2.phone = '76-54-321', u2.count = [42, 73, 256, 256]

print(User.count)
# [42, 73, 256, 256]

