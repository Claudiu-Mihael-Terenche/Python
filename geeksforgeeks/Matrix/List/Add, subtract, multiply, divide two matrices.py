# Program to add two matrices using list comprehension
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

rows = len(matrix1)
cols = len(matrix1[0])

res1 = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
res2 = [[matrix1[i][j] - matrix2[i][j] for j in range(cols)] for i in range(rows)]
res3 = [[matrix1[i][j] * matrix2[i][j] for j in range(cols)] for i in range(rows)]
res4 = [[matrix1[i][j] / matrix2[i][j] for j in range(cols)] for i in range(rows)]

for r in res1:
    print(r)

for r in res2:
    print(r)

for r in res3:
    print(r)

for r in res4:
    print(r)
