"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные
в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""

from random import randint

def first_func(func):
    def wrapper(*args):
        if 1 < args[0] < 100 and 1 < args[1] < 10:
            return func(*args)
        return func(randint(1, 100), randint(1, 10))
    return wrapper

@first_func   
def guess(num, count):
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
    guess(55, 2) 