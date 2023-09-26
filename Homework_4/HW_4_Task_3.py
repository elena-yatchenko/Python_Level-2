# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# ДОБАВЛЕНО СОХРАНЕНИЕ/ЧТЕНИЕ ОСТАТКА ИЗ ФАЙЛА + СПИСОК ОПЕРАЦИЙ

import os 

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

def import_data(amount: int, file_name:str) -> int:
    path_sourse = os.path.join ('.', 'Homework_4', file_name)
    with open(path_sourse, 'r', encoding='utf-8') as sourse:
        for elem in sourse:
            amount = amount + int(elem)
    return amount

def export_data(amount: int, file_name:str) -> None:
    path_destination = os.path.join(".", "Homework_4", file_name)
    with open(path_destination, "w", encoding="utf-8") as data_destination:
        data_destination.write(str(summa))
        return
    
print('Приветствие!')
summa = 0
file_name = 'Amount.csv'
summa = import_data(summa, file_name)
print(f'Текущий баланс {summa} y.e.', end='\n\n')
print('Сумма пополнения и снятия кратны 50 у.е.')
count = 0  # количество операций для начисления бонуса 3%
oper_list = []

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
                oper_list.append('+' + str(enter))
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
                oper_list.append('-' + str(enter))
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
        print('Работа завершена. Заберите Вашу карту', end='\n')
        print(f'Текущий баланс {summa} y.e.', end='\n')
        print(f'Cписок операций поступления/снятия денег: {", ".join(oper_list)}')
        export_data(summa, file_name)
        quit()

    else:
        print('Некорректный ввод данных. Выберите один из предложенных вариантов')
   
   
   # Cписок операций поступления/снятия денег: +250, -200, +4000