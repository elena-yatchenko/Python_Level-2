"""
Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

from Less_14_TAsk_2 import clear_text
import pytest

def test_non_change():
    assert "this is a sample" == clear_text("this is a sample"), "провал"


def test_register():
    assert "this is a sample" == clear_text("This is a sample"), "провал"


def test_punctuation():
    assert "this is a sample" == clear_text("this is a sample,"), "провал"


def test_another_alph():
    assert "this is a sample " == clear_text("this is a sample вапвап"), "провал"


def test_all():
    assert "this is a sample  " == clear_text("This is a Sample, - вапвап"), "провал"


###333




if __name__ == '__main__':
    pytest.main(['-sv'])