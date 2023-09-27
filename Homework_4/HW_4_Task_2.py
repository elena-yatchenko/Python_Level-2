# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def new_dict(**qwargs):
    my_dict = {}
    for key, value in qwargs.items():
        if isinstance(value, int|float|str|tuple|bool):
            my_dict[value] = key
        else: 
            my_dict[str(value)] = key
    return my_dict

print(new_dict(int=2, float=3.54, list=[5, 2, 5], bool=True, set=(1, 1, 5)))

# {2: 'int', 3.54: 'float', '[5, 2, 5]': 'list', True: 'bool', (1, 1, 5): 'set'}