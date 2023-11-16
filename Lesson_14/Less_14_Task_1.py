"""
📌 Создайте функцию, которая удаляет из текста все символы
    кроме букв латинского алфавита и пробелов.
📌 Возвращается строка в нижнем регистре.
"""

# letter: str
# letter.isascii()
# letter.isspace()


def clear_text(text: str):
    clear = "".join(
        [
            letter
            for letter in text.lower
            if ord(letter) in range(97, 123) or letter.isspace()
        ]
    )
    return clear.lower()


result = clear_text("This is a sample, текст на русском 12544")
print(result)

# letter : str
# letter.isascii()
# letter.isspace()


def clear_text(text: str):
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
