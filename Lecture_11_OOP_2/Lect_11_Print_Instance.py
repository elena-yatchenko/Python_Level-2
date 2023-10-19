# ПРЕДСТАВЛЕНИZ ЭКЗЕМПЛЯРА (ЧТО ВЫВОДИТ PRINT)

# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name

#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
        
# user = User('Спенглер')
# print(user)  # <__main__.User object at 0x00000214FFF1EF10>

"""Для получения читаемого описания необходимо переопределить как
минимум один из дандер методов: __str__ или __repr__."""

# Представление для ПОЛЬЗОВАТЕЛЯ, __STR__

"""Дандер метод __str__ используется для получения удобного пользователю
описания экземпляр"""

# class User:
    
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
        
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
        
#     def __str__(self):
#         return f'Экземпляр класса User с именем "{self.name}"'
    
# user = User('Спенглер')
# print(user) # Экземпляр класса User с именем "Спенглер"

# Представление для СОЗДАНИЯ экземпляра, __REPR__

"""Дандер метод __repr__ аналогичен __str__, но возвращает максимально близкое к
созданию экземпляра класса представление. Если скопировать вывод метода repr и присвоить его переменной, должен
получится ещё один экземпляр класса"""

# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
        
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
        
#     def __repr__(self):
#         return f'User({self.name})'
    
# # user = User('Спенглер')
# # print(user)  # User(Спенглер)

# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
        
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
    
# user = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print(user) # User(Венкман, ['протонный ускоритель', 'ловушка'])

"""Мы снова получили строку, которую можно скопировать и создать экземпляр без
внесения правок(разве что ясно обозначить строкой имя через ''). 
При этом свойство life опущено в выводе, т.к. не влияет на создание экземпляра.
"""

# ПРИОРИТЕТ МЕТОДОВ

# class User:
#     ...
# user = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print(user)
# print(f'{user}')

# print(repr(user))
# print(f'{user = }')

"""Если у нас для класса прописан и метод __str__, и метод __repr__:
В первых двух вариантах сработает __str__, во последних двух вариантах - __repr__
"""

# ПЕЧАТЬ КОЛЛЕКЦИЙ

""" Однако метод __repr__ оказывается более приоритетным, если на печать выводится
не один элемент, а коллекция элементов.
"""

class User:
    
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3
        
    def __str__(self):
        eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
        return f'Перед нами {self.name} с {eq}. Количество жизней - {self.life}'
    
    def __repr__(self):
        return f'User({self.name}, {self.equipment})'
    
u_1 = User('Спенглер')
u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')
ghostbusters = [u_1, u_2, u_3]
print(ghostbusters)
# [User(Спенглер, []), User(Венкман, ['протонный ускоритель', 'ловушка']), User(Стэнц, ['ловушка', 'прибор ночного видения'])]

print(f'{ghostbusters}')
# [User(Спенглер, []), User(Венкман, ['протонный ускоритель', 'ловушка']), User(Стэнц, ['ловушка', 'прибор ночного видения'])]

print(repr(ghostbusters))
# [User(Спенглер, []), User(Венкман, ['протонный ускоритель', 'ловушка']), User(Стэнц, ['ловушка', 'прибор ночного видения'])]

print(f'{ghostbusters = }')
# ghostbusters = [User(Спенглер, []), User(Венкман, ['протонный ускоритель', 'ловушка']), User(Стэнц, ['ловушка', 'прибор ночного видения'])]

print(*ghostbusters, sep='\n')
# Перед нами Спенглер с пустыми руками. Количество жизней - 3
# Перед нами Венкман с оборудованием: протонный ускоритель, ловушка. Количество жизней - 3
# Перед нами Стэнц с оборудованием: ловушка, прибор ночного видения. Количество жизней - 3

"""В приведённом примере список из трёх экземпляров при печати возвращает repr
представление во всех четырёх рассмотренных способах. И только при распаковке
списка через звёздочку функция print получает экземпляры напрямую и вызывает
их дандер __str__"""



