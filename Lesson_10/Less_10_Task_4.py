"""
Создайте класс Сотрудник.
📌 Воспользуйтесь классом человека из прошлого задания.
📌 У сотрудника должен быть:
    ○ шестизначный идентификационный номер
    ○ уровень доступа вычисляемый как остаток от деления
      суммы цифр id на семь
"""
from Less_10_Task_3 import Person
import random

# class Person():

#     def __init__(self, name, surname, father_name, age):
#         self.name = name
#         self.surname = surname
#         self.father_name = father_name
#         self.__age = age
        
class Employee(Person):
    
    def __init__(self, name, surname, father_name, age, id_number):
        super().__init__(name, surname, father_name, age)
        if len(str(id_number))!= 6:
            self.id_number = random.randint(100_000, 999_999)
        else:
            self.id_number = id_number
        
    def secure_level(self):
        return sum((int(i) for i in str(self.id_number))) % 7
        
user = Employee('Елена', 'Ятченко', 'Михайловна', 36, 1265478) 

print(user.secure_level()) 
  