"""
Создайте класс Моя Строка, где:
    будут доступны все возможности str
    дополнительно хранятся имя автора строки и время создания (time.time)
instance = super().__new__(cls, *args, **kwargs)
"""
from datetime import datetime

class MyStr(str):
    
    def __new__(cls, name, text='lesson'):
        instance = super().__new__(cls, name)
        instance.name = name
        instance.text = text
        instance.my_time = datetime.today()
        return instance
    
  
    def __str__(self):
        return f'{self.text} (Автор текста: {self.name}, время: {self.my_time})'
    

    
str1 = MyStr('Elena', 'test text')
# print(str1.my_time)
# print(str1.name)
# print(str1.text)
print(str1)

        
    