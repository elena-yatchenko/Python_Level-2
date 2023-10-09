# JSON
# в питоне модуль - import json
"""
СЕРИАЛИЗАЦИЯ - процесс преобразования объекта в поток байтов для сохранения или передачи в память, базу данных или файл. 
ДЕСЕРИАЛИЗАЦИЯ - восстановление объктов из байт, сохранение которых было произведено ранее. 
Процедура выгрузки "зафиксированной" информации пользователем
"""

"""
JSON - популярный формат передачи текстовых данных, по структуре схож со словарем в питоне
"""

# ЧТЕНИЕ JSON в Python: LOAD() - для объекта, LOADS() - для строк
# import json

# with open('user.json', 'r', encoding='utf-8') as f:
#     json_file = json.load(f)

# print(f'{type(json_file) = }\n{json_file} = ')
# print(f'{json_file["name"] = }')
# print(f'{json_file["adress"]["geo"] = }')
# print(f'{json_file["email"] = }')

# # type(json_file) = <class 'dict'>
# # {'id': 2, 'name': 'Erwin Howell', 'username': 'Antonette', 'email': ['shanna@malissa.tv', 'antonette@howel.com'], 'adress': {'street': 'Victor Plains', 'city': 'Visoky', 'zipcode': '90666-7771', 'geo': {'lat': '-43.9509', 'lng': '-34.4618'}}, 'phone': '010-962-6593', 'company': {'name': 'Deckow-Cruist', 'catchPhrase': 'Proactive didact'}} =
# # json_file["name"] = 'Erwin Howell'
# # json_file["adress"]["geo"] = {'lat': '-43.9509', 'lng': '-34.4618'}
# # json_file["email"] = ['shanna@malissa.tv', 'antonette@howel.com']

# Если json в виде строки: 

# import json

# json_text = """[
#         {
#             "userID": 1,
#             "id": 9, 
#             "title": "Lorem Ipsum has been the industry's standa"   
#         },
#         {
#             "userID": 1,
#             "id": 10, 
#             "title": "when an unknown printer took" 
#         }, 
#         {
#             "userID": 2,
#             "id": 11, 
#             "title": "classical Latin literature from 45 BC" 
#         },
#         {
#             "userID": 2,
#             "id": 12, 
#             "title": "cites of the word in" 
#         }       
# ]"""
         
# print(f'{type(json_text) = }\n{json_text = }')
# json_list = json.loads(json_text)
# print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }')

# # type(json_text) = <class 'str'>
# # json_text = '[\n        {\n            "userID": 1,\n            "id": = 9, \n            "title": "Lorem Ipsum has been the industry\'s standa"   \n        },\n        
# # {\n            "userID": 1,\n            "id": = 10, \n            "title": "when an unknown printer took" \n        }, \n        {\n            "userID": 2,\n
# #   "id": = 11, \n            "title": "classical Latin literature from 45 BC" \n        },\n        {\n            "userID": 2,\n            "id": = 12, \n            "title": "cites of the word in" \n        }       \n]'
# # type(json_list) = <class 'list'>        len(json_list) = 4
# # json_list = [{'userID': 1, 'id': 9, 'title': "Lorem Ipsum has been the industry's standa"}, {'userID': 1, 'id': 10, 'title': 'when an unknown printer took'}, {'userID': 2, 'id': 11, 'title': 'classical Latin literature from 45 BC'}, {'userID': 2, 'id': 12, 'title': 'cites of the word in'}]

# на выходе получаем СПИСОК С 4 СЛОВАРЯМИ ВНУТРИ

# ЗАПИСЬ ИЗ Python в JSON - DUMP(), DUMPS()

# DUMP() - из Питон в ОБЪЕКТ JSON

# import json

# my_dict = {
#     "first_name": "Джон",
#     "last_name": "Смит",
#     "hobbies": ["кузнечное дело", "программирование", "путешествия"],
#     "age": 35,
#     "children": [
#         {
#             "first_name": "Алиса",
#             "age": 5
#         },
#         {
#             "first_name": "Маруся",
#             "age": 3
#         }
#     ]
# }

# print(f'{type(my_dict) = }\n{my_dict = }')
# with open ('new_user.json', 'w') as f:
#     json.dump(my_dict, f)

# type(my_dict) = <class 'dict'>
# my_dict = {'first_name': 'Джон', 'last_name': 'Смит', 'hobbies': ['кузнечное дело', 'программирование', 'путешествия'], 
#            'age': 35, 'children': [{'first_name': 'Алиса', 'age': 5}, {'first_name': 'Маруся', 'age': 3}]}

""" в файле 'new_user.json' видим запись 
{"first_name": "\u0414\u0436\u043e\u043d", "last_name": "\u0421\u043c\u0438\u0442", 
русские символы заменены на спец. коды. При этом они не потерялись. Если произвести десериализацию: """

# with open('new_user.json', 'r', encoding='utf-8') as f:
#     new_dict = json.load(f)
# print(f'{new_dict = }')

# # new_dict = {'first_name': 'Джон', 'last_name': 'Смит', 'hobbies': ['кузнечное дело', 'программирование', 'путешествия'], 'age': 35, 'children': [{'first_name': 'Алиса', 
# # 'age': 5}, {'first_name': 'Маруся', 'age': 3}]}

"""
Если хотим убрать символы экранирования, нужно воспользоваться доп. параметром для функции dump - ensure_ascii=False
"""

# with open ('new_user.json', 'w', encoding='utf-8') as f:
#     json.dump(my_dict, f, ensure_ascii=False)

## результат - {"first_name": "Джон", "last_name": "Смит", "hobbies": ["кузнечное дело", "программирование", "путешествия"],.....

# DUMPS() - из Питон в СТРОКУ, хранящую структуру JSON

# dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)
# print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

# type(dict_to_json_text) = <class 'str'>
# dict_to_json_text = '{"first_name": "Джон", "last_name": "Смит", "hobbies": ["кузнечное дело", "программирование", "путешествия"], 
# "age": 35, "children": [{"first_name": "Алиса", "age": 5}, {"first_name": "Маруся", "age": 3}]}'

# ДОПОЛНИТЕЛЬНЫЕ ПАРАМЕТРЫ DUMP/DUMPS
import json

my_dict2 = {
    "id": 2,
    "name": "Erwin Howell",
    "username": "Antonette",
    "email": "shanna@malissa.tv",
    "adress": {
        "street": "Victor Plains",
        "city": "Visoky",
        "zipcode": "90666-7771"
    },
    "phone": "7-995-544"
}

res = json.dumps(my_dict2, indent=2, separators=(',', ':'), sort_keys=True)
print(res) # - ПОЧЕМУ НЕ СТРОКА?????

# # {
# #   "adress":{
# #     "city":"Visoky",
# #     "street":"Victor Plains",
# #     "zipcode":"90666-7771"
# #   },
# #   "email":"shanna@malissa.tv",
# #   "id":2,
# #   "name":"Erwin Howell",
# #   "phone":"7-995-544",
# #   "username":"Antonette"
# # }

# TEST

# import json

# a = 'Hello world'
# b = {key: value for key, value in enumerate(a)}

# c = json.dumps(b, indent = 3, separators=('; ', '= '))
# print(c)


# # {
# #    "0"= "H";
# #    "1"= "e";
# #    "2"= "l";
# #    "3"= "l";
# #    "4"= "o";
# #    "5"= " ";
# #    "6"= "w";
# #    "7"= "o";
# #    "8"= "r";
# #    "9"= "l";
# #    "10"= "d"
# # }