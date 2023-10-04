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

from random import randint, sample

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
    my_list = list(permutations(range(1, 9), 2))
    queens = sample((my_list), 8)
    # print(my_list)
    return queens

# print(generate_boards())

#def show_result():
# board_list = []
# n = 0
# while n <= 4:
#     if check_queens(generate_boards()) == True:
#         board_list.append(generate_boards())
#         n += 1
#     # return board_list
# print(board_list)

print(check_queens([(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]))
# print(show_result())


# print(generate_boards())

