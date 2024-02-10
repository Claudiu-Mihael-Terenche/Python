tup = (5, 6, (5, 6), 7, (8, 9), 9)

x = str(tup).translate({ord(item): None for item in '(),'}).split()
y = list(map(int, x))
z = list(set(y))

res = dict()
for item in z: res[item] = y.count(item)

print('The elements frequency:', res)

'''
# Using replace(),list(),map(),set(),split(),count() functions
# Python3 code to demonstrate working of
# Elements Frequency in Mixed Nested Tuple

tup = (5, 6, (5, 6), 7, (8, 9), 9)

# Printing original tuple
# print("The original tuple : " + str(test_tuple))

# Elements Frequency in Mixed Nested Tuple

# x = x.replace("(", "")
# x = x.replace(")", "")
# x = x.replace(",", "")

# y = x.split()

x = str(tup).translate({ord(item): None for item in '(),'}).split()
y = list(map(int, x))
z = list(set(y))
res = dict()

for item in z: res[item] = y.count(item)

print('The elements frequency:', res)
'''
