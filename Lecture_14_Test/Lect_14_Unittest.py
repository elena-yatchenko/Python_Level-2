# Основы тестирования с unittest

"""Рассмотрим более мощный по функциональности инструмент тестирования из
коробки. Модуль unittest входит в стандартную библиотеку Python и не требует
дополнительной установки. Более того, unittest называют фреймворком, а не просто
модулем"""

# Общие моменты работы с unittest

# import unittest


# class TestCaseName(unittest.TestCase):
#     def test_method(self):
#         self.assertEqual(2 * 2, 5, msg="Видимо и в этой вселенной не работает :-(")


# if __name__ == "__main__":
#     unittest.main()

# AssertionError: 4 != 5 : Видимо и в этой вселенной не работает :-(

"""Для хранения тестов рекомендуется создавать отдельный файл с тестами или папку
tests, если файлов с тестами будет много. Смешивать в одном файле исполняемый
код и тесты не рекомендуется.
В файле с тестом импортируем модуль unittest и создаём класс для тестирования -
test case. Такой класс должен наследоваться от TestCase.
Внутри класса создаём методы, имена которых должны начинаться со слова test.
Таких методов внутри класса может быть несколько.
По наследованию от класса TestCase и именам методов unittest понимает, что перед
ним тесты, которые необходимо запустить.

Для проверки используем утверждения - “ассерты”. В приведённом примере
assertEqual принимает два аргумента: 2 * 2 и 5. Тест утверждает, что они равны. А
если значения не равны, будет поднято исключение AssertionError с текстом,
который передали в ключевом параметре msg.
"""

"""Внимание! Реальные тесты не должны содержать неверные утверждения, подобные “дважды два равно пяти”"""

"""Для запуска тестов вызываем функцию main(). Она проанализирует файл, соберёт тестовые кейсы, 
запустит и сообщит результаты проверки"""

"""Внимание! Команда для запуска тестов из командной строки выглядит аналогично запуску doctest"""

""" 
$ python3 -m unittest tests.py -v
"""

# Применение тестов Unittest

"""Файл prime.py без тестов doctest"""

# def is_prime(p: int) -> bool:
#     if not isinstance(p, int):
#         raise TypeError("The number P must be an integer type")
#     elif p < 2:
#         raise ValueError("The number P must be greater than one")
#     elif p > 100_000_000:
#         print("If the number P is prime, the check may take a long time. Working...")
#     for i in range(2, p):
#         if p % i == 0:
#             return False
#     return True

"""А тесты прописываем в файле test_prime.py"""

# ЗАПУСК ТЕСТОВ DOCTEST ИЗ UNİTTEST

"""А что если тесты уже написаны в doctest? В этом случае можно создать функцию
test_loader и добавить тесты doctest в перечень для тестирования. Изучите пример."""

# import doctest
# import unittest

# import prime

# def load_tests(loader, tests, ignore):
#     tests.addTests(doctest.DocTestSuite(prime))
#     tests.addTests(doctest.DocFileSuite('prime.md'))
#     return tests

# if __name__ == '__main__':
#     unittest.main(verbosity=2)

"""Объект tests используя метод addTests добавляет импортированный модуль prime.
Для этого используется класс DocTestSuite из модуля doctest. А если необходимо
тестировать документацию, используется класс DocFileSuite. Теперь функция
unittest.main соберёт написанные раннее тесты doctest и запустит их.
"""

# ПОДГОТОВКА ТЕСТА И СВОРАЧИВАНИЕ РАБОТ

"""Иногда бывает необходимо выполнить какие-то действия до начала тестирования,
развернуть тестируемую среду. А после завершения теста наоборот, убрать лишнее.
Для этих целей в unittest есть зарезервированные имена методов setUp и tearDown.
Часто их называют фикстурами."""

# ➢ МЕТОД setUp

"""Когда внутри класса есть несколько тестовых методов, вызов метода setUp происходит ПЕРЕД КАЖДЫМ вызовом теста.
"""
import unittest

