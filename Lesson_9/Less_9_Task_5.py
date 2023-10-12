
"""Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""
import json
from random import randint
import os
from functools import wraps

"""функция логинится???? - посмотреть в записи"""
"""декораторами для сохранения параметров - проверяет есть ли запись в json, считывает существующую инфо, если есть, дополняет и перезаписывает"""
def save_param(func): 
    my_dict = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal my_dict
        #result = func(*args, **kwargs)
        file_name = f'{func.__name__}.json'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file_r:
                my_dict = json.load(file_r)
        my_dict[str(args)] = args
        my_dict.update(**kwargs)
        my_dict['result'] = func(*args, **kwargs)
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(my_dict, file, indent=2, ensure_ascii=False)
        #return result
        # return my_dict 
    return wrapper

""" ○ декоратором контроля значений - если при вызове фунцкии ввели аргументы вне заданных диапазонов, фукнция генерирует свои, в рамках нужных диапазонов"""
def control(func):
    @wraps(func)
    def wrapper(*args):
        if 1 < args[0] < 100 and 1 < args[1] < 10:
            return func(*args)
        return func(randint(1, 100), randint(1, 10))
    return wrapper

"""○ декоратором для многократного запуска - причем запускается работа всех трех декораторов. т.к. вызывая фукнцию, мы вызывыаем их все"""
def repeat(times):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
            
        return wrapper
    return deco

"""запускаются от самого ближнего к нашей фукнции до самого дальнего: save_param, control и после repeat"""
@repeat(3)
@control
@save_param   
def guess(num, count):
    """12345558755"""
    min_limit = 1
    max_limit = num
    number = randint(min_limit, max_limit)
    #print(num)

    attempt = count
    while attempt > 0:
        print('Попытка:', attempt)
        attempt -= 1

        print(f'Введите число от {min_limit} до {max_limit}: ')
        res = int(input())
        if res < min_limit or res > max_limit:
            print('Введите число в указанном диапазоне')
        elif res == number:
            print('Верно!')
            break
        elif res < number:
            print('Больше')
        elif res > number:
            print('Меньше')
        
    else:
        print('Вы исчерпали все попытки, к сожалению')
        # quit()
   

if __name__ == '__main__':
    guess(210, 2)
    
    print(guess.__name__)