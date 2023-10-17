"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
📌 У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
📌 Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст."""

class Person():

    def __init__(self, name, surname, father_name, age):
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.__age = age
        
    def birthday(self):
        self.__age += 1
        
    def full_name(self):
        return f'{self.surname} {self.name} {self.father_name}'
    
    def get_curr_age(self):
        return self.__age
    
p1 = Person('Елена', 'Ятченко', 'Михайловна', 38)
p1.birthday()
print(p1.get_curr_age())
print(p1.full_name())


if __name__ == "__main__":
    p1 = Person('Елена', 'Ятченко', 'Михайловна', 38)
    p1.birthday()
    print(p1.get_curr_age())
    print(p1.full_name())