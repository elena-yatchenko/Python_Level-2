# Напишите функцию, которая открывает
# на чтение созданные в прошлых задачах
# файлы с числами и именами. Перемножьте пары чисел.

# В новый файл сохраните имя и произведение:
#   если результат умножения отрицательный,
#   сохраните имя записанное строчными буквами и произведение по модулю

#   если результат умножения положительный,
#   сохраните имя прописными буквами и произведение округлённое до целого.

# В результирующем файле должно быть столько же строк,
# сколько в более длинном файле. При достижении конца
# более короткого файла, возвращайтесь в его начало.

def func(path_numb: str, path_name: str, path_result: str):
    with (
        open(path_numb, 'r', encoding='utf-8') as data_numbers,
        open(path_name, 'r', encoding='utf-8') as data_name,
        open(path_result, 'a', encoding='utf-8') as result,
        
    ):
        len_numb = sum(1 for i in data_numbers) # находим длину файлов,чтобы понять какой больше
        len_name = sum(1 for i in data_name)
        # data_numbers.seek(0)
        # data_name.seek(0)
        
        for i in range(max(len_numb, len_name)): # идем циклу столько раз, сколько строка в более длинной файле
            numb = string_step(data_numbers)
            name = string_step(data_name)
            num_i, num_f = numb.split('|') # распаковка полученной строки
            mult = int(num_i) * float(num_f)
            if mult < 0:
                result.write(f'{name.lower()} {-mult}\n')
            if mult > 0:
                result.write(f'{name.upper()} {mult: .0f}\n') # округляем, можно и через round, не прописывая второй аргумент (количество знаков после запятой)
                                
        
# функция, которая идет по строкам файла и возвращает по 1 строке      
def string_step(name_file): 
    text = name_file.readline()
    if text == "":
        name_file.seek(0) # когда доходим до конца файла (пустая строка), возвращаем курсор в начало
        text = name_file.readline()
    return text.strip() # удаляем \n в конце строки
        
func('text.txt', 'text_name.txt', 'text_result.txt')

# другой вариант посчитать количество строк в файле
# длинна строк в файле 
# with open('text.txt') as f:
#         my_lines = f.readlines()
# print(len(my_lines))
# print(my_lines)



