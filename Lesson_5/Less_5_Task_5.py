
# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

my_dig = ['Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else 'FissBuzz' if i % 3 == 0 and i % 5 == 0 else i for i in range(1, 101)]

print(my_dig)


# развернутое решение
fizzbuzz = []
for i in range(1, 101):
    if i % 15 == 0:
        fizzbuzz.append('FizzBuzz')
    elif i % 3 == 0:
        fizzbuzz.append('Fizz')
    elif i % 5 == 0:
        fizzbuzz.append('Buzz')
    else:
        fizzbuzz.append(i)
print(fizzbuzz)