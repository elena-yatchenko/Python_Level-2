"""
📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.
📌 Логируйте ошибки, если текст не соответсвует формату.
"""
from datetime import datetime

import logging

logging.basicConfig(level=logging.INFO, filename="file.log", encoding="utf-8")
logger = logging.getLogger(__name__)

MONTHS = [
    "   ",
    "янв",
    "фев",
    "мар",
    "апр",
    "мая",
    "июн",
    "июл",
    "авг",
    "сен",
    "окт",
    "ноя",
    "дек",
]
WEEKDAYS = ["пон", "вто", "сре", "чет", "пят", "суб", "вос"]


def transf_date(text: str):
    try:
        num, weekday, month = text.split()
        num = int(num[0])
        weekday = WEEKDAYS.index(weekday[:3])
        month = MONTHS.index(month[:3])
        count = 0
    except ValueError as e:
        logger.error(f"в тексте {text} возникла ошибка")
        return None

    for day in range(1, 32):
        date = datetime(day=day, month=month, year=datetime.now().year)
        if date.weekday() == weekday:
            count += 1
            if count == num:
                logger.info(f"Получили текст {text}. Результат - дата {date}")
                return date
    logger.error(f"Дата не определена. Возможно, стоит проверить параметр {num}")


print(transf_date("1-й четверг ноября"))
print(transf_date(" 7-я среда мая"))
