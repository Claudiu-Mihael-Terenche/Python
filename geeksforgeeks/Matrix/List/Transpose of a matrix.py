# Using zip()

matrix = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]

res1 = [list(row) for row in zip(*matrix)]

for row in res1: print(row)

cols = len((matrix[0]))

res2 = [[row[i] for row in matrix] for i in range(cols)]

for row in res2: print(' '.join([str(elem) for elem in row]))

'''
# Using zip()
matrix = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]

res1 = [list(row) for row in zip(*matrix)]

# print("Original Matrix:")
# for row in matrix:
	# print(row)

# print("Transposed Matrix:")
for row in res1: print(row)

# Using list comprehension
# A = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]

cols = len((matrix[0]))

res2 = [[row[i] for row in matrix] for i in range(cols)]

for row in res2: print(' '.join([str(elem) for elem in row]))
'''
