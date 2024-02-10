from functools import reduce

list1 = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]

ord_list = ['Geeks', 'best', 'CS', 'Gfg']

res1 = sorted(list1, key=lambda item: ord_list.index(item[0]))

temp = dict(list1)

res2 = [(key, temp[key]) for key in ord_list]

res3 = reduce(lambda acc, key: acc + [ele for ele in list1 if ele[0] == key], ord_list, [])

print('The ordered tuple list:\n', res1, '\n', res2, '\n', res3)

'''
# Using lambda

def order_tuples_by_list(list1, ord_list):
	return sorted(list1, key=lambda item: ord_list.index(item[0]))

list1 = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]

ord_list = ['Geeks', 'best', 'CS', 'Gfg']

print(order_tuples_by_list(list1, ord_list))

list1 = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]

ord_list = ['Geeks', 'best', 'CS', 'Gfg']

res1 = sorted(list1, key=lambda item: ord_list.index(item[0]))

# print(res1)

# Python3 code to demonstrate working of
# Order Tuples by List
# Using dict() + list comprehension

# initializing list
# test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

# printing original list
# print("The original list is : " + str(test_list))

# initializing order list
# ord_list = ['Geeks', 'best', 'CS', 'Gfg']

# Order Tuples by List
# Using dict() + list comprehension

temp = dict(list1)

res2 = [(key, temp[key]) for key in ord_list]

# print('The ordered tuple list:', res2)

# Using reduce():
from functools import reduce

# test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

# printing original list
# print("The original list is : " + str(test_list))

# initializing order list
# ord_list = ['Geeks', 'best', 'CS', 'Gfg']

# using reduce() to sort the list based on order list

res3 = reduce(lambda acc, key: acc + [ele for ele in list1 if ele[0] == key], ord_list, [])

print('The ordered tuple list:\n', res1, '\n', res2, '\n', res3)
'''
