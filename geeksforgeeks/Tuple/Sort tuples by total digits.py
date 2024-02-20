list1 = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]

res1 = sorted(list1, key=lambda tup: sum([len(str(ele)) for ele in tup]))


def count_digs(tup): return sum([len(str(ele)) for ele in tup])


list1.sort(key=count_digs)

print('Sorted tuples:\n', res1, '\n', list1)

'''
# Python3 code to sort tuples by total digits using sorted() + lambda + sum() + len()

list1 = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]

# printing original list
# print("The original list is : " + str(list1))

# performing sort, lambda function provides logic

res1 = sorted(list1, key=lambda tup: sum([len(str(ele)) for ele in tup ]))

# print('Sorted tuples:', res1)

# Python3 code to sort tuples by total digits using sort() + len() + sum()

def count_digs(tup): return sum([len(str(ele)) for ele in tup]) # gets total digits in tuples


# list2 = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]

# printing original list
# print('The original list is:', str(list2))

# performing sort

list1.sort(key=count_digs)

print('Sorted tuples:\n', res1, '\n', list1)
'''
