# Using enumerate
list1 = [1, 3, 4, 6, 5, 1]
num = 1

res1 = [item for item in list1 if item != num]

res2 = [j for i, j in enumerate(list1) if j != num]

print('', *res1, '\n', *res2)
