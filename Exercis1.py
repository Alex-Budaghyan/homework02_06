def count_adjacent_m(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'M':
                new_matrix[i][j] = 'M'
                continue

            count = 0
            if i > 0 and matrix[i - 1][j] == 'M':
                count += 1
            if i < rows - 1 and matrix[i + 1][j] == 'M':
                count += 1
            if j > 0 and matrix[i][j - 1] == 'M':
                count += 1
            if j < cols - 1 and matrix[i][j + 1] == 'M':
                count += 1
            if i > 0 and j > 0 and matrix[i - 1][j - 1] == 'M':
                count += 1
            if i > 0 and j < cols - 1 and matrix[i - 1][j + 1] == 'M':
                count += 1
            if i < rows - 1 and j > 0 and matrix[i + 1][j - 1] == 'M':
                count += 1
            if i < rows - 1 and j < cols - 1 and matrix[i + 1][j + 1] == 'M':
                count += 1

            new_matrix[i][j] = count
    return new_matrix


m = int(input("Enter the number of rows of the matrix: "))
n = int(input("Enter the number of columns of the matrix: "))
matrix = []
for i in range(m):
    row  = []
    for j in range(n):
        el = input("Enter element: ")
        row.append(el)
    matrix.append(row)
new_matrix = count_adjacent_m(matrix)
for row in new_matrix:
    print(row)