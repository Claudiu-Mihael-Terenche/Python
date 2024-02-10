list1 = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]

res1 = sorted(list1, key=lambda sub: (-sub[0], sub[1]))

list2 = [(7, (8, 4)), (5, (6, 1)), (7, (5, 9)), (10, (5, 4)), (10, (1, 3))]

res2 = sorted(list2, key=lambda sub: (-sub[0], sum(sub[1])))

print('The tuple after custom sorting is:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of custom sorting in list of tuples using sorted() + lambda

list1 = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]

# printing original list
# print("The original list is : " + str(test_list))

# Custom sorting in list of tuples
# Using sorted() + lambda

res1 = sorted(list1, key=lambda sub: (-sub[0], sub[1]))

# print('The tuple after custom sorting is:', res1)

# Python3 code to demonstrate working of custom sorting in list of tuples using sorted() + lambda() + sum()

list2 = [(7, (8, 4)), (5, (6, 1)), (7, (5, 9)), (10, (5, 4)), (10, (1, 3))]

# printing original list
# print("The original list is : " + str(test_list))

# Custom sorting in list of tuples
# Using sorted() + lambda() + sum()

res2 = sorted(list2, key=lambda sub: (-sub[0], sum(sub[1])))


print('The tuple after custom sorting is:\n', res1, '\n', res2)
'''
