"""
📌 Доработаем задачу 2.
📌 Сохраняйте в лог файл раздельно:
    ○ уровень логирования,
    ○ дату события,
    ○ имя функции (не декоратора), - полезно, т.к. бывает нужно знать, в какой функции произошла ошибка
    ○ аргументы вызова,
    ○ результат.
"""

from datetime import datetime

import logging

logging.basicConfig(level=logging.INFO, filename="file.log", encoding="utf-8")
logger = logging.getLogger(__name__)


def dec_log(func):
    def wrapper(*args, **kwarqs):
        _datetime = datetime.now()
        data = dict()
        res = func(*args, **kwarqs)
        data[_datetime] = (args, res)
        logger.info(f"{func.__name__}:{data}")
        return res

    return wrapper


@dec_log
def zero_devide(num_1, num_2):
    try:
        result = num_1 / num_2
    except ZeroDivisionError as e:
        result = float("inf")
    return result


print(zero_devide(2, 4))
print(zero_devide(2, 0))
