# DOCTEST
"""Инструмент doctest встроен в Python и не требует дополнительных манипуляций по
установке и настройке"""

"""Проверка примеров в документации, регрессионное тестирование"""

"""простейшая (без оптимизации) функция, проверяющая является ли число простым
или составным используя нахождение остатка от деления.
"""
# def is_prime(p: int) -> bool:
#     """
#     Checks the number P for simplicity using finding the remainder of the 
#     division in the range [2, P).
#     """
#     for i in range(2, p):
#         if p % i == 0:
#             return False
#     return True


# if __name__ == '__main__':
#     help(is_prime)

"""
>>> from main import is_prime

>>> is_prime(42)
False
>>> is_prime(73)
True
>>>

Вызов функции в режиме интерпретатора позволяет получить ответ для любых значений."""

"""Если перенести вызову и результаты из консоли в строку документации функции
(класса, модуля), получим тесты doctest. В нашем случае можно сделать так:
"""

def is_prime(p: int) -> bool:

    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

"""В документацию добавлены строки вызова функции в режиме интерпретатора. Они
начинаются с тройной стрелки и пробела. Сразу после идёт строка с ответом.
В “нейм-мейн” спрятали импорт модуля doctest и вызов функции testmod для
тестирования кода.
"""
"""!!! Важно! doctest запускает код и сравнивает возвращаемое значение в
виде текста с текстов внутри строки документации. Если допустить опечатку,
поставить лишние отступы или ещё как-то изменить текст ответа, тест будет
провален."""

"""При запуске файла ничего не происходит. По умолчанию тестирование не выводит
информации, если тесты прошли успешно. Попросим добавить вывод результатов в
любом случае. Для этого исправим последнюю строку на
doctest.testmod(verbose=True)
Теперь перед нами подробный вывод того, что тесты пройдены успешно."""

# Получаем следующий вывод
# Trying:
#     is_prime(42)
# Expecting:
#     False
# ok
# Trying:
#     is_prime(73)
# Expecting:
#     True
# ok
# 1 items had no tests:
#     __main__
# 1 items passed all tests:
#    2 tests in __main__.is_prime
# 2 tests in 2 items.
# 2 passed and 0 failed.
# Test passed.
