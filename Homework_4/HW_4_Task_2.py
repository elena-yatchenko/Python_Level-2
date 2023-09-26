# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def new_dict(**qwargs):
    my_dict = {}
    for key, value in qwargs.items():
        if hash(value):
            my_dict[value] = key
        else: 
            my_dict[value] = str(key)
    return my_dict

print(new_dict(int=2, float=3.54, bool=True))

# list=[5, 2, 5], set=(1, 1, 5)