# СТРОКА ДОКУМЕНТАЦИИ

"""Как и при создании функции, при создании классов принято оставлять
документацию к нему. Для этого достаточно использовать многострочный
комментарий СРАЗУ ПОСЛЕ определения класса (если сделаем через пустую строку, 
то будет восприниматься уже как обычный комментарий. И команды чтения документации
не будут видеть ее)"""

# ВЫЗОВ ЧЕРЕЗ ФУНКЦИЮ HELP()

class User:
    """A User training class for demonstrating class documentation.
    Shows the operation of the help(cls) and the dander method __doc__"""
    
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name
        
    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()
        
# u_1 = User('Спенглер')
# print('Справка класса User ниже', '*' * 50)
# help(User)
# print('Справка экземпляра u_1 ниже', '*' * 50)
# help(u_1)

# # Help on class User in module __main__:

# # class User(builtins.object)
# #  |  User(name: str)
# #  |
# #  |  A User training class for demonstrating class documentation.
# #  |  Shows the operation of the help(cls) and the dander method __doc__      
# #  |
# #  |  Methods defined here:
# #  |
# #  |  __init__(self, name: str)
# #  |      Added the name parameter.   и т.д.

# ВЫЗОВ ДОКУМЕНТАЦИИ ЧЕРЕЗ ДАНДЕР МЕТОД __DOC__

"""Любая многострочная строка после заголовка класса и метода автоматичские
сохраняется в дандер переменную __doc__.  Помимо вызова справки через
функцию help можно прочитать отдельный мнострочник напрямую обратившись к
переменной."""

u_1 = User('Спенглер')
print(f'Документация класса: {User.__doc__ = }')
print(f'Документация экземпляра: {u_1.__doc__ = }')
print(f'Документация метода: {u_1.simple_method.__doc__}')

# Документация класса: User.__doc__ = 'A User training class for demonstrating class documentation.\n    Shows the operation of the help(cls) and the dander method __doc__'
# Документация экземпляра: u_1.__doc__ = 'A User training class for demonstrating class documentation.\n    Shows the operation of the help(cls) and the dander method __doc__'
# Документация метода: Example of a simple method.

# TEST

class MyClass:
    A = 42
    """About class"""

    def __init__(self, a, b):
        """self.__doc__ = None"""
        self.a = a
        self.b = b
        
    def method(self):
        """Documentation"""
        self.__doc__ = None
        
help(MyClass)

Help on class MyClass in module __main__:

# class MyClass(builtins.object)
#  |  MyClass(a, b)
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, a, b)
#  |      self.__doc__ = None
#  |
#  |  method(self)
#  |      Documentation
