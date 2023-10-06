# 'eyuioa'
# 'qwrtpsdfghjklzxcvbnm'
# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.

import random

# glas = 'eyuioa'
# sogl = 'qwrtpsdfghjklzxcvbnm'
# answer= []
# num_it = random.randint(4, 7)
# for i in range(random.randint(4, 7)):
#     answer.extend([random.choice(glas), random.choice(sogl)])
# print(''.join(answer).title()[:num_it])
#def name_gen(file: str):
    
    # def add_text(count: int, file: str):
    # with open(file, 'a', encoding='utf-8') as data:
    
    
def num_of_dev(file: str, count: int):
    glas = 'eyuioa'
    sogl =  'qwrtpsdfghjklzxcvbnm'
    
    with open(file, 'a', encoding='utf-8') as data:
        for j in range(count):  # количество генерируемых записей (строк с псевдоименем)
            num_it = random.randint(4,7) # генерируем количество букв в имени
            answer = []
            for i in range(4):
                answer.extend([random.choice(glas),random.choice(sogl)]) # добавляем по 2 рандомные буквы, гласную и согласную
            print("".join(answer).title()[:num_it], file=data) # срезом [:num_it] берем только 4-7 первых букв из полученной строки

# задавая в print атрибут file записываем данные сразу в наш файл


if __name__ == '__main__':
    num_of_dev('text_name.txt',8)

