# Задача о матричных операциях

# Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.

# АТРИБУТЫ класса:
# rows (int): Количество строк в матрице.
# cols (int): Количество столбцов в матрице.
# data (list): Двумерный список, содержащий элементы матрицы.

# МЕТОДЫ класса:

# __init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols, 
# а также создает двумерный список data размером rows x cols и заполняет его нулями.

# __str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу, 
# где элементы разделены пробелами, а строки разделены символами новой строки. Например:

# 1 2 3
# 4 5 6
# __repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано для создания 
# нового объекта того же класса с такими же размерами и данными.

# __eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True, 
# если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.

# __add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые 
# размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент равен сумме 
# соответствующих элементов входных матриц.

# __mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет, что количество столбцов в первой 
# матрице равно количеству строк во второй матрице. Если условие выполняется, создает новую матрицу, 
# где элемент на позиции [i][j] равен сумме произведений элементов соответствующей строки из первой матрицы и столбца из 
# второй матрицы.

# Пример

# На входе:


# # Создаем матрицы
# matrix1 = Matrix(2, 3)
# matrix1.data = [[1, 2, 3], [4, 5, 6]]

# matrix2 = Matrix(2, 3)
# matrix2.data = [[7, 8, 9], [10, 11, 12]]

# # Выводим матрицы
# print(matrix1)

# print(matrix2)
# На выходе:


# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# На входе:


# # Сравниваем матрицы
# print(matrix1 == matrix2)
# На выходе:


# False
# На входе:


# # Выполняем операцию сложения матриц
# matrix_sum = matrix1 + matrix2
# print(matrix_sum)
# На выходе:


# 8 10 12
# 14 16 18
# На входе:


# # Выполняем операцию умножения матриц
# matrix3 = Matrix(3, 2)
# matrix3.data = [[1, 2], [3, 4], [5, 6]]

# matrix4 = Matrix(2, 2)
# matrix4.data = [[7, 8], [9, 10]]

# result = matrix3 * matrix4
# print(result)
# На выходе:


# 25 28
# 57 64
# 89 100

class Matrix:
    

    def __init__(self, rows, cols):
        """__init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows (строки) и cols(столбцы), 
        а также создает двумерный список data размером rows x cols (т.е. список из rows подсписков с количеством элементов в подсписке
        равным cols) и заполняет его нулями."""
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)]
    

    def __str__(self):
        """__str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу, 
        где элементы разделены пробелами, а строки разделены символами новой строки."""
        # self.info = ''
        # for i in range(self.rows):
        #     self.curr_info = f"{' '.join(map(str, self.data[i]))}"
        #     self.info += f'{self.curr_info}\n' 
        # print([' '.join(map(str, self.data[i])) for i in range(self.rows)])
        # ['0 0 0', '0 0 0']
        return '\n'.join([' '.join(map(str, self.data[i])) for i in range(self.rows)])
   

    def __repr__(self):
        """__repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано для создания 
        нового объекта того же класса с такими же размерами и данными."""
        return f'Matrix ({self.rows}, {self.cols})'
        
    def __eq__(self, other):
        """ __eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True, 
        если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False."""
        # print(all([self.data[i][j] == other.data[i][j] for j in range(self.cols) for i in range(self.rows)]))
        return self.rows == other.rows and self.cols == other.cols and all([self.data[i][j] == other.data[i][j] 
                                                                           for j in range(self.cols) for i in range(self.rows)])
        # можно разбить проверку на этапы, см. решение системы
        
    def __add__(self, other):
        """__add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые 
        размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент равен сумме 
        соответствующих элементов входных матриц."""
        if self.rows != other.rows or self.cols != other.cols:
            return 'Матрицы имеют различные размеры и не подходят для операции сложения'
        else:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]       
            return result
            # return [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
            # # в таком варианте принт выведет именно лист, а не выражения для __str__ или __repr__. Т.е. я явно задаю матрицу, а не объект класса Matrix
        
    def __mul__(self, other):
        """__mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет, что количество столбцов в первой 
        матрице равно количеству строк во второй матрице. Если условие выполняется, создает новую матрицу, 
        где элемент на позиции [i][j] равен сумме произведений элементов соответствующей строки из первой матрицы и столбца из 
        второй матрицы.""" 
        if self.cols != other.rows:
            return 'Матрицы не подходят для операции умножения'   
        else:
            result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result
      
# m1 = Matrix(3, 3)
# m2 = Matrix(3, 3)
# # print(m1)
# # print(m1 == m2)
# m1.data = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# m2.data = [[1, 1, 1], [4, 4, 4], [3, 3, 3]]
# print(m1 == m2)
# print(m1)
# print()
# print(m2)
# print()
# #print(m1 + m2)
# print(m1 * m2)


# ПРОВЕРКИ (ТЕСТЫ)


# # Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# # Выводим матрицы
# print(matrix1)

# print(matrix2)
# На выходе:


# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# На входе:


# # Сравниваем матрицы
print(matrix1 == matrix2)
# На выходе:


# False
# На входе:


# # Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)
# На выходе:


# 8 10 12
# 14 16 18
# На входе:


# # Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
# На выходе:


# 25 28
# 57 64
# 89 100








# class Matrix:
#     """
#     Класс, представляющий матрицу.

#     Атрибуты:
#     - rows (int): количество строк в матрице
#     - cols (int): количество столбцов в матрице
#     - data (list): двумерный список, содержащий элементы матрицы

#     Методы:
#     - __str__(): возвращает строковое представление матрицы
#     - __repr__(): возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта
#     - __eq__(other): определяет операцию "равно" для двух матриц
#     - __add__(other): определяет операцию сложения двух матриц
#     - __mul__(other): определяет операцию умножения двух матриц
#     """

#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.data = [[0 for j in range(cols)] for i in range(rows)]

#     def __str__(self):
#         """
#         Возвращает строковое представление матрицы.

#         Возвращает:
#         - str: строковое представление матрицы
#         """
#         return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

#     def __repr__(self):
#         """
#         Возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта.

#         Возвращает:
#         - str: строковое представление матрицы
#         """
#         return f"Matrix({self.rows}, {self.cols})"

#     def __eq__(self, other):
#         """
#         Определяет операцию "равно" для двух матриц.

#         Аргументы:
#         - other (Matrix): вторая матрица

#         Возвращает:
#         - bool: True, если матрицы равны, иначе False
#         """
#         if self.rows != other.rows or self.cols != other.cols:
#             return False
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 if self.data[i][j] != other.data[i][j]:
#                     return False
#         return True

#     def __add__(self, other):
#         """
#         Определяет операцию сложения двух матриц.

#         Аргументы:
#         - other (Matrix): вторая матрица

#         Возвращает:
#         - Matrix: новая матрица, полученная путем сложения двух исходных матриц
#         """
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Матрицы должны иметь одинаковые размеры")
#         result = Matrix(self.rows, self.cols)
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 result.data[i][j] = self.data[i][j] + other.data[i][j]
#         return result

#     def __mul__(self, other):
#         """
#         Определяет операцию умножения двух матриц.

#         Аргументы:
#         - other (Matrix): вторая матрица

#         Возвращает:
#         - Matrix: новая матрица, полученная путем умножения двух исходных матриц
#         """
#         if self.cols != other.rows:
#             raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
#         result = Matrix(self.rows, other.cols)
#         for i in range(self.rows):
#             for j in range(other.cols):
#                 for k in range(self.cols):
#                     result.data[i][j] += self.data[i][k] * other.data[k][j]
#         return result
