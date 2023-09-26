# Задание №7

# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

my_dict = dict(comp1=[5, 85, 25, -80, 120], comp2=[65, 52, 42, -52, 0], comp3=[25, 41, 20, 13])
# print(my_dict)


# def profit(my_dict: dict[str, list[int]]) -> bool:
#     result_list = []
#     for company, summa in my_dict.items():
#         result = sum(summa)
#         result_list.append(result)
#     return all(map(lambda x: x > 0, result_list))

# или

def profit(my_dict: dict[str, list[int]]) -> bool:
    return all(map(lambda x: sum(x) > 0, my_dict.values()))
   
    
print(profit(my_dict))

# result_list = []
# for company, summa in my_dict.items():
#     result = sum(summa)
#     result_list.append(result)
# print(result_list)
# if all(map(lambda x: x > 0, result_list)):
#     print(True)
# else:
#     print(False)   

# [155, 107, 99]
# True

# [155, -127, 99]
# False