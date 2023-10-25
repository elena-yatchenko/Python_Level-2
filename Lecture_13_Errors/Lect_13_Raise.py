# КЛЮЧЕВОЕ СЛОВО RAISE

"""Команда поднимает исключение, указанное после неё. 
Используется для случаев, когда вы явно хотите сообщить о
неправильной работе вашего кода"""

"""Например у нас есть функция, которая запрещает изменять значение у
существующих ключей.
"""

# def add_key(dct, key, value):
#     if key in dct:
#         raise KeyError(f'Перезаписывание существующего ключа запрещено. {dct[key] = }')
#     dct[key] = value
#     return dct

# data = {'one': 1, 'two': 2}
# print(add_key(data, 'three', 3))
# # {'one': 1, 'two': 2, 'three': 3}

# print(add_key(data, 'three', 3))
# # KeyError: 'Перезаписывание существующего ключа запрещено. dct[key] = 3'

"""Первый раз мы смогли добавить пару ключ-значение в словарь. Но строкой ниже
получили ошибку. Ключ уже добавлен в словарь и изменить его нельзя. Поднимаем
исключение KeyError."""

# ПОДНИМАЕМ ИСКЛЮЧЕНИЯ В КЛАССАХ

"""Более сложный пример поднятия исключений — контроль создания класса.
Подобное было при создании дескрипторов. В нашем случае класс отслеживает
переданные аргументы в методе инициализации."""

class User:
    def __init__(self, name, age):
        if 6 <= len(name) < 30:
            self.name = name
        else:
            raise ValueError(f'Длина имени должна быть между 6 и 30 символами. {len(name) = }')
        if not isinstance(age, (int, float)):
            raise TypeError(f'Возраст должен быть числом. Используйте int или float. {type(age) = }')
        elif age < 0:
            raise ValueError(f'Возраст должен быть положительным. {age = }')
        else:
            self.age = age
            
# user = User('Яков', '-12')
# # ValueError: Длина имени должна быть между 6 и 30 символами. len(name) = 4

# user = User('Руслан', '-12')
# # TypeError: Возраст должен быть числом. Используйте int или float. type(age) = <class 'str'>

# user = User('Руслан', -12)
# # ValueError: Возраст должен быть положительным. age = -12

# user = User('Руслан', 12)
# print(user.name, user.age)
# # Руслан 12

"""Класс контролирует длину имени пользователя. Далее убеждаемся, что возраст —
число. И если верно, то проверяем больше ли нуля число."""

# TEST

def func(a, b, c):
    if a < b < c:
        raise ValueError('Не перемешано!')
    elif sum((a, b, c)) == 42:
        raise NameError('Это имя занято!')
    elif max(a, b, c, key=len) < 5:
        raise MemoryError('Слишком глуп!')
    else:
        raise RuntimeError('Что-то не так!!!')
    
# func(11, 7, 3) # 1
# TypeError: object of type 'int' has no len() - для целых чисел не можем определять длину

# func(3, 2, 3) # 2
# TypeError: object of type 'int' has no len()

# func(73, -40, 9) # 3
# NameError: Это имя занято!

# func(10, 20, 30) # 4
# ValueError: Не перемешано!
