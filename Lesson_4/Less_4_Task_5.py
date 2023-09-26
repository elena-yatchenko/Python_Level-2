# Задание №5

# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 

name = ['Sam', 'Nick', 'John']
salary = [2500, 1850, 2000]
percent = ['25%', '60%', '40%']

# print(list(zip(name, salary, percent)))

def package(name: list, salary: list, percent: list) -> dict: # как это оформить через args?
    dict = {}
    for name, salary, percent in zip(name, salary, percent):
        dict[name] = round(salary * float(percent[:-1]) / 100, 2)
    return dict

print(package(name, salary, percent))

# {'Sam': 625.0, 'Nick': 1110.0, 'John': 800.0}

# dict = {}
# for name, salary, percent in zip(name, salary, percent):
#     dict[name] = salary * float(percent)
# print(dict)

# # вариант через элементы списка
# dict = {}
# for elem in list(zip(name, salary, percent)):
#     dict[elem[0]] = elem[1] * float(elem[2])
# print(dict)

