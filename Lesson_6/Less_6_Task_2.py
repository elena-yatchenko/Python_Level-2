# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных
# границах и пользователь должен угадать
# его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.


from random import randint

# LOWER_LIMIT = 0
# UPPER_LIMIT = 1000
# MAX_ATTEMPTS = 10
# one = 1
# guess = 0

# num = randint(LOWER_LIMIT, UPPER_LIMIT)

# print("Угадайте число от 0 до 1000. У вас 10 попыток.")

# def func(a, b, c):
#     for attempt in range(MAX_ATTEMPTS):
#         guess = int(input(f"Попытка №{attempt + one}: "))

#         if guess < num:
#             print("Загаданное число больше.")
#         elif guess > num:
#             print("Загаданное число меньше.")
#         else:
#             print("Поздравляю! Вы угадали число!")
#             break
#     else:
#         print("Вы исчерпали все попытки. Загаданное число было:", num)
        

def func(a, b, c):
    num = randint(a, b)
    for attempt in range(c):
        guess = int(input(f"Попытка №{attempt + 1}: "))

        if guess < num:
            print("Загаданное число больше.")
        elif guess > num:
            print("Загаданное число меньше.")
        else:
            print("Поздравляю! Вы угадали число!")
            return True
    print("Вы исчерпали все попытки. Загаданное число было:", num)
    return False   

if __name__ == '__main__':
    print(func(1, 10, 5)) 