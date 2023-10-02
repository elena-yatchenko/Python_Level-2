# ВСТРОЕННЫЕ МОДУЛИ "ИЗ КОРОБКИ"

# МОДУЛЬ SYS и запуск скрипта с параметрами - работа с КОМАНДНОЙ СТРОКОЙ (ИЛИ В КОНСОЛИ)

"""
Модуль sys обеспечивает доступ к некоторым переменным(параметрам), используемым или 
поддерживаемым интерпретатором, а также к функциям, тесно взаимодействующим
с интерпретатором.

!!! Программа, модуль, файл, скрипт - это по сути СИНОНИМЫ.
Когда мы открываем командную строку, пишем python, дальше пишем название файла, 
то мы запускаем этот файл (скрипт)

Код файла: 

from sys import argv

print('start')
print(argv)
print('stop')

Команда запуска: 

python script.py -d 42 -s "Hello world!" -k 100
"""

# В терминале переходим в ту папку, где наши файлы - дальше в консоль (или делать это в командной строке)
# (пишем python) и имя файла (запуск его)

# PS D:\My Documents\docs\Geek Brains\Python_Level-2> cd .\Lecture_6_Modules
# PS D:\My Documents\docs\Geek Brains\Python_Level-2\Lecture_6_Modules> python .\modules_01.py 42
# start
# stop 
"""заданная переменная 42 не вышла
Теперь в другом файле используем импорт from sys import argv
и вызываем файл с указанием переменных
"""
# PS D:\My Documents\docs\Geek Brains\Python_Level-2\Lecture_6_Modules> python .\modules_02.py 42 'Hello world!' hi, how are you 67
# start
# ['.\\modules_02.py', '42', 'Hello world!', 'hi', 'how', 'are', 'you', '67']
# stop

"""
На выходе получаем список с переданными переменными
!!! Элементом списка с индексом [0] указано имя файла вызванного файла (.\\modules_02.py)
Строка, которая была передана в кавычках, попала в одну ячейку, как единый объект. 
Та, что без кавычек, разбилась на элементы по пробелу как разделителю 
Числа при такой передаче воспринимаются как строки, т.е. нужно использовать int
для перевода в число
"""

# МОДУЛ RANDOM

"""
Модуль используется для ГЕНЕРАЦИИ ПСЕВДОСЛУЧАЙНЫХ ЧИСЕЛ. 

Псевдо, т.к. внутри модуля есть таблица с числами, т.е. числа случайные, но 
заранее определены. И внутри модуля есть алгоритм, который определяет как их 
"случайно" генерировать. 

- random() -генерирует псевдослучайные числа в диапазоне [0, 1) (0 включен, 1 - нет)

- seed(a = None, version=2) -инициализирует генератор. Если значение "а" не указано, 
для инициализации используется текущее время ПК

- getstate() - возвращает объект с текущим состоянием генератора

- setstate(state) - устанавливает новое состояние генератора, принимая 
на вход объект, возвращенный функцией getstate()
"""

# import random as rnd

# print(f'{rnd.random() = }') # rnd.random() = 0.19233479389341168
# rnd.seed(42) # задал начальную точку отсчета
# state = rnd.getstate()
# print(f'{state = }')
# print(f'{rnd.random() = }') # rnd.random() = 0.6394267984578837
# print(f'{rnd.random() = }') # rnd.random() = 0.025010755222666936
# rnd.setstate(state) # вернулись опять к состоянию state, в результате сгенерированные числа будут теми же, что были
# print(f'{rnd.random() = }') # rnd.random() = 0.6394267984578837
# print(f'{rnd.random() = }') # rnd.random() = 0.025010755222666936

""" Т.е. можем "угадывать" случайные числа. Чтобы этого не просиходило, либо 
ничего не задаем в seed(), либо задаем текущее время в секундах """

# НЕСКОЛЬКО ЧАСТО ИСПОЛЬЗУЕМЫХ ФУНКЦИЙ RANDOM

"""
- randint(a, b) - целое число от a до b

- uniform(a, b) - вещественное число от a до b

- choice(seq) - случайный элемент последовательности

- randrange(start, stop[, step]) - число из диапазона

- shuffle() - перемешиваем коллекцию х in place

- sample(population, k, *, weight=None) - выборка в k элементов из 
population (уникальных)

- choices((population, k, *, weight=None)- выборка в k элементов из 
population (повтоярющихся). 
"""

# import random as rnd

# START = -100
# STOP = 1_000
# STEP = 10
# data = [2, 4, 6, 8, 42, 73]

# print(f'{rnd.randint(START, STOP) = }') # 788
# print(f'{rnd.uniform(START, STOP) = }') # 487.3201875992388
# print(f'{rnd.choice(data) = }') # 2
# print(f'{rnd.randrange(START, STOP, STEP) = }') # 320

# print(f'{data =}') # data =[2, 4, 6, 8, 42, 73]
# rnd.shuffle(data)
# print(f'{data =}') # data =[6, 2, 4, 8, 42, 73]

# print(f'{rnd.sample(data, 3) = }') # [8, 42, 4]
# print(f'{rnd.sample(data, 3, counts=[1, 2, 1, 1, 1, 100]) = }') # [73, 73, 73]
""" 
weight принимает на вход список, который должен содержать столько же элементов, 
сколько в нашем преедаваемом списке data. Каждый элемент списка counts
говорит нам, сколько должен повторяться каждый из элементов 
передаваемого в метод списка (data в нашем случае.
Т.е. теперь мы выбираем из списка data(измененного после shuffle), в котором 
100 раз повторяется 73, 2 раз повтоярется 2-ка, и по 1 разу все остальные элементы.
Т.е. там уже не 6, а 106 элементов (100 + 2 + 1 + 1 + 1 + 1)
И из этого списка мы просим принести 3 любых элемента случайным образом.
count - относительный вес элемента в списке для выбора (более высокая степень
вероятности его выбора). Если count=None, элементы отбираются в итоговую
последовательность с равной вероятностью
"""

# TEST

# import random
# from sys import argv

# print(random.uniform(int(argv[1]), int(argv[2])))
# print(random.randrange(int(argv[1]), int(argv[2]), int(argv[1])))
# print(random.sample(range(int(argv[1]), int(argv[2]), int(argv[1]), 10)))

# script запущен командой: python main.py 10 1010


