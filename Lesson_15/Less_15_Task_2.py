"""
📌 На семинаре про декораторы был создан логирующий декоратор.
    Он сохранял аргументы функции и результат её работы в файл.
📌 Напишите аналогичный декоратор, но внутри используйте модуль logging.
"""

"""в качестве ключа можно взять или пару входящих значений, или результат, или параметр даты (лучше всего, Точно будет уникальное)
!!!дописать"""

from datetime import datetime

import logging

logging.basicConfig(level=logging.INFO, filename="file.log", encoding="utf-8")
logger = logging.getLogger(__name__)


def dec_log(func):
    def wrapper(*args, **kwarqs):
        _datetime = datetime.now()
        data = dict()
        res = func(*args, **kwarqs)
        """записываем входные параметры функции и результат ее работы в словарь, ключ - текущий момент времени"""
        data[_datetime] = (args, res)
        """args можно выводить в файл log и в виде кортежа (args) и как отдельные значения через запятую (*args)"""
        logger.info(data)
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
