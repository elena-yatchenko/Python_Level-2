"""Задание №5
Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5."""

from datetime import datetime
import logging
import argparse

parser = argparse.ArgumentParser(prog="find date", description="Task_5 parser")

parser.add_argument(
    "-num",
    metavar="N",
    type=str,
    help="введите номер дня недели (строка или целое число)",
    default="1",
)
parser.add_argument(
    "-weekday",
    metavar="W",
    type=str,
    help="введите день недели (строка или целое число)",
    default=str(datetime.now().weekday()),
)
parser.add_argument(
    "-month",
    metavar="M",
    type=str,
    help="введите месяц (строка или целое число)",
    default=str(datetime.now().month),
)
args = parser.parse_args()
print(f"В скрипт передано: {args}")


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


def transf_date(data_num: str, data_weekday: str, data_month: str):
    _datetime = datetime.now()
    logger.info(f'Получили данные: {", ".join((data_num, data_weekday, data_month))}')
    if not data_num.isdigit():
        try:
            num = int(data_num[0])
        except ValueError as e:
            logger.error(
                f"{_datetime}: при вводе текста возникла ошибка {e}. Значение {data_num}"
            )
            return None
    else:
        num = int(data_num)

    if not data_weekday.isdigit():
        try:
            weekday = WEEKDAYS.index(data_weekday[:3])
        except ValueError as e:
            logger.error(f"{_datetime}: При вводе тексте возникла ошибка {e}.")
            return None
    else:
        weekday = int(data_weekday)
        if not (0 <= weekday <= 6):
            logger.warning(
                f"{_datetime} Численное значение дня недели должно быть в диапазоне от 0 до 6. Введено {data_weekday}"
            )
            weekday = 0
            logger.warning(
                f"{_datetime} Принимаем значение дня недели равным 0 (понедельник)."
            )

    if not data_month.isdigit():
        try:
            month = MONTHS.index(data_month[:3])
        except ValueError as e:
            logger.error(f"{_datetime}: При вводе тексте возникла ошибка {e}.")
            return None
    else:
        month = int(data_month)
        if not (0 < month <= 12):
            logger.warning(
                f"{_datetime} Численное значение месяца должно быть в диапазоне от 1 до 12. Введено {data_month}"
            )
            month = 1
            logger.warning(f"{_datetime} Принимаем значение месяца равным 1 (январь).")

    count = 0
    for day in range(1, 32):
        try:
            date = datetime(day=day, month=month, year=datetime.now().year)
            if date.weekday() == weekday:
                count += 1
                if count == num:
                    logger.info(f"Результат - дата {date}")
                    return date
        except ValueError as e:
            logger.error(f"Дата не определена. Закончились дни в месяце")
            return None
    logger.error(f"Дата не определена. Возможно, стоит проверить параметр {num}")


print(transf_date(args.num, args.weekday, args.month))

# запуск:
# python Less_15_Task_5_some.py -num '2-й' -weekday 'чbтверг' -month 'ноября'
# python Less_15_Task_5_some.py -num 2 -weekday 7 -month 11
# python Less_15_Task_5_some.py -weekday 'четверг' -month 0
# python Less_15_Task_5_some.py -num '1-я' -weekday 'среда'
# python Less_15_Task_5_some.py
# python Less_15_Task_5_some.py -num '2-й' -weekday 'четверг' -month 'ноября'

"""
ВОПРОСЫ:
1. Если бы делали декоратор wrapper, использовали бы там только kwarqs? (если параметры ключевые тут передаем из терминала)
2. При вводе args из командной строки всегда получаем их в виде строкового значения?

Если нет, то как прописать 2 варианта типов данных для add_argument()? Например если я могу получить 
данные и в виде строки, и в виде целого числа (потом в функции обработаю в зависимости от того, в каком виде получила? 
type=?

parser.add_argument('-num', metavar='N', type=str, help='введите номер дня недели (строка или целое число)', default='1')
"""

"""
запуск: python Less_15_Task_5.py -h

результат:
 
usage: find date [-h] text [text ...]

Task_5 parser

positional arguments:
  text        введите строку запроса

options:
  -h, --help  show this help message and exit
"""
