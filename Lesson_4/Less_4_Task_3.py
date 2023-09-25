# Задание №3

# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def new_dict(text):
    my_list=[]
    for number in text.split():
        # symb = chr(int(number))
        my_list.append(chr(int(number)))
    # print(my_list)
    my_dict = {}
    for elem in my_list:
        my_dict[elem] = ord(elem)
    return my_dict

enter_text = input('Введите 2 целых числа через пробел: ')
print(new_dict(enter_text))

# ['Ϫ', 'ဎ']
# {'Ϫ': 1002, 'ဎ': 4110}