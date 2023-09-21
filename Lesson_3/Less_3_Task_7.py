# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается каждая
# буква в строке без использования метода count и с ним.
# Результат сохраните в словаре,
# где ключ - символ, а значение - частота встречи символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

word = input('Введите строку: ')
my_dict = {}

for letter in word:
    my_dict.setdefault(letter, 0)
    my_dict[letter] += 1
    
print(my_dict)

# можно дополнительно удалить из полученного словаря пробелы и проч. знаки, 
# удалив указанные пары ключ-пробелы