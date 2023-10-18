# ИНКАПСУЛЯЦИЯ

"""В ряде языков программирования под инкапсуляцией понимается сокрытие части
свойств и методов класса от доступа извне класса"""

# ОДНО ПОДЧЕРКИВАНИЕ в начале - ЗАЩИЩЕННАЯ ПЕРЕМЕННАЯ/МЕТОД

# class Person:
#     max_up = 3
#     _max_level = 80
    
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
        
#     def _check_level(self):
#         return self.level < self._max_level
    
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
            
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
        
# p1 = Person('Сильвана', 'Эльф', 120)
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу', speed=60)
# print(f'{p1._max_level = }')  # p1._max_level = 80
# print(f'{p2._speed = }')  # p2._speed = 100
# p2._speed = 150
# print(f'{p2._speed = }') # p2._speed = 150
# p3.level_up()
# print(f'{p3.level = }') # p3.level = 2
# p3.level = 80
# p3.level_up() # p3.level = 80
# print(f'{p3.level = }')

"""
Переменная уровня класса _max_level и переменная уровня экземпляра _speed
говорят другим разработчикам, что они защищены. Так мы просим их не
использовать. Однако мы сможем обратиться к ним через точечную нотацию.

Аналогично метод _check_level говорит о том, что он защищён. Метод нужен классу
для проверки достижения максимального уровня персонажа и не должен
использоваться напрямую вне класса. А вот его вызов из метода level_up считается
нормальным поведением.
"""

# ДВА ПОДЧЕРКИВАНИЯ в начале - ПРИВАТНАЯ ПЕРЕМЕННАЯ/МЕТОД

"""Переменная с двумя подчёркиваниями в начале не может иметь
более одного подчёркивания в конце имени. Двойное подчёркивание до и
после имени — магическая переменная Python. Подобно __init__ такие имена
зарезервированы для особых действий."""

# class Person:
#     __max_up = 3
#     _max_level = 80
    
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#         self.up = 3
        
#     def _check_level(self):
#         return self.level < self._max_level
    
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
            
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity

#     def add_up(self):
#         self.up += 1
#         self.up = min(self.up, self.__max_up)
        
# p1 = Person('Сильвана', 'Эльф', 120)
# # print(f'{p1.up = }')  # p1.up = 3
# p1.up = 1
# # print(f'{p1.up = }')  # p1.up = 1
# for _ in range(5):
#     p1.add_up()
#     print(f'{p1.up = }')  
    
# # p1.up = 2
# # p1.up = 3
# # p1.up = 3
# # p1.up = 3
# # p1.up = 3  - так не не может быть больше self.__max_up

# print(p1.__max_up) # AttributeError: 'Person' object has no attribute '__max_up'
# print(Person.__max_up) # AttributeError: type object 'Person' has no attribute '__max_up'

"""Переменная __max_up доступна внутри класса и его экземпляров. Мы используем
её для увеличения количества жизней персонажа в методе add_up. Никаких
проблем с доступом нет.
Когда же пытаемся обратиться к свойству напрямую, получаем ошибку доступа к
атрибуту. Аналогичные ошибки будут и при обращении к методу, начинающемуся с
двух подчёркиваний."""

# ДОСТУП К ПРИВАТНЫМ ПЕРЕМЕННЫМ

"""
Приватная переменная __max_up не исчезает за пределами класса. Срабатывает
механизм модификации имени. В общем случае он превращает переменную
__name в переменныю _classname__name. НО лучше это не использовать.
Если приходится обращаться к приватной переменной, значит может она не должна 
быть приватной?
"""

# class Person:
#     __max_up = 3
#     ...
# p1 = Person()
# print(p1._Person__max_up) # 3

# TEST
"""Перед вами несколько строк кода. Какие ошибки и недочёты есть в коде. У вас 3
минуты.
"""
# class User:
#     def __init__(self, name, phone, password):
#         self.__name__ = name
#         self._phone = phone
#         self.__password = password
        
# u1 = User('One', '123-45-67', 'qwerty')
# print(f'{u1.__name__ = }, {u1._phone = }, {u1._User__password = }')

"""некорректно использовать __name__в2-х местах, обращаться к _User__password"""

