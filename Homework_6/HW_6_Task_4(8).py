# Задание №8
# � Создайте пакет с всеми модулями, которые вы создали за
# время занятия.
# � Добавьте в __init__ пакета имена модулей внутри дандер
# __all__.
# � В модулях создайте дандер __all__ и укажите только те
# функции, которые могут верно работать за пределами
# модуля.

from mymodul import chess

print(chess.check_queens([(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]))