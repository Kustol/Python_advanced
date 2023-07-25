'''
Напишите функцию для транспонирования матрицы
'''


def matrix_trans(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(f'Исходная матрица: {matrix}')
    print(f'Транспонированная матрица: {trans_matrix}')

if __name__ == "__main__":
    matrix = [[1, 4],
              [2, 5],
              [3, 6]]
    matrix_trans(matrix)
