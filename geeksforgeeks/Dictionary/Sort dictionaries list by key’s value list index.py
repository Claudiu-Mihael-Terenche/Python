list1 = [{"Gfg": [6, 7, 9], "is": 9, "best": 10},
         {"Gfg": [2, 0, 3], "is": 11, "best": 19},
		 {"Gfg": [4, 6, 9], "is": 16, "best": 1}]

K1 = 'Gfg'; idx = 2; K2 = 'best'

res1 = sorted(list1, key=lambda ele: ele[K1][idx])

res2 = sorted(sorted(list1, key=lambda ele: ele[K2]), key=lambda ele: ele[K1][idx])

print('The required sort order:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Sort dictionaries list by Key's Value list index
# Using sorted() + lambda (Additional parameter in case of tie)

list1 = [{"Gfg": [6, 7, 9], "is": 9, "best": 10},
         {"Gfg": [2, 0, 3], "is": 11, "best": 19},
		 {"Gfg": [4, 6, 9], "is": 16, "best": 1}]

# printing original list
# print("The original list : " + str(test_list))

K1 = 'Gfg'; idx = 2; K2 = 'best'

# using sorted() to perform sort in basis of 2 parameter key
# inner is evaluated after the outer key in lambda order

res1 = sorted(list1, key=lambda ele: ele[K1][idx])
res2 = sorted(sorted(list1, key=lambda ele: ele[K2]), key=lambda ele: ele[K1][idx])

print('The required sort order:\n', res1, '\n', res2)
'''
