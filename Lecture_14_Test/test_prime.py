import io
import unittest
from unittest.mock import patch
from prime import is_prime

class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(42))
        self.assertTrue(is_prime(73))

    def test_type(self):
        self.assertRaises(TypeError, is_prime, 3.14)

    def test_value(self):
        with self.assertRaises(ValueError):
            is_prime(-100)
            is_prime(1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_false(self, mock_stdout):
        self.assertFalse(is_prime(100_000_001))
        self.assertEqual(mock_stdout.getvalue(), 'If the number P is prime, the check may take a long time. Working...\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_true(self, mock_stdout):
        self.assertTrue(is_prime(100_000_007))
        self.assertEqual(mock_stdout.getvalue(), 'If the number P is prime, the check may take a long time. Working...\n')

if __name__ == '__main__':
    unittest.main(verbosity=2)

"""по умолчанию verbosity=1 - без отображения информации о тесте. verbosity=2 - с отображением инфо """

"""Разберём каждый из тестов внутри класса:

➢ Кейс test_is_prime
Проверяем базовую работу функции. Утверждение assertFalse ожидает получить
ложь в качестве аргумента. В нашем случае в качестве результата вызова функции.
Аналогично assertTrue ожидает получить истину.

➢ Кейс test_type
Утверждение assertRaises ожидает ошибку типа (аргумент один) если вызвать
функцию is_prime (аргумент два) и передать ей число 3.14 (аргумент три).

➢ Кейс test_value
Используем менеджер контекста для утверждения ошибки и внутри контекста
дважды запускаем функцию. assertRaises во всех случаях будет ожидать ошибку
значения

➢ Кейсы test_warning_false и test_warning_true

🔥 Внимание! Оба примера выходят за рамки основ unittest. Это скорее
пример на будущее для самых любознательных.

Используя декоратор patch из модуля mock перенаправляем стандартный поток
вывода sys.stdout обращаясь к StringIO модуля ввода-вывода io. Результат попадает
в параметр mock_stdout. Внутри метода делаем стандартную проверку на ложь или
истину для большого числа. А далее проверяем, что стандартный вывод получил
значение, совпадающее с ожидаемым текстом предупреждения.

🔥 Внимание! Разбор Mock объектов выходит за рамки лекции. Самые
любознательные могут обратиться к стандартной документации языка.
https://docs.python.org/3.11/library/unittest.mock.html
"""

# Вывод результата тестов
"""verbosity=1"""
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 17.745s

# OK

"""verbosity=2"""

# test_is_prime (__main__.TestPrime.test_is_prime) ... ok
# test_type (__main__.TestPrime.test_type) ... ok
# test_value (__main__.TestPrime.test_value) ... ok
# test_warning_false (__main__.TestPrime.test_warning_false) ... ok
# test_warning_true (__main__.TestPrime.test_warning_true) ... ok

# ----------------------------------------------------------------------
# Ran 5 tests in 18.039s

# OK
 