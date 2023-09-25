# STRING - СТРОКА как массив данных

""" 
Работа со стороками как со списком:
 * Квадратные скобки []
 - доступ к элементу по индексу
 - срезы строк
#  - метод replace() - заменяет элемент строки на нужный, в итоге получаем новый объект (т.к. объект строка не изменяется)
#  * метод count() - подсчет вхождений элемента
#  * метод index() - индекс первого вхождения элемента
#  * метод find() - индекс первого вхождения элемента
разница index и find: в случае, если искомый элемент отсутствует в строке, find выведет -1, 
а index даст ошибку. Можем использовать любой, в зависимости от наших целей.
#  """

# text = 'Hello world!'
# print(text[6]) # w
# print(text[3:7]) # lo w

# new_txt = text.replace('l', 'L', 2) 
# # replace(что меняем, на что меняем, количество замен). Если количество замен не указываем, то заменяет все найденные
# print(text, new_txt, sep='\n') 
# # Hello world!
# # HeLLo world!

# text = 'Hello world!'
# print(text.count('l')) # 3
# print(text.index('l')) # 2
# print(text.find('l')) # 2
# print(text.find('z')) # -1 (значит, что прошлисьпо строке от начала до конца и указанную букву не нашли)
# print(text.index('z')) # ValueError: substring not found

# text = 'Hello world!'
# print(text[::-1]) # !dlrow olleH - реверс строки

# ФОРМАТИРОВАНИЕ СТРОК

""" 
- через % - старый способ, сохранился в некоторых модулях (например, модуль логирования данных)
- метод format() - строковой метод, заменяющий фигурные скобки на переменные
- f-строка - сочетание неизменного текста и переменных в фигурных скобках 
"""
# name = 'Alex'
# age = 12
# text = 'Меня зовут %s и мне %d лет' % (name, age)
# # s - строка (string), d - число (digit)
# print(text) # Меня зовут Alex и мне 12 лет


# name = 'Alex'
# age = 12
# text = 'Меня зовут {} и мне {} лет'.format(name, age)
# print(text) # Меня зовут Alex и мне 12 лет

# name = 'Alex'
# age = 12
# text = f'Меня зовут {name} и мне {age} лет.' # самый популярный в данное время
# print(text) # Меня зовут Alex и мне 12 лет
# print(f'{{фигурные скобки}} и {{name}}') # {фигурные скобки} и {name}

# ПРОЧИЕ НЮАНСЫ ФОРМАТИРОВАНИЯ

pi = 3.1415
# print(f'Число Пи с точностью 2 знака: {pi:.2f}') # Число Пи с точностью 2 знака: 3.14

""" Здесь : после имени переменной показывает, что ее будем форматировать, .2f - 2 знака
после запятой для вещественного числа (f - float)"""

data = [3254, 43643145320025, 43465474, 2342, 462256, 1747]
# for item in data:
    #print(f'{item:>10}')
    
#       3254
# 436431453200255584
#   43465474
#       2342
#     462256
#       1747
    #print(f'{item:<10}')

# 3254      
# 436431453200255584
# 43465474
# 2342
# 462256
# 1747
    # print(f'{item:^10}')

#    3254   
# 43643145320025
#  43465474
#    2342
#   462256
#    1747

""" >10 значит используем выравнивание по правому краю и правый край начинается 
на расстоянии 10 знаков (если длина элемента больше 10, он вылезает за край) 
<10  - выравнивание по левому краю, отступ 10 знаков
^10 - выравнивание по центру относительно заданого диапазона (середина = 10 / 2)"""

# num = 2 * pi * data[1]
# print(f'{num = :_}') # num = 274_209_882_045_717.1

""" 
num = :_  Т.е. вводим имя переменной, пробел, =, пробел, далее применяетсяформатирование для содержимого 
переменной - это символ _. Т.е. разбиваем число на группы по 3 цифры, разделяя их символом 
подчеркивания (об этом ранее говорили: символ _ позволяет визуально облегчить чтение длинных
чисел, но при этом игнорируется Питоном, т.е. число воспринимается обычным числом)

"""
# num = 274_209_882_045_717.1
# num1 = num
# print(num1) # 274209882045717.1

# СТРОКОВЫЕ МЕТОДЫ

"""
* метод split() - разбивает строку на отдельные элементы

* метод join() - формирует строку из отдельных элементов различных коллекций
* методы upper(), lower(), title(), capitalize() - изменение регистра

* методы startswith() и endswith() - проверка на совпадение с началом или концом строки

"""
# SPLIT()

# link = 'http://Users/User/Documents/Данные компа/Study/Python_Level-2/'
# urls = link.split('/')
# print(urls) 
# # ['http:', '', 'Users', 'User', 'Documents', 'Данные компа', 'Study', 'Python_Level-2', '']

# a,b,c = input('Введите 3 числа через пробел: ').split()
# print(c,b,a) # 75 8 51

# a, b, c, *_ = input("Введите не менее трех чисел через пробел: ").split()
# print(c,b,a) 
# # Введите не менее трех чисел через пробел: 25 87 8 9 87 44 
# # 8 87 25

# JOIN()

# data = ['http:', '', 'Users', 'User', 'Documents', 'Данные компа', 'Study', 'Python_Level-2', '']
# url = '/'.join(data) - тут может быть не только список, другие итерируемые объекты тоже
# print(url) # http://Users/User/Documents/Данные компа/Study/Python_Level-2/
# url = ' '.join(data)
# print(url) # http:  Users User Documents Данные компа Study Python_Level-2 

# upper(), lower(), title(), capitalize()
"""
Эти методы работают только для тех символов кодировки, которые воспринимаются как текст и 
варианты начертания Строчная и Прописная (т.е. представлены в 2 вариантах). Иначе метод ничего не поменяет
"""

# text = 'однажды в СТУДЕНУЮ зИмнЮЮ ПоРУ'
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

# ОДНАЖДЫ В СТУДЕНУЮ ЗИМНЮЮ ПОРУ
# однажды в студеную зимнюю пору
# Однажды В Студеную Зимнюю Пору
# Однажды в студеную зимнюю пору

# startswith() и endswith() - возвращают True или False

text = 'однажды в СТУДЕНУЮ зимнюю ПоРУ'
print(text.startswith('Однажды')) # False
print(text.startswith('однажды')) # True
print(text.endswith('зимнюю', 0, -5)) # True  - тут мы проверяли от 0 до -5 индекса, т.е. исключили последние 5 символов: пробел и слово "ПоРу"

""" 
В данных методах могут быть дополнительные аргументы: индекс старта и индекс стопа
"""

                  