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

parser = argparse.ArgumentParser(prog='find date', description='Task_5 parser')
"""вводим несколько параметров, которые могут быть либо строкой, либо числом"""
parser.add_argument('-num', metavar='N', type=str, help='введите номер дня недели (строка или целое число)',
                    default=1)
parser.add_argument('-weekday', metavar='W', type=str, help='введите день недели (строка или целое число)',
                    default=datetime.now().weekday)
parser.add_argument('-month', metavar='M', type=str, help='введите месяц (строка или целое число)', 
                    default=datetime.now().month)
args = parser.parse_args()
# print(f'В скрипт передано: {args}')


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

# def dec_log(func):
#     def wrapper(*args, **kwarqs):
#         _datetime = datetime.now()
#         data = dict()
#         res = func(*args, **kwarqs)
#         data[_datetime] = (args, res)
#         logger.info(f"{func.__name__}:{data}")
#         return res

#     return wrapper


def transf_date(num: str, weekday: str, month: str):
    logger.info(f'Получили данные: {", ".join((num, weekday, month))}')
    
    try:
        num = int(num[0]) 
        weekday = WEEKDAYS.index(weekday[:3]) 
        month = MONTHS.index(month[:3]) 
        count = 0 
    except ValueError as e:
        logger.error(f"в тексте возникла ошибка")
        return None 

    
    for day in range(1, 32):
        date = datetime(day=day, month=month, year=datetime.now().year)
        if date.weekday() == weekday:
            count += 1
            if count == num:
                logger.info(f"Результат - дата {date}")
                return date
    logger.error(f"Дата не определена. Возможно, стоит проверить параметр {num}")


print(transf_date(args.num, args.weekday, args.month))
# запуск:  python Less_15_Task_5_some.py -num '1-й' -weekday 'четверг' -month 'ноября'
# python Less_15_Task_5_some.py -num 3 -weekday 2 -month 11
# python Less_15_Task_5_some.py -num -weekday 'четверг' -month 11
# python Less_15_Task_5_some.py -num '1-я' -weekday 'среда' -month
# python Less_15_Task_5_some.py -num -weekday -month

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