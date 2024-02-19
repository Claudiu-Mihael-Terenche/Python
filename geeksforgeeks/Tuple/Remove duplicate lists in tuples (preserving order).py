tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])

res1 = []
for item in tup:
    if item not in res1:
        (res1.append(item))

temp = set()
res2 = [ele for ele in tup if not (tuple(ele) in temp or temp.add(tuple(ele)))]

print('The unique lists tuple is:\n', res1, '\n', res2)

'''
# Using loop and if-else statement

tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])

res1 = []
for item in tup:
    if item not in res1:
        (res1.append(item))

# print('The unique lists tuple is:', res1)

# Python3 code to demonstrate working of
# Remove duplicate lists in tuples(Preserving Order)
# Using list comprehension + set()

# Initializing tuple
# tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])

# printing original tuple
# print("The original tuple is : " + str(test_tup))

# Remove duplicate lists in tuples(Preserving Order)
# Using list comprehension + set()

temp = set()
res2 = [ele for ele in tup if not(tuple(ele) in temp or temp.add(tuple(ele)))]

print('The unique lists tuple is:\n', res1, '\n', res2)
'''
