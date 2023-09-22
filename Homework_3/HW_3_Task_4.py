# Cписок повторяющихся элементов

# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке 
# не должно быть дубликатов.

# Пример
# На входе:
# lst = [1, 1, 2, 2, 3, 3]
# На выходе: 
# [1, 2, 3]

lst = [1, 1, 2, 2, 3, 3]

new_lst = []
for elem in lst:
    if lst.count(elem) > 1:
        new_lst.append(elem)
print(list(set(new_lst)))

# РЕШЕНИЕ СИСТЕМЫ  !!!!

# duplicates = set()

# for item in lst:
#     if lst.count(item) >= 2:
#         duplicates.add(item)

# result = list(duplicates)
# print(result)
