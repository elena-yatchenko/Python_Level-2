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
    
    def to_dict(self): 
        return {'name': self.name, 'id': self._id, 'level': self.level}
    
    def __eq__(self, other: object) -> bool:
        return self.name == other.name and self._id == other._id


class Project():

    #file_name = 'new_json.json'

    def __init__(self):
        self.lst_users = self.read_json()

    '''метод считывания данных (загрузка данных (функция из задания 4))'''
    def read_json(self):
        lst_users = []
        store_id = set()
        try:
            with open('new_json.json', 'r', encoding='utf-8') as f:
                user_data = json.load(f)
                for user in user_data:
                    lst_users.append(User(user['name'], user['id'], user['level']))
                    store_id.add(user['id'])
        except FileNotFoundError as e:
            print(e)
        return lst_users

    """вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
    магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение
    доступа. А если пользователь есть, получите его уровень из множества пользователей."""
    """т.е. это аутентификация того пользователя, который будет потом добавлять остальных (через цикл while), он должен 
    обязательно быть уже в списке"""

    def auth_user(self):
        name = input('Введите имя: ')
        _id = input('Введите id: ') 
        level  = None
        my_user = User(name, _id, level)
        for user in self.lst_users:
            if my_user == user:
                my_user.level = user.level
                return my_user
        raise AccessError(_id)

    """добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа."""   
    def add_user(self, creator: User, creature: User):
        if int(creator.level) > int(creature.level):
            raise LevelError(creature.level)
        self.lst_users.append(creature)
        return self.lst_users
    
    def save_json(self):
        with open('new_json.json', 'w', encoding='utf-8') as f:
            """генерируем список словарей по данным пользователей из списка"""
            res_users = [i.to_dict() for i in self.lst_users]
            """т.к. i сейчас  - это объект (экземпляр класса User), то можем обратиться через точечную нотацию к методу данного класса"""
            json.dump(res_users, f, indent=2)
    
project = Project()
my_user = project.auth_user()

"""Собирающий блок инфо для add_user"""   

while True:
    name = input('Name: ')
    if name == 'help':
        break
    if not name:
        print('Имя не должно быть пустым')
        continue
    _id = (input('id: '))
    level = (input('level: '))
    if int(level) not in range(1, 8):
        print('Уровень доступа должен быть от 1 до 7')
        continue
        
    project.add_user(my_user, User(name, _id, level))

project.save_json()







# class User:
    
#     def __init__(self, name, _id, level):
#         self.name = name
#         self._id = _id
#         self.level = level
        
#     def __str__(self):
#         return f'Создан пользователь {self.name}, уровень = {self.level}, id = {self._id}'
    
    
# class Project(User):
    
#     def __init__(*args):
#         super.__init__(*args)
        
    
#     def create_new(self, file_name):
#         self.users = set()
        
#         with open(file_name, 'r', encoding='utf-8') as f:
#             new_dict = json.load(f)
#             for level, row_dict in new_dict.items():
#                 for _id, name in row_dict.items():
#                     user = User(name, _id, level)
#                     self.users.add(user)
#             return self.users
        
     
       
#     def enter(self, file_name):
#         for _ in self.create_new(file_name):
#             if self._id == _id:
#                 return self.level
#             else:
#                 raise AccessError(f'Отсутствует пользователь {self.name} с идент. номером {self._id}')


#     # def check_level(self)
    
# if __name__ == '__main__':
#     #all_users = Project.create_new('result_write.json')
#     # for user in all_users:
#         #print(user._id)
        
#     print(Project.enter('result_write.json', 'elena', 224))