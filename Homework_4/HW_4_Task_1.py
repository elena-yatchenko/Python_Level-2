# Напишите функцию для транспонирования матрицы
# см. List Comprehension
# вар.1 

# transp_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
# print(transp_matrix)

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         transp_matrix[j][i] = matrix[i][j]
# print(transp_matrix)

# вар. 2

matrix = [[5, 7, 9, 3], [2, 4, 6, 7]] 

def transp(matrix):
    transp_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transp_matrix

print(transp(matrix))

                 