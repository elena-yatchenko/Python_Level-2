# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и 
# знаменателем. Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.
# numerator - числитель, denominator - знаменатель

import fractions

numer1, denom1 = map(int, input('Введите дробь 1: ').split("/")) # распаковка
numer2, denom2 = map(int, input('Введите дробь 2: ').split("/"))
# split разбивает введенную в виде строки запись (3/4) по делителю "/" в список из отдельных элементов 
# print(input('Введите дробь 1: ').split("/"))

f1 = fractions.Fraction(numer1, denom1)
f2 = fractions.Fraction(numer2, denom2)
print(f1 + f2, f1 * f2)

def common_denom (denom1: int, denom2: int) -> int:
    if denom1 >= denom2:
        number = denom1
        step = denom1
    else:
        number = denom2
        step = denom2
    while number:
        if number % denom1 == 0 and number % denom2 == 0:
            com_denom = number
            break
        else:
            number += step
    return com_denom


def reduction(num, den):
    if num <= den:
        n = num
    else:
        n = den
    while n:
        if num % n == 0 and den % n == 0:
            num = int(num / n)
            den = int(den / n)
            break
        else:
            n -= 1
    return num, den

# случай равенства знаменателей можно было не включать в функцию, но добавила, чтобы не вносить это условие потом при дальнейшем решении

sum_denom = common_denom(denom1, denom2)
sum_num = (sum_denom / denom1 * numer1) + (sum_denom / denom2 * numer2)
mult_den = denom1 * denom2
mult_num = numer1 * numer2 

s_num, s_den = reduction(sum_num, sum_denom)
m_num, m_den = reduction(mult_num, mult_den)
 
print(f'Сумма введенных дробей = {int(s_num)}/{int(s_den)}')
print(f'Произведение введенных дробей = {int(m_num)}/{int(m_den)}')   

          
# Код, конечно, написан на примитивном уровне, сама понимаю. 
# Но я нуля учусь, нет базы и опыта программирования. 
# Зато работает вроде :)))
            
