# Задание №4
# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json

class User:
    
    """Конструктор экземпляра, который хранит в себе атрибуты экзмепляра"""
    def __init__(self, name, _id, level):
        self.name = name
        self._id = _id
        self.level = level
        
    def __str__(self):
        return f'Создан пользователь {self.name}, уровень = {self.level}, id = {self._id}'
    
    """метод класса, который переводит считываемую информацию (атрибуты экземпляра) в словарь"""
    def to_dict(self): 
        return {'name': self.name, 'id': self._id, 'level': self.level}
    
store_id = set()
lst_users = []

while True:
    name = input('Name: ')
    if name == 'help':
        break
    if not name:
        print('Имя не должно быть пустым')
        continue
    _id = (input('id: '))
    if _id in store_id:
        print('Данный пользователь с {_id} id уже добавлен')
        continue
    level = (input('level: '))
    if level in range(1, 8):
        print('Уровень доступа должен быть от 1 до 7')
        continue
        
    store_id.add(_id)
    lst_users.append(User(name, _id, level))

'''передаем функции имя файла и список экземпляров класса User'''    
def save_json(file_name, users):
    with open(file_name, 'w', encoding='utf-8') as f:
        """генерируем список словарей по данным пользователей из списка"""
        res_users = [i.to_dict() for i in users]
        """т.к. i сейчас  - это объект (экземпляр класса User), то можем обратиться через точечную нотацию к методу данного класса"""
        json.dump(res_users, f, indent=2)
        
save_json('new_json.json', lst_users)


        







"""мое решение, тоже само по себе работает. """

# import os


# def create_user(file_name):
#     store_id = set()
#     if os.path.exists(file_name): # если такой файл уже существует, открываем его на чтение, загружаем существующий словарь 
#         # с данными и с ним дальше будем работать
#         with open(file_name, 'r', encoding='utf-8') as f:
#             new_dict = json.load(f)
#             for _, value in new_dict.items():
#                 store_id.update(value.keys()) 
# # если файл существует, значит там уже есть сет с сохраненными id, которые являются ключами вложенного словаря, 
# # апдейтим(выгружаем) их, чтобы дальше проверять уникальность следующих id
#     else:   
#         new_dict = {str(i): {} for i in range(1, 8)}
        
#     while True:
#         name = input('Name: ')
#         if name == 'help':
#             break
#         if not name:
#             print('Имя не должно быть пустым')
#             continue
#         _id = (input('id: '))
#         if _id in store_id:
#             print('Данный пользователь с {_id} id уже добавлен')
#             continue
#         level = (input('level: '))
#         if level not in new_dict: # проверяет, есть ли такой ключ в нашем словаре, который задан с ключами 1 - 7
#             print('Уровень доступа должен быть от 1 до 7')
#             continue
            
#         store_id.add(_id)
#         new_dict[level].update({_id: name})
#         print(new_dict)                   
            
#         with open('result_task2.json', 'w', encoding='utf-8') as f:
#             json.dump(new_dict, f, indent=2, ensure_ascii=False)
            
# class User:
    
#     def __init__(self, name, _id, level):
#         self.name = name
#         self._id = _id
#         self.level = level
        
#     def __str__(self):
#         return f'Создан пользователь {self.name}, уровень = {self.level}, id = {self._id}'
        
#     def create_new(file_name):
#         users = set()
#         with open(file_name, 'r', encoding='utf-8') as f:
#             new_dict = json.load(f)
#             for level, row_dict in new_dict.items():
#                 for _id, name in row_dict.items():
#                     user = User(name, _id, level)
#                     users.add(user)
#             return users
                
# # result_write.json

# if __name__ == '__main__':
#     all_users = User.create_new('result_write.json')
#     for user in all_users:
#         print(user)
#         print(user._id)
        

                    
        
 