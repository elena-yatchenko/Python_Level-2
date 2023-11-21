"""
📌 Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль.
"""

import logging

logging.basicConfig(level=logging.INFO, filename="file.log", encoding="utf-8")

logger = logging.getLogger(__name__)


def zero_devide(num_1, num_2):
    try:
        result = num_1 / num_2
    except ZeroDivisionError as e:
        logger.error(f"Получили ошибку {e}\nПараметры {num_1} {num_2}")
        result = float("inf")
    logger.info(f"Параметры {num_1} {num_2}. Результат равен {result}")
    return result


print(zero_devide(2, 4))
print(zero_devide(2, 0))
