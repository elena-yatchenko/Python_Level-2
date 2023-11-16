#  Разработка через тестирование, TDD

"""Разработка через тестирование (англ. test-driven development, TDD) — техника
разработки программного обеспечения, которая основывается на повторении очень
коротких циклов разработки: сначала пишется тест, покрывающий желаемое
7
изменение, затем пишется код, который позволит пройти тест, и под конец
проводится рефакторинг нового кода к соответствующим стандартам.
В TDD выделяют следующие этапы:
1. Добавление теста
2. Запуск всех тестов: убедиться, что новые тесты не проходят
3. Написать код
4. Запуск всех тестов: убедиться, что все тесты проходят
5. Рефакторинг
6. Повторить цикл
"""

# добавление теста

"""Попробуем добавить в нашу функцию тесты для проверки особых случаев, а
именно:
● Число должно быть натуральным.
○ Если функция вызывается не с целым, будем возвращать ошибку типа.
○ А если число будет целым, но не натуральным, ошибку значения.
● Отдельно напишем тест для единицы - натурального целого числа, которое не
может быть проверено на простоту.
● Предусмотреть предупреждение о возможно долгом поиске ответа, если на
простоту проверяется число больше ста миллионов.
○ Сделаем тест для большого составного числа
○ Отдельно сделаем тест для большого простого числа
"""
def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time.
    Working...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time.
    Working...
    True
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()

"""!!! Обратите внимание на многоточия в тестах ошибок. Модуль doctest ориентируется
на первую строку об ошибке. Это или Traceback (most recent call last): или Traceback
(innermost last): Так как номера строк кода, пути имена могут меняться, середина
вывода игнорируется. Её можно заменить на многоточие. Важна последняя строка,
которая начинается с типа ошибки и последующего за ней текста.
"""
# Запуск всех тестов: убедиться, что новые тесты не проходят

"""Запускаем файл с кодом даже не включая режим отображения verbose. И получаем
огромный список ошибок заканчивающийся следующим итогом:
*****************************************************************
*****
1 items had failures:
5 of 7 in __main__.is_prime
***Test Failed*** 5 failures.
Логично провалить 5 новых тестов, ведь мы пока не писали код, который позволит
их пройти.
"""
"""!!! Важно! Так как doctest сравнивает текст, вызов ошибки, например через
raise и печать аналогичного текста через print() будут восприниматься
одинаково.
"""
# Написать код

"""Самое время написать несколько строчек кода внутри функции is_prime(). На
выходе получим следующий файл:
"""
def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time. Working...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time. Working...
    True
    """
    if not isinstance(p, int):
        raise TypeError('The number P must be an integer type')
    elif p < 2:
        raise ValueError('The number P must be greater than 1')
    elif p > 100_000_000:
        print('If the number P is prime, the check may take a long time. Working...')
    for i in range(2, p):
        if p % i == 0:
            return False
    return True
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

"""Понадобилось написать шесть строк кода, три проверки.
1. Убедиться что число целое, иначе вызвать ошибку типа.
2. Убедиться, что число не меньше двух, иначе вызвать ошибку значения. Тут мы
проходим сразу два теста из пяти добавленных в техзадании.
3. Убедиться, что число меньше ста миллионов, иначе вывести
предупреждение. Снова закрываем два теста одной проверкой"""

# Запуск всех тестов: убедиться, что все тесты проходят
"""Запуск кода без режима verbose ничего не выводит. Код успешно проходит тесты. С
режимом отображения увидим успешное прохождение всех семи тестов:
...
7 passed and 0 failed.
Test passed.
"""