list1 = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]

temp = set(list1) & {(b, a) for a, b in list1}

res = {(a, b) for a, b in temp if a < b}

print('The symmetric tuples:', res)

'''
# Python3 code to demonstrate working of
# Extract Symmetric Tuples
# Using dictionary comprehension + set()

list1 = [(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]

# printing original list
# print("The original list is : " + str(test_list))

# Extract Symmetric Tuples
# Using dictionary comprehension + set()

temp = set(list1) & {(b, a) for a, b in list1}

res = {(a, b) for a, b in temp if a < b}

print('The symmetric tuples:', res)
'''
