"""
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
import doctest


def clear_text(text: str):
    """
    >>> clear_text('this is a sample')
    'this is a sample'
    >>> clear_text('This is a sample')
    'this is a sample'
    >>> clear_text('this is a sample,')
    'this is a sample'
    >>> clear_text('this is a sample вапвап')
    'this is a sample '
    >>> clear_text('This is a Sample, - вапвап')
    'this is a sample  '
    """
    clear = "".join(
        [
            letter
            for letter in text.lower()
            if ord(letter) in range(97, 123) or letter.isspace()
        ]
    )
    return clear.lower()


result = clear_text("This is a sample, вапвап 3453456")
print(result)

if __name__ == "__main__":
    doctest.testmod(verbose=True)
