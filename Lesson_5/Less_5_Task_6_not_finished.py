# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»

# без перехода на новую строку.

# решение из задачи семинара 1
# for i in range(2, 11):
#     for j in range(2, 6):
#         print(f"{j} x {i} = {j * i}\t", end="")
#     print("\t", end="")
#     for j in range(6, 10):
#         print(f"{j} x {i} = {j * i}\t", end="")
#     print()
    
# mult_table = ((f"{j} x {i} = {j * i}\t" for j in range(2, 10)) for i in range(2, 11))

# for elem in mult_table:
#     print(elem)

mult_table = (((print('\n\n', end='') if (k == 5 or k == 9) and (k == 5 and j == 10) else print('\n', end='') if (k == 5 or k == 9) and not (k == 5 and j == 10) \
                else print('\t', end='') if not (k == 5 or k == 9) else f'{k:2} * {j:2} = {j * k:2}' for  k in range(2 + i * 4, 6 + i * 4)) for j in range(2, 11)) for i in range(2))
for elem in mult_table:
    print(elem)
?????
#     записать тернарным оператором

# print("ТАБЛИЦА УМНОЖЕНИЯ".center(62))

# for i in range(2):
#     for j in range(2, 11):
#         for k in range(2 + i * 4, 6 + i * 4):
#             print(f'{k:2} * {j:2} = {j * k:2}', end='')
#             if k == 5 or k == 9:
#                 if k == 5 and j == 10:
#                     print('\n\n', end='')
#                 else:
#                     print('\n', end='')
#             else:
#                 print('\t', end='')