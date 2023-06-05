def rotate_matrix_180(matrix):
    m = len(matrix)
    n = len(matrix[0])
    new_matrix = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            new_matrix[i][j] = matrix[m - i - 1][n - j - 1]

    return new_matrix


m = int(input("Enter the number of rows of the matrix: "))
n = int(input("Enter the number of columns of the matrix: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        el = int(input("Enter element: "))
        row.append(el)
    matrix.append(row)

new_matrix = rotate_matrix_180(matrix)

for row in new_matrix:
    print(row)


