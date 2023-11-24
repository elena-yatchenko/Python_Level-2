
# !!! Примеры реализации задач 5-6
# https://docs-python.ru/standart-library/modul-pathlib-python/manipuljatsii-putjami-fajlovoj-sistemy-sistemnyh-vyzovov/

import logging
import argparse
from datetime import datetime

logging.basicConfig(filename='error.log', encoding='utf-8', level=logging.ERROR)

logger = logging.getLogger(__name__)

MONTHS = (' ', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')
WEEKDAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')

def get_date(text):
    try:
        count, weekday, month = text.split()
    except ValueError as e:
        logger.error(f'Не смог разбить строку "{text}" на компоненты')
        return None
    
    count = int(count) if count.isdigit() else int(count[:-2])
    weekday = int(weekday) if weekday.isdigit() else WEEKDAYS.index(weekday[:3])
    month = int(month) if month.isdigit() else MONTHS.index(month[:3])
    spam = 0
    for day in range(1, 31 + 1):
        date = datetime(day=day, month=month, year=datetime.now().year)
        if date.weekday() == weekday:
            spam += 1
            if spam == count:
                return date

def parse():
    parser = argparse.ArgumentParser(
        prog='get_date()',
        description='Получаем дату по дню недели и месяцу',
        epilog='При отсутствии значений параметров берётся текущий день недели и текущий месяц'
        )
    parser.add_argument('-c', '--count', default=1,
    help='Какой по счёту день недели? ')
    parser.add_argument('-w', '--weekday', default=datetime.now().weekday(),
    help='Названия дня недели? ')
    parser.add_argument('-m', '--month', default=datetime.now().month,
    help='Названия месяца? ')
    args = parser.parse_args()
    return get_date(f'{args.count} {args.weekday} {args.month}')

if __name__ == '__main__':
    print(get_date('1-йчетвергноября'))
    print(get_date('1-й четверг ноября'))
    print(get_date('3-я среда мая'))

print(parse())


# 6 задача
# Можно было сделать так
import argparse
import logging
from collections import namedtuple
from pathlib import Path

logging.basicConfig(filename='dir_info.txt', encoding='utf-8', level=logging.INFO)

logger = logging.getLogger(__name__)

File = namedtuple('File', 'name, extension, dir, parent')

def read_dir(path: Path):
    for file in path.iterdir():
        obj = File(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(obj)
        if obj.dir:
            read_dir(Path(obj.parent) / obj.name)

def walker():
    parser = argparse.ArgumentParser(
    prog='walk()',
    description='Сохраняем данные о каталоге в файл',
    )
    parser.add_argument('-p', '--path', required=True, type=Path,
    help='Какую директорию анализируем? ')
    args = parser.parse_args()
    return read_dir(args.path)

if __name__ == '__main__':
    walker()