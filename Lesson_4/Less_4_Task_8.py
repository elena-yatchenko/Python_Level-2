# Задание №8

# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

text = 'test_name' 
numbers = [2, 5, 8, 1.5]
tuples = (1, 78, 85)
s = 5555
s_name = '663311'
dict_s = dict(one=1, three=3, five=5)
names = 'OOOIIIAAA'

# glob_dict = globals() # словарь глобальных переменных (переменная-значение)
# print(glob_dict)
# work_dict = dict(list(filter(lambda x: not x[0].startswith('__'), globals().items()))) # убираем из словаря дандер-методы
# print(work_dict)

def rewrite(func):
    work_dict = dict(list(filter(lambda x: not x[0].startswith('__'), globals().items())))
    result_dict = {}
    for variable, meaning in work_dict.items():
        if variable.endswith('s') and len(variable) > 1:
            result_dict[variable[:len(variable)-1]] = meaning
            result_dict[variable] = None
        else:
            result_dict[variable] = work_dict[variable]
    return result_dict


print(rewrite(globals()))

# {'text': 'test_name', 'number': [2, 5, 8, 1.5], 'numbers': None, 'tuple': (1, 78, 85), 
# 'tuples': None, 's': 5555, 's_name': '663311', 'dict_': {'one': 1, 'three': 3, 'five': 5}, 
# 'dict_s': None, 'name': 'OOOIIIAAA', 'names': None, 'rewrite': <function rewrite at 0x0000026BE96719E0>}