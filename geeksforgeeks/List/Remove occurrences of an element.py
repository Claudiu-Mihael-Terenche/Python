# Using enumerate

list1 = [1, 3, 4, 6, 5, 1]

num = 1

res = [j for i, j in enumerate(list1) if j != num]

print(res)
