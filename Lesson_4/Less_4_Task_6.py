# Задание №6

# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


# idx1 = 4
# idx2 = 28
from random import randint # для рандомного составления списка. 
my_list = [randint(1, 10) for i in range(10)]
print(my_list)
a, b = map(int,input('Ввести 2 числа через пробел: ').split())

def my_sum(my_list: list, idx1: int, idx2: int) -> int:
    
    if idx1 > idx2:
        idx2, idx1 = idx1, idx2
    if idx1 < 0:
        idx1 = 0 
    if idx2 > len(my_list):
        idx2 = len(my_list)-1
    result = sum(my_list[idx1:idx2+1])
    return result

print(my_sum(my_list, a, b))

# [7, 8, 7, 2, 9, 8, 1, 9, 1, 5]
# Ввести 2 числа через пробел: 100 0
# 57

# [9, 1, 10, 7, 3, 4, 7, 3, 5, 10]
# Ввести 2 числа через пробел: 0 100
# 59

# [3, 6, 5, 3, 1, 7, 6, 2, 1, 5]
# Ввести 2 числа через пробел: -1 20
# 39

# если задаем вручную данные
# lst = [25, 254, 0, 2, 3, 8, 21, 6, 8, 4]

# print(my_sum(lst, 4, 28)) # 50
# print(my_sum(lst, -2, 5)) # 292
# print(my_sum(lst, 2, 5)) # 13

