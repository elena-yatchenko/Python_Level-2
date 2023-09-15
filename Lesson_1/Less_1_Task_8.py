# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

print('Введите количество рядов елки (число от 1 до 9): ')

number = int(input())
n = 1
step = 2

for i in range(1, number+1):
    space = int((step * number - 1 - n) / 2)
    print(' ' * space + '*' * n + ' ' * space)
    n += step
    