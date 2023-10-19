"""📌 Доработаем класс Архив из задачи 2.
📌 Добавьте методы представления экземпляра для программиста
и для пользователя.
"""

class Archive:
    """список атрибутов"""
    my_list = []
    
    def __new__(cls, *args):
        instance = super().__new__(cls)
        instance.my_list.append(args)
        return instance
    
    def __init__(self, number, text):
        self.number = number
        self.text = text
        
    def __str__(self):
        return f'Получен экземпляр с атрибутами {self.number} и {self.text}, лист-архив = {self.my_list}'
    
    def __repr__(self):
        return f'Archive({self.number, self.text})'
        
example1 = Archive(2, 'two')
example2 = Archive(4, 'four')

print(example1)
print(f'{example2 = }')

# print(Archive.my_list)
# print(example1.my_list)
# print(example2.my_list)
# print(Archive.my_list)

# help(Archive)