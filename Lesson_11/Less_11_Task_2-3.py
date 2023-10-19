"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
    📌 При создании нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списков-архивов
    
    📌 list-архивы также являются свойствами экземпляра
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
        
example1 = Archive(2, 'two')
example2 = Archive(4, 'four')

# print(Archive.my_list)
# print(example1.my_list)
# print(example2.my_list)
# print(Archive.my_list)

help(Archive)