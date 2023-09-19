# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

def bonus(amount: int) -> int:
    percent = 3
    summa = amount + (amount * percent / 100)
    print(f'Вам начисляется {percent}% бонуса за пользование картой - {amount * percent / 100} y.e.', end='\n\n')
    
    return summa

def receive_fee(receive_sum: int) -> float:
    percent = 1.5
    fee = receive_sum * percent / 100
    if fee < 30:
        fee = 30
    elif fee > 600:
        fee = 600
    return fee

def rich(amount):
    percent = 10
    if amount > 5000000:
        print(f'Вычитается налог на богатство в размере {(amount * percent / 100)} y.e.')
        amount = amount - (amount * percent / 100)
        print(f'Текущий баланс {amount} y.e.', end='\n\n')
    return amount


print('Приветствие!')
summa = 0
print(f'Текущий баланс {summa} y.e.', end='\n\n')
print('Сумма пополнения и снятия кратны 50 у.е.')
count = 0  # количество операций для начисления бонуса 3%

while True:
    print('Пополнить - 1', 'Снять - 2', 'Выйти - 3', sep='\n')
    select = input('Выберите желаемое действие: ')
    
    if select == '1':
        summa = rich(summa) 
        n = 3
        while n > 0:
            enter = int(input('Введите желаемую сумму пополнения. Сумма должна быть кратна 50 у.е.: '))
            if enter % 50 == 0:
                summa = summa + enter
                count += 1
                print(f'Текущий баланс {summa} y.e.', end='\n\n')
                if count == 3:
                    summa = bonus(summa)
                    count = 0
                print(f'Текущий баланс {summa} y.e.', end='\n\n')
                break
            else:
                print('Сумма должна быть кратна 50. Введите сумму: ')
                n -= 1    
        else:
            print('К сожалению, Вы использовали 3 попытки ввода суммы.')

    elif select == '2':
        summa = rich(summa)
        n = 3
        while n > 0:
            enter = int(input('Введите желаемую сумму снятия. Сумма должна быть кратна 50 у.: '))
            fee = receive_fee(enter)
            if enter > (summa - fee):
                print(f'На счете недостаточно средств ({(summa - fee)}), введите другую сумму', end='\n\n')    
            elif enter % 50 == 0:
                print(f'Комиссия за снятие составляет {receive_fee(enter)} y.e.', end='\n\n')
                summa = summa - enter - fee
                count += 1
                if count == 3:
                    summa = bonus(summa)
                    count = 0
                print(f'Текущий баланс {summa} y.e.', end='\n\n')
                break
            else:
                print('Сумма должна быть кратна 50. Введите сумму: ')
                n -= 1    
        else:
            print('К сожалению, Вы использовали 3 попытки ввода суммы.')

    elif select == '3':
        print('Работа завершена. Заберите Вашу карту', end='\n\n')
        print(f'Текущий баланс {summa} y.e.', end='\n\n')
        quit()

    else:
        print('Некорректный ввод данных. Выберите один из предложенных вариантов')
   


