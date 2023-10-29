# Задание №3
# Создайте класс с базовым исключением и дочерние классы-исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyException(Exception):
    pass

class LevelError(MyException):
    
    def __init__(self, value):
     self.value = value
     
    def __str__(self):
        return f'Полученный уровень {self.value} не соответствует требуемому'
    
class AccessError(MyException):
     
    def __init__(self, value):
        self.value = value 
        
    def __str__(self):
        return f'Уровень доступа {self.value} не соответсвует требуемому'
    
     
    