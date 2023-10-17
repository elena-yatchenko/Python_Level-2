# Лотерея Класс

# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

# Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать 
# числа из вашего билета из list1 со списком выпавших чисел list2

# Пример входных данных:

# list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
# list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

# game = LotteryGame(list1, list2)
# matching_numbers = game.compare_lists()

# Пример выходных данных:

# Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
# Количество совпадающих чисел: 7

class LotteryGame:
    
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        
    
    def compare_lists(self):
        result_list = list()
        for number in self.list1:
            if number in self.list2:
                result_list.append(number)
        if result_list:
            print(f'Совпадающие числа: {result_list}')
            print(f'Количество совпадающих чисел: {len(result_list)}')
        else: 
            print('Совпадающих чисел нет.')

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]  
     
game = LotteryGame(list1, list2)
                
matching_numbers = game.compare_lists()
    





# РЕШЕНИЕ СИСТЕМЫ

class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        matching_numbers = []  # Инициализируем список для совпадающих чисел

        for num1 in self.list1:
            if num1 in self.list2:
                matching_numbers.append(num1)
        if matching_numbers:
            print("Совпадающие числа:", matching_numbers)
            print("Количество совпадающих чисел:", len(matching_numbers))
        else:
            print("Совпадающих чисел нет.")

        return matching_numbers
