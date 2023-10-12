
"""
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""


from random import randint


def first_func(func):
    def wrapper(*args):
        if 1 < args[0] < 100 and 1 < args[1] < 10:
            return func(*args)                          # при обращении к func (через if или без), это вызывает следующий декоратор (в нашем случае @repeat)
        return func(randint(1, 100), randint(1, 10))
    return wrapper

def repeat(times):
    def deco(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs) # когда дергаем функцию func, нас перебрасывает к следующему декоратору, пока не дойдем до последнего. Здесь repeat последний, так что
                # тут уже будет работать сама func = guess. Причем повторяться будет вся обертка, включая first_func 
            
        return wrapper
    return deco

"""каждый следующий декоратор получает в работу результат работы предыдущего"""
@repeat(3)
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
    guess(120, 2)
    