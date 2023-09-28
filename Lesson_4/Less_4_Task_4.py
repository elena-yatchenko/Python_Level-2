# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

''' пузырьковая сортировка, принцип: большие (тяжелые) пузырьки поднимаются наверх, 
а маленькие остаются вначале. Т.е мы постоянно сравниваем первый элемент 
со вторым и так далее и перемещаем в случае, если следующий элемент меньше. 
Мы так выдавливаем. Важно: фиксировать отсортированную часть. 
Любая сортировка - это 2 цикла'''

my_list = [3, 5, 1, 8, 10, 120, 25, 1]

for j in range(len(my_list)-1): # по j идем, чтоб список уменьшать на j, не терять время на проверку отсортированных
    for i in range(len(my_list) -1 - j): # -j - фиксируем правую отсортированную часть списка, чтобы туда не лезть
       if my_list[i] > my_list[i+1]:
           my_list[i], my_list[i +1] = my_list[i + 1], my_list[i]
print(my_list) 
        
# [1, 1, 3, 5, 8, 10, 25, 120]