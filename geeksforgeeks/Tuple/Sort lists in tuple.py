tup = ([7, 5, 4], [8, 2, 4], [0, 7, 5])

res1 = tuple(map(sorted, tup))

res2 = tuple((sorted(sub) for sub in tup))

print('The tuple after sorting lists:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Sort lists in tuple
# Using map() + sorted()


tup = ([7, 5, 4], [8, 2, 4], [0, 7, 5])

# printing original tuple
# print("The original tuple is : " + str(test_tup))

# Sort lists in tuple
# Using map() + sorted()

res1 = tuple(map(sorted, tup))

# print('The tuple after sorting lists:', res1)

# Python3 code to demonstrate working of
# Sort lists in tuple
# Using tuple() + sorted() + generator expression

# Initializing tuple
# test_tup = ([7, 5, 4], [8, 2, 4], [0, 7, 5])

# printing original tuple
# print("The original tuple is : " + str(test_tup))

# Sort lists in tuple
# Using tuple() + sorted() + generator expression

res2 = tuple((sorted(sub) for sub in tup))

print('The tuple after sorting lists:\n', res1, '\n', res2)
'''
