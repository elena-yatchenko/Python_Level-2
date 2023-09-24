# задание 8 (подходит для расширенного количества друзей)
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
        ("Саша", ("стул", "еда", "нож", "фонарик", "спички", "одежда")),
        ("Коля", ("одежда", "топор", "спички", "нож", "котелок"))
    ]
)

                 
stuff = []
for value in things.values():
    stuff.append(set(value))
    
print(stuff)

for elem in stuff:
    common = elem
    for thing in stuff:
        if elem == thing:
            continue
        else: 
            common = common.intersection(thing)
    print(f"Все 3 друга взяли следующие вещи: {' и '.join(common)}")
    break 

diff_list = []
for elem in stuff:
    differ = elem
    for thing in stuff:
        if elem == thing:
            continue
        else: 
            differ = differ.difference(thing)
    if differ != set():
        diff_list.append(differ)
print(diff_list)

for elem in diff_list:
    for key, value in things.items():
        if elem.intersection(value) != set():
            # diff_str = " и ".join(elem)
            print(f"Друг, у которого единственного есть {' и '.join(elem)} - {key}")
            # print(f"Друг, у которого нет {elem} - {key}")
 
exception_list = []

for idx in range(len(stuff)):
    for pos in range(idx+1, len(stuff)):
        if stuff[idx] & stuff[pos] != common:
            exception =  (stuff[idx] & stuff[pos]) - common
            if exception != set():
                exception_list.append(exception)
print(exception_list)

for elem in exception_list:
    for key, value in things.items():
        if elem.intersection(value) == set():
            print(f"Единственный друг, который не взял {' и '.join(elem)} - {key}")


