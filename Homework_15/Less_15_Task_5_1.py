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

parser = argparse.ArgumentParser(prog='find date', description='Task_5 parser')
"""если вводим просто 1 параметр-строку, как в задаче 4"""
parser.add_argument('request', metavar='text', type=str, nargs='*', help='введите строку запроса')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

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


print(transf_date(*args.request))
# запуск: python Less_15_Task_5_1.py '1-й четверг ноября' 


"""
запуск: python Less_15_Task_5_1.py -h

результат:
 
usage: find date [-h] text [text ...]

Task_5 parser

positional arguments:
  text        введите строку запроса

options:
  -h, --help  show this help message and exit
"""