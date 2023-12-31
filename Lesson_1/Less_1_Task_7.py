# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

min_limit = 1
max_limit = 999

while True:
    print(f'Введите число от {min_limit} до {max_limit}: ')
    num = int(input())
    if num < min_limit or num > max_limit:
        print('Неправильно введено число, вводите новое число в заданном диапазоне')
    else:
        break


if 1 <= num <= 9:
    print(f'Введена цифра {num}', f'Квадрат {num} равен {num ** 2}', sep= '\n')
elif 10 <= num <= 99:
    num1 = num // 10
    num2 = num % 10
    print(f'Введено двузначное число {num}', f'Произведение цифр {num} равно {num1 * num2}', sep='\n')
elif 100 <= num <= 999:
    num1 = num // 100
    num2 = num % 100 // 10
    num3 = num % 10
    if num3 == 0:
        print(f'Введено трехзначное число {num}', f'Зеркальное отображение {num} равно {str(num2) + str(num1)}', sep='\n')
    else:
        print(f'Введено трехзначное число {num}', f'Зеркальное отображение {num} равно {str(num3) + str(num2) + str(num1)}', sep='\n')
