# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT) 

from random import randint

min_limit = 0
max_limit = 1000
num = randint(min_limit, max_limit)
print(num)

attempt = 10
while attempt > 0:
    print('Попытка:', attempt)
    attempt -= 1

    print(f'Введите число от {min_limit} до {max_limit}: ')
    res = int(input())
    if res < min_limit or res > max_limit:
        print('Введите число в указанном диапазоне')
    elif res == num:
        print('Верно!')
        break
    elif res < num:
        print('Больше')
    elif res > num:
        print('Меньше')
    
else:
    print('Вы исчерпали все попытки, к сожалению')
    quit()




