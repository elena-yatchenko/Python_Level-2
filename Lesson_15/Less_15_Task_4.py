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
        num, weekday, month = text.split()  # распаковка параметров
        num = int(num[0]) # num[0] - берем 1-й элемент полученной строки '1-й'
        weekday = WEEKDAYS.index(weekday[:3]) # находим индекс (числовое значение) дня недели (понедельник - 0, воскресенье - 6)
        month = MONTHS.index(month[:3]) # находим индекс (числовое значение) месяца из списка MONTHS, где первый - пробел, 
        # чтобы начать не с 0, а с 1 счет месяцев 
        count = 0 # порядковый номер выбранного дня недели в месяце
    except ValueError as e:
        logger.error(f"в тексте {text} возникла ошибка")
        return None # return, чтобы функция остановилась, а не ломалась. Дальше нет смысла работать, если вышла ошибка

    # перебираем по датам полученный месяц
    for day in range(1, 32):
        # получаем дату из предоставленных данных
        date = datetime(day=day, month=month, year=datetime.now().year)
        if date.weekday() == weekday: # когда в месяце встречаем заданный день недели, добавляем счетчик
            count += 1
            if count == num:
                logger.info(f"Получили текст {text}. Результат - дата {date}")
                return date # останавливаем цикл, когда получаем нужный поряковый номер дня
    logger.error(f"Дата не определена. Возможно, стоит проверить параметр {num}")


print(transf_date("1-й четверг ноября"))
print(transf_date(" 7-я среда мая"))
