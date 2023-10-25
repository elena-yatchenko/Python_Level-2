# СОЗДАНИЕ СОБСТВЕННЫХ ИСКЛЮЧЕНИЙ

"""Попробуем для класса User из прошлого примера создать свои исключения.
Писать код исключений будем в отдельном файле error.py """

"""Теперь внесём правки в код инициализации пользователя. Заодно избавимся от
магических чисел для минимальной и максимальной длины имени."""

from error import UserNameError, UserAgeError

# class User:
#     MIN_LEN = 6
#     MAX_LEN = 30

#     def __init__(self, name, age):
#         if self.MIN_LEN <= len(name) < self.MAX_LEN:
#             self.name = name
#         else:
#             raise UserNameError
#         if not isinstance(age, (int, float)) or age < 0:
#             raise UserAgeError
#         else:
#             self.age = age

# user = User('Яков', '-12')

# # error.UserNameError

"""Подобный код отлично справляется с поставленной задачей. Но стал менее
информативен в случае возникновения ошибок.

Подобный код отлично справляется с поставленной задачей. Но стал менее
информативен в случае возникновения ошибок.
"""

# МЕТОДЫ __INIT__ И __STR__ В КЛАССАХ ИСКЛЮЧЕНИЙ

"""Чтобы исключение давало подробную информацию об ошибке, будем передавать
ему проблемную переменную. Класс User доработаем в строках подъёма ошибок"""

# from error import UserNameError, UserAgeError

# class User:
#     def __init__(self, name, age):
#         if 6 < len(name) < 30:
#             self.name = name
#         else:
#             raise UserNameError(name)
#         if not isinstance(age, (int, float)) or age < 0:
#             raise UserAgeError(age)
#         else:
#             self.age = age
            
# user = User('Яков', '-12')
# # raise UserNameError(name)
# # error.UserNameError: Яков

"""Благодаря наследованию переданные в исключение переменные могут выводится
в тексте ошибки.

Уже лучше. Но без пары дандер методов в классах ошибок пока не идеально.
Дорабатываем код в файле error.
"""

"""В классе User надо исправит строку вызова ошибки имени,
чтобы код сработал верно. Иначе исключение вернёт нам 
TypeError: UserNameError.__init__() missing 2 required positional arguments:
'lower' and 'upper'"""

class User:
    MIN_LEN = 6
    MAX_LEN = 30
    
    def __init__(self, name, age):
        if self.MIN_LEN <= len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError((age))
        else:
            self.age = age
            
# user = User('Яков', '-12')

# error.UserNameError: Имя пользователя Яков содержит 4 символа(ов).     
# Это меньше нижней границы. Попадите в диапазон (6, 30).

user = User('Руслан', '-12')

# error.UserAgeError: Возраст пользователя должен быть целым int() или вещественным float() больше нуля.
# У вас тип <class 'str'>, а значение -12