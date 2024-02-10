tup = (5, 20, 3, 7, 6, 8)

K = 2

tup = list(tup)

temp = sorted(tup)

res = tuple(temp[:K] + temp[-K:])

print('The extracted values:', res)

'''
# Python3 code to demonstrate working of
# Maximum and Minimum K elements in Tuple
# Using slicing + sorted()

test_tup = (5, 20, 3, 7, 6, 8)

# print("The original tuple is : " + str(test_tup))

K = 2

# Maximum and minimum K elements in tuple using slicing + sorted()
test_tup = list(test_tup) # test_tup = set(list(test_tup))
temp = sorted(test_tup)
res = tuple(temp[:K] + temp[-K:])

print('The extracted values:', res)
'''
