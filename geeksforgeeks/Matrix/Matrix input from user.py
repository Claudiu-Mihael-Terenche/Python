R = int(input('Enter the number of rows: '))
C = int(input('Enter the number of columns: '))

matrix = []
print('Enter the entries row wise: ')

for i in range(R):  # a for loop for row entries
    a = []
    for j in range(C):  # a for loop for column entries
        a.append(int(input()))
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=' ')
    print()
