# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

# def gen(n):
#     count = 0
#     start = 2
#     while count < n:
#         for i in range(2, start):
#             if start % i == 0:
#                 break
#         else: 
#             count +=1
#             yield start
#         start += 1
        
# for i in gen(10):
#     print(i)
    
                
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def gen(n):
    number = 2
    count = 0
    while count < n:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number
            count += 1
        number +=1

for i in gen(10):
    print(i)