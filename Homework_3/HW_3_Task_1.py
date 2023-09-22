# Список вещей для похода
# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Результат должен быть в виде словаря с вещами в рюкзаке:{предмет:вес}.
# Достаточно вернуть один допустимый вариант.
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

# {'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}

# items = {
#     "спальник": 1.5,
#     "палатка": 3.2,
#     "термос": 0.6,
#     "карта": 0.1,
#     "фонарик": 0.3,
#     "котелок": 0.8,
#     "еда": 2.5,
#     "одежда": 1.7,
#     "обувь": 1.2,
#     "нож": 0.2
# }
# max_weight = 1

import decimal
decimal.getcontext().prec = 20

weight = 0
backpack = {}

for key in items.keys():
    weight += decimal.Decimal(items[key])
    #print(weight)
    if decimal.Decimal(weight) < decimal.Decimal(max_weight):
        backpack[key] = items[key]
    else:
        weight -= decimal.Decimal(items[key])
#print(decimal.Decimal(weight))
print(backpack)

# решение системы:

backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight

print(backpack)