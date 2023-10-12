
"""
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""

from random import randint


def first_func(num, count):
    def second_func():
        min_limit = 0
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
    return second_func

if __name__ == '__main__':
    result = first_func(75, 5)() 
    result()  
    

# def first_func(num, count):
#     def second_func():
#         r = randint(1, num)
#         print(r)
#         for attempt in range(count):
#             guess = int(input(f"Попытка №{attempt + 1}: "))

#             if guess < r:
#                 print("Загаданное число больше.")
#             elif guess > r:
#                 print("Загаданное число меньше.")
#             else:
#                 print("Поздравляю! Вы угадали число!")
#                 break
#         else:
#             print("Вы исчерпали все попытки. Загаданное число было:", r)

#     return second_func


# if __name__ == '__main__':
#     result = first_func(75, 5)
#     result()