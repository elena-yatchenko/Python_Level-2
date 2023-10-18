# НАСЛЕДОВАНИЕ

"""
В Python все объекты являются наследниками класса object.
Т.е. фактически задание класса Person выглядит так:

class Person(object):
    pass

НО: Наследование от object принято опускать при создании класса, поэтому:

class Person:
    pass
"""

class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity
        
    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)

# class Hero(Person):
#     def __init__(self, power, *args, **kwargs):
#         self.power = power
#         super().__init__(*args, **kwargs)
        
# p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
# print(f'{p1.name = }, {p1.up = }, {p1.power = }')
        
# # p1.name = 'Сильвана', p1.up = 3, p1.power = 'archery'

"""Герой - дочерний класс для
персонажа. Мы хотим добавить герою свойство power и прописываем его в методе
инициализации. Далее вызываем метод super().__init__, т.е. метод инициализации
родительского класса. Без такого вызова не будут созданы атрибуты родительского
класса.
Теперь при создании экземпляра класса Hero мы вначале передаём его аргументы,
а далее аргументы родительского класса Person."""  

# ПЕРЕОПРЕДЕЛЕНИЕ МЕТОДОВ

"""При наследовании мы можем использовать в дочернем классе все общедоступные
свойства и методы родительского класса. Кроме того можно создать свои. И если
имена будут совпадать, произойдёт переопределение. Будут браться значения
дочернего класса."""  

"""Класс Person и его методы созданы чуть выше"""    

# class Hero(Person):
#     def __init__(self, power, *args, **kwargs):
#         self.power = power
#         super().__init__(*args, **kwargs)

#     def change_health(self, other, quantity):
#         self.health += quantity * 2
#         other.health -= quantity * 2

#     def add_many_up(self):
#         self.up += 1
#         self.up = min(self.up, self._Person__max_up * 2)
        
# p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
# p2 = Person('Маг', 'Тролль')
# print(f'{p1.health = }, {p2.health = }') # p1.health = 100, p2.health = 100
# p1.change_health(p2, 10)
# print(f'{p1.health = }, {p2.health = }') # p1.health = 120, p2.health = 80
# p2.change_health(p1, 10)
# print(f'{p1.health = }, {p2.health = }') # p1.health = 110, p2.health = 90
# p1.add_many_up()
# print(f'{p1.up = }') # p1.up = 4

"""В примере создан метод change_health с дополнительным множителем. Он
срабатывает у героя. Но при вызове метода у экземпляра класса Person
срабатывает старый метод.

В методе add_many_ups для обхода инкапсуляции используем запись
self._Person__max_up. Экземпляр обращается к приватному атрибуту родительского
класса, напрямую указав его."""

# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ

class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level
    
    def level_up(self):
        if self._check_level():
            self.level += 1
            
    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity
        
    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)
        
class Address:
    
    def __init__(self, country, city, street):
        self.country = country or ''
        self.city = city or ''
        self.street = street or ''
        
    def say_address(self):
        return f'Адрес героя: {self.country}, {self.city}, {self.street}'

class Weapon:
    
    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand or 'Клинок'
        self.right_hand = right_hand or 'Лук'
        
class Hero(Person, Address, Weapon):
    
    def __init__(self, power, name=None, race=None, speed=None, 
        country=None, city=None, street=None, left_hand=None, right_hand=None):
        self.power = power
        Person.__init__(self, name, race, speed)
        Address.__init__(self, country, city, street)
        Weapon.__init__(self, left_hand, right_hand)
    
    
    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2
        
    def add_many_ups(self):
        self.up += 1
        self.up = min(self.up, self._Person__max_up * 2)
        
p1 = Hero('archery', 'Сильвана', 'Эльф', 120,
country='Эльфляндия', street='Ночного эльфа',
left_hand='Стрела')
print(f'{p1.say_address()}') 
# Адрес героя: Эльфляндия, , Ночного эльфа

print(f'{p1.right_hand = }, {p1.left_hand = }')
# p1.right_hand = 'Лук', p1.left_hand = 'Стрела'

"""Мы создали классы Address и Weapon. Добавив их к нашему герою, получаем
сочетание атрибутов и методов всех перечисленных классов. Обратите внимание на
то как происходит инициализация родительских классов внутри Hero __init__.
Прописали все параметры из родительских классов в инициализации класса Hero.
Далее вручную распределяем аргументы между методами __init__ каждого из
родительских классов."""

# MRO

"""MRO - method resolution order переводится как “порядок разрешения
методов”"""

# class A:
#     def __init__(self):
#         print('Init class A')
#         self.data_a = 'A'
        
# class B:
#     def __init__(self):
#         print('Init class B')
#         self.data_b = 'B'
        
# class C:
#     def __init__(self):
#         print('Init class C')
#         self.data_c = 'C'
        
# class D:
#     def __init__(self):
#         print('Init class D')
#         self.data_d = 'D'
        
# class X1(A, C):
#     def __init__(self):
#         print('Init class X1')
#         super().__init__()
        
# class X2(B, D):
#     def __init__(self):
#         print('Init class X2')
#         super().__init__()
        
# class X3(A, D):
#     def __init__(self):
#         print('Init class X3')
#         super().__init__()
        
# class Z(X1, X2, X3):
#     def __init__(self):
#         print('Init class Z')
#         super().__init__()
        
# print(*Z.mro(), sep='\n')

# # <class '__main__.Z'>
# # <class '__main__.X1'>
# # <class '__main__.X2'>
# # <class '__main__.B'>
# # <class '__main__.X3'>
# # <class '__main__.A'>
# # <class '__main__.C'>
# # <class '__main__.D'>
# # <class 'object'>

"""У каждого класса есть метод mro, который вычисляет порядок наследования. Он
отвечает за инициализацию каждого класса один раз в порядке слева направо и по
старшинству, т.е. родитель не может быть инициализирован раньше дочернего
класа.
Поиск аргументов и методов в экземпляре класса Z будет происходить в порядке,
представленном методом mro.
!!! Не стоит из родительских классов обращаться к аргументам и
методам дочерних классов или классов того же уровня наследования."""

# Смотреть доп, ничего не понятно по MRO

# TEST

class A:
    name = 'A'
    
    def call(self):
        print(f'I am {self.name}')

class B:
    name = 'B'

    def call(self):
        print(f'I am {self.name}')

class C:
    name = 'C'

    def call(self):
        print(f'I am {self.name}')

class D(C, A):
    pass

class E(D, B):
    pass

e = E()
e.call() # I am C

