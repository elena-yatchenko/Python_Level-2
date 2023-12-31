# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

# import json
# import os


# def func(file_name):
#     store_id = set()
#     if os.path.exists(file_name):
#         with open(file_name, 'r', encoding='utf-8') as f:
#             new_dict =json.load(f)
#             for _, value in new_dict.items():
#                 store_id.update(value.keys())
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
#         if level not in new_dict: # првоеряет, есть ли такой ключ в нашем словаре, который задан с ключами 1 - 7
#             print('Уровень доступа должен быть от 1 до 7')
#             continue

# # Оператор continue передает элемент управления в следующую итерацию ближайшего внешнего оператора do , for или while , 
# # в которой она отображается, минуя все оставшиеся операторы в теле оператора do , for или while. Т.е. в данном случае с любого 
# # continue вернемся в  name = input('Name: ')
# #     
#         store_id.add(_id)
#         new_dict[level].update({_id: name}) # апдейтим внутренний словарь, который является значением ключа level
#         print(new_dict)                   
            
#         with open('result_write.json', 'w', encoding='utf-8') as f:
#             json.dump(new_dict, f, indent=2, ensure_ascii=False)
 
# func('result_write.json')   
# dump перезаписывает словарь каждый раз, просто каждый раз он уже с добавленными новыми значениями


import csv 
import json

def json_to_csv(file_name):
    with (
        open(file_name, 'r', encoding='utf-8') as file_json,
        open('csv_name.csv', 'w', newline='', encoding='utf-8') as file_csv
    ):
        csv_write = csv.DictWriter(file_csv, fieldnames=['level', 'id', 'name'], dialect='excel', delimiter=',',
                                   quoting=csv.QUOTE_MINIMAL)
        csv_write.writeheader()

        lst = []
        new_dict =json.load(file_json)
        for level, value in new_dict.items():
            for _id, name in value.items():
                lst.append({'level': int(level), 'id': int(_id), 'name': name})
        print(lst)     
        csv_write.writerows(lst)
        
json_to_csv('result_write.json')
