# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

things = dict(
    [
        ("Петя", ("палатка", "термос", "еда", "котелок", "одежда")),
        ("Вася", ("одежда", "еда", "нож", "спички", "котелок")),
        ("Саша", ("одежда", "еда", "нож", "фонарик", "спички")),
    ]
)

stuff = []
for value in things.values():
    stuff.append(set(value))
a, b, c = stuff
# Какие вещи взяли все три друга:
res1 = a.intersection(b, c)
print(f"Все 3 друга взяли следующие вещи: {res1}")
# print(stuff)

res2_1 = a.difference(b, c)
res2_2 = b.difference(a, c)
res2_3 = c.difference(a, b)

res2 = res2_1 | res2_2 | res2_3
print(f"Только у кого-то одного из друзей есть следующие вещи: {res2}")

list_res3 = []
if a & b != a & b & c:
    res3 = (a & b) - (a & b & c)
    list_res3.append(res3)
    print(f"{res3}, разница в {c}")
if b & c != a & b & c:
    res3 = (b & c) - (a & b & c)
    list_res3.append(res3)
    print(f"{res3}, разница в {a}")
if a & c != a & b & c:
    res3 = (a & c) - (a & b & c)
    list_res3.append(res3)
    print(f"{res3}, разница в {b}")

print(list_res3)

for elem in list_res3:
    for key, value in things.items():
        if elem.intersection(value) == set():
            print(f"Друг, у которого нет {elem} - {key}")

# step_list = []
# for idx in range(len(stuff)):
#     diff = stuff[idx]
#     for pos in range(1, len(stuff)):
#         diff.difference_update(stuff[pos])
#     print(diff)
#     for idx in range(len(stuff) - step):
#         step_list.append(stuff[idx + step])
#     print(step_list)
#     for idx in range(step):
#         step_list.append(stuff[idx])
#     print(step_list)


# keys = []


# print(things.items())

#     print(common)
#     keys.append(key)

# print(keys)


# res2 = a ^ b ^ c   # ПОЧЕМУ НЕ РАБОТАЕТ? ДАЕТ {'термос', 'палатка', 'одежда', 'фонарик', 'еда', 'котелок'}
# print(res2)


# ???? как сделать распаковку, чтоб на печать как строку вывести, а не в виде множества. Если не знаешь, сколько
# элементов
