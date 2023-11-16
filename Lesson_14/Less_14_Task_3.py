"""
Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
import unittest
from Less_14_TAsk_2 import clear_text


class TestStr(unittest.TestCase):
    def test_non_change(self):
        self.assertEqual("this is a sample", clear_text("this is a sample"))

    def test_register(self):
        self.assertEqual("this is a sample", clear_text("This is a sample"))

    def test_punctuation(self):
        self.assertEqual("this is a sample", clear_text("this is a sample,"))

    def test_another_alph(self):
        self.assertEqual("this is a sample ", clear_text("this is a sample вапвап"))

    def test_all(self):
        self.assertEqual("this is a sample  ", clear_text("This is a Sample, - вапвап"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
