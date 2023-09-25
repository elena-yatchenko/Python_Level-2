# Задание №6

# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


# idx1 = 4
# idx2 = 28

def my_sum(my_list: list, idx1: int, idx2: int) -> int:
    lst_2 = []

    if idx1 < 0:
        idx1 = 0 
    if idx2 > len(my_list):
        idx2 = len(my_list)-1
    for idx in range(idx1, idx2+1): # отбираем элементы списка между переданными индексами, включая сами индексы
        lst_2.append(my_list[idx])
    return sum(lst_2)

lst = [25, 254, 0, 2, 3, 8, 21, 6, 8, 4]

print(my_sum(lst, 4, 28)) # 50
print(my_sum(lst, -2, 5)) # 292
print(my_sum(lst, 2, 5)) # 13

