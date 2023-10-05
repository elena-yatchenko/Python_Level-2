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
    
    
def num_of_dev(file: str,count: int):
    glas = 'eyuioa'
    sagl =  'qwrtpsdfghjklzxcvbnm'
    
    with open(file, 'a', encoding='utf-8') as data:
        for j in range(count):
            num_it = random.randint(4,7)
            answer = []
            for i in range(random.randint(4,7)):
                answer.extend([random.choice(glas),random.choice(sagl)])
            print("".join(answer).title()[:num_it],file=data)



if __name__ == '__main__':
    num_of_dev('text_name.txt',8)

