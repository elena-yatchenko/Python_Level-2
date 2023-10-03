# вызываем созданный модуль из задачи 2

# from Less_6_Task_2 import func

# print(func(1, 7, 3))

# вызываем модуль из задачи 3

from Less_6_Task_3 import func as f2
from sys import argv

print(f2(*[int(i) for i in argv[1:]]))

# Передача параметров
# PS C:\Users\User\Documents\PC_Data\Study\Python_Level-2\Lesson_6> python .\Less_6_Task_2_copy.py 60 70 3
# Попытка №1: 65
# Загаданное число больше.
# Попытка №2: 67
# Загаданное число больше.
# Попытка №3: 69
# Загаданное число меньше.
# Вы исчерпали все попытки. Загаданное число было: 68
# False