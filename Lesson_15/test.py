import argparse
parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float,
nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'Получили экземпляр Namespace: {args = }')
print(f'У Namespace работает точечная нотация: {args.numbers = }')
print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')

# запрос - python test.py 42 3.14 73

# полученные результаты

# Получили экземпляр Namespace: args = Namespace(numbers=[42.0, 3.14, 73.0])
# У Namespace работает точечная нотация: args.numbers = [42.0, 3.14, 73.0]
# Объекты внутри могут быть любыми: args.numbers[1] = 3.14

# python Less_15_Task_5.py '1-й четверг ноября'