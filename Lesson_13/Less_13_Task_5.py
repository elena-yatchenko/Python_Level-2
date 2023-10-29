# Задание №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

import json
from Less_13_Task_3 import LevelError, AccessError


class User:
    
    def __init__(self, name, _id, level):
        self.name = name
        self._id = _id
        self.level = level
        
    def __str__(self):
        return f'Создан пользователь {self.name}, уровень = {self.level}, id = {self._id}'
    
    
class Project(User):
    
    def __init__(*args):
        super.__init__(*args)
        
    
    def create_new(self, file_name):
        self.users = set()
        
        with open(file_name, 'r', encoding='utf-8') as f:
            new_dict = json.load(f)
            for level, row_dict in new_dict.items():
                for _id, name in row_dict.items():
                    user = User(name, _id, level)
                    self.users.add(user)
            return self.users
        
     
       
    def enter(self, file_name, _id):
        for _ in self.create_new(file_name):
            if self._id == _id:
                return self.level
            else:
                raise AccessError(f'Отсутствует пользователь {self.name} с идент. номером {self._id}')


    # def check_level(self)
    
if __name__ == '__main__':
    #all_users = Project.create_new('result_write.json')
    # for user in all_users:
        #print(user._id)
        
    print(Project.enter('result_write.json', 'elena', 224))