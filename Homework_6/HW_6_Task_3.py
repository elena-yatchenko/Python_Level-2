# Расстановка ферзей

# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка 
# ферзей на шахматной доске, в которой ни один ферзь не бьет другого. 
# Другими словами, ферзи размещены таким образом, что они не находятся на одной вертикали, 
# горизонтали или диагонали.

# Список из 4х комбинаций координат сохраните в board_list. 
# Дополнительно печатать его не надо.

# Пример использования 
# На входе:
# print(generate_boards())
# На выходе:
# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)], [(1, 5), (2, 3), (
# 3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)], [(1, 3), (2, 6), (3, 8), (4, 2[(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]), (5, 4), 
# (6, 1), (7, 7), (8, 5)], ]

from itertools import combinations, permutations

from random import randint, sample, shuffle

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for elem in combinations(queens, 2):
        q1, q2 = elem
        if is_attacking(q1, q2):
            return False
    return True

def generate_boards():
    # my_list = [(randint(1, 8), randint(1, 8)) for i in range(8)]
    all_permutation = list(permutations(range(1, 9)))
    shuffle(all_permutation)
    """ если не указан параметр r (длина генерируемых кортежей), тогда permutations генерирует кортежи длиной 
    переданного объекта iterable"""
    #print(all_permutation)
    # queens = sample((my_list), 8)

    board_list = []
    n = 1
    
    # while n <= 4:
    for permutation in all_permutation:
        if n <= 4:
        # идем по кортежам, сгенерированным generate_boards() и добавляем позицию (индекс+1) к каждому элементу кортежа?
        # получая список-расстановку из 8 пар)
            queens = [(i+1, permutation[i]) for i in range(8)]  
            if check_queens(queens):
                board_list.append(queens)
                n += 1
        else:
            break
    return board_list
    
 
print(generate_boards())
# print(check_queens([(1, 6), (2, 3), (3, 7), (4, 4), (5, 1), (6, 8), (7, 2), (8, 5)]))
# print(show_result())


# print(generate_boards())

# РЕШЕНИЕ СИСТЕМЫ

# import random
# from itertools import combinations

# def generate_board():
#     # Генерируем случайную доску
#     board = []

#     for i in range(1, 8+1):
#         queen = (i, random.randint(1, 8))
#         board.append(queen)
#     return board

# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True

# def generate_boards():
#     # Генерируем доски, пока не получим 4 успешные расстановки
#     count = 0
#     board_list = []
#     while count < 4:
#         board = generate_board()
#         if check_queens(board):
#             count += 1
#             board_list.append(board)
#     return board_list