class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [2, 3, 5, 7]
        print('Выполнил setUp') # Только для демонстрации работы метода

    def test_append(self):
        self.data.append(11)
        self.assertEqual(self.data, [2, 3, 5, 7, 11])

    def test_remove(self):
        self.data.remove(5)
        self.assertEqual(self.data, [2, 3, 7])

    def test_pop(self):
        self.data.pop()
        self.assertEqual(self.data, [2, 3, 5])

if __name__ == '__main__':
    unittest.main()

"""В примере трижды создаётся список на четыре элемента. Каждый из тестов
ожидает, что будет работать с числами 2, 3, 5, 7 и никак не учитывает результаты
работы других тестов. Подобный подход удобен, когда надо прогнать большое
количество тестов на одном и том же наборе данных."""

# ➢ МЕТОД tearDown

"""Метод tearDown будет вызван после успешного выполнения метода setUp и в случае
если тест отработал успешно, и если он провалился"""

import unittest

class TestSample(unittest.TestCase):
    def setUp(self) -> None:
        with open('top_secret.txt', 'w', encoding='utf-8') as f:
            for i in range(10):
                f.write(f'{i:05}\n')

    def test_line(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                pass
        self.assertEqual(i, 10)

    def test_first(self):
        with open('top_secret.txt', 'r', encoding='utf-8') as f:
            first = f.read(5)
            self.assertEqual(first, '00000')

    def tearDown(self) -> None:
        from pathlib import Path
        Path('top_secret.txt').unlink()

if __name__ == '__main__':
    unittest.main()

"""В примере метод setUp создаёт перед каждым тестом файл со строками чисел. Два
теста работают с этим файлом. И после каждого происходит удаление файла из
tearDown метода.
Даже если провалить тест, файл будет удалён.
"""

# Перечень доступных утверждений assert

"""
В списке ниже приведены доступные в unittest утверждения и пояснения о том что
именно они проверяют.
● assertEqual(a, b) - a == b
● assertNotEqual(a, b) - a != b
● assertTrue(x) - bool(x) is True
● assertFalse(x) - bool(x) is False
● assertIs(a, b) - a is b
● assertIsNot(a, b) - a is not b
● assertIsNone(x) - x is None
● assertIsNotNone(x) - x is not None
● assertIn(a, b) - a in b
● assertNotIn(a, b) - a not in b
● assertIsInstance(a, b) - isinstance(a, b)
● assertNotIsInstance(a, b) - not isinstance(a, b)
● assertRaises(exc, fun, *args, **kwds) - функция fun(*args, **kwds) поднимает
исключение exc
● assertRaisesRegex(exc, r, fun, *args, **kwds) - функция fun(*args, **kwds)
поднимает исключение exc и сообщение совпадает с регулярным
выражением r
● assertWarns(warn, fun, *args, **kwds) - функция fun(*args, **kwds) поднимает
предупреждение warn
● assertWarnsRegex(warn, r, fun, *args, **kwds) - функция fun(*args, **kwds)
поднимает предупреждение warn и сообщение совпадает с регулярным
выражением r
● assertLogs(logger, level) - блок with записывает логи в logger с уровнем level
20
● assertNoLogs(logger, level) - блок with не записывает логи в logger с уровнем
level
● assertAlmostEqual(a, b) - round(a-b, 7) == 0
● assertNotAlmostEqual(a, b) - round(a-b, 7) != 0
● assertGreater(a, b) - a > b
● assertGreaterEqual(a, b) - a >= b
● assertLess(a, b) - a < b
● assertLessEqual(a, b) - a <= b
● assertRegex(s, r) - r.search(s)
● assertNotRegex(s, r) - not r.search(s)
● assertCountEqual(a, b) - a и b содержат одни и те же элементы в одинаковом
количестве независимо от их порядка в коллекциях
Как вы видите перечень допустимых проверок достаточно обширный, чтобы
удовлетворить практически любые запросы по написанию тестов.
"""

