# Напишите функцию для транспонирования матрицы

MATRIX = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def transp(matrix):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]

    return result


print(transp(MATRIX))

# temp_number = matrix[i][j]
# matrix[i][j] = matrix[j][i]
# matrix[j][i] = temp_number
