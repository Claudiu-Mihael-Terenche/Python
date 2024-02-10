tup = (1, 5, 7, 8, 10)

res1 = tuple(i * j for i, j in zip(tup, tup[1:]))

res2 = tuple(map(lambda i, j: i * j, tup[1:], tup[:-1]))

res3 = []
for i in range(len(tup) - 1): res3.append(tup[i] * tup[i + 1])

res3 = tuple(res3)

print('Resultant tuple after multiplication:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to do djacent element multiplication using zip() + generator expression + tuple

tup = (1, 5, 7, 8, 10)

# printing original tuple
# print("The original tuple : " + str(tup1))

# adjacent element multiplicationusing zip() + generator expression + tuple

res1 = tuple(i * j for i, j in zip(tup, tup[1:]))

# print('Resultant tuple after multiplication:', res1)

# Python3 code to do adjacent element multiplication using tuple() + map() + lambda

# tup2 = (1, 5, 7, 8, 10)

# printing original tuple
# print("The original tuple : " + str(tup2))

# adjacent element multiplication using tuple() + map() + lambda

res2 = tuple(map(lambda i, j: i * j, tup[1:], tup[:-1]))

# print('Resultant tuple after multiplication:', res2)

# Python3 code to do adjacent element multiplication using for loop

# tup3 = (1, 5, 7, 8, 10)

# printing original tuple
# print("The original tuple : " + str(tup3))

res3 = []
for i in range(len(tup) - 1): res3.append(tup[i] * tup[i + 1])

res3 = tuple(res3)

print('Resultant tuple after multiplication:\n', res1, '\n', res2, '\n', res3)
'''
