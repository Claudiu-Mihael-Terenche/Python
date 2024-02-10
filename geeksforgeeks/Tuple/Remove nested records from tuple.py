tup = (1, 5, 7, (4, 6), 10)

res1 = [item for item in tup if not isinstance(item, tuple)]

res2 = list(filter(lambda item: not isinstance(item, tuple), tup))

print('Elements after removal of nested records:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Remove nested records
# Using list comprehension

tup = (1, 5, 7, (4, 6), 10)

# printing original tuple
# print("The original tuple : " + str(test_tup))

# Remove nested records

res1 = [item for item in tup if not isinstance(item, tuple)]

# print('Elements after removal of nested records:', res1)

# Python3 code to demonstrate working of
# Remove nested records
# Using filter() and lambda function

# tup = (1, 5, 7, (4, 6), 10)

# printing original tuple
# print("The original tuple : " + str(test_tup))

# Remove nested records

res2 = list(filter(lambda item: not isinstance(item, tuple), tup))

print('Elements after removal of nested records:\n', res1, '\n', res2)
'''
