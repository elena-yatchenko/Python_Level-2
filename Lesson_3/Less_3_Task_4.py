# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

my_list = [2, 5, 3, 3, 3, 2, 5, 10, 11, 12]

for i in my_list:
    if my_list.count(i) == 2:
        for j in range(2): # говорим, что цикл нужно повторить 2 раза
            my_list.remove(i)

print(my_list)

# Говорим, что хотим запустить операцию remove для каждого подходящего под условие (count == 2) элемента 2раза. 
# Иначе remove() найдет первое его вхождение в лист, удалит и остановится. Дальше по списку она не пойдет
# А так он после 1-й проходки цикла удалит 1 значение, а после второй найдет в списке уже следующее такое же и удалит его тоже

# [3, 3, 3, 10, 11, 12]
