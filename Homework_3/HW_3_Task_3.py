# Список вещей для похода - Все варианты
# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Результат должен быть в виде словаря с вещами в рюкзаке:{предмет:вес}
# *Верните все возможные варианты комплектации рюкзака.
# Пример
# На входе:
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
# На выходе:
# [{'ключи': 0.3},
#  {'кошелек': 0.2},
#  {'ключи': 0.3, 'кошелек': 0.2},
#  {'телефон': 0.5},
#  {'ключи': 0.3, 'телефон': 0.5},
#  {'кошелек': 0.2, 'телефон': 0.5},
#  {'ключи': 0.3, 'кошелек': 0.2, 'телефон': 0.5},
#  {'зажигалка': 0.1},
#  {'зажигалка': 0.1, 'ключи': 0.3},
#  {'зажигалка': 0.1, 'кошелек': 0.2},
#  {'зажигалка': 0.1, 'ключи': 0.3, 'кошелек': 0.2},
#  {'зажигалка': 0.1, 'телефон': 0.5},
#  {'зажигалка': 0.1, 'ключи': 0.3, 'телефон': 0.5},
#  {'зажигалка': 0.1, 'кошелек': 0.2, 'телефон': 0.5},
#  {'ключи': 0.3, 'кошелек': 0.2, 'телефон': 0.5}]



# import decimal
# decimal.getcontext().prec = 20

# weight = 0
# backpack = {}

# for key in items.keys():
#     weight += (items[key])
#     #print(weight)
#     if (weight) < (max_weight):
#         backpack[key] = items[key]
#     else:
#         weight -= (items[key])
# #print(decimal.Decimal(weight))
# print(backpack)

# решение системы:

backpack = {}
lst = []
for item, weight in items.items():
    for j in range
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight

print(backpack)

не знаю, как решить? 
