from itertools import chain

# Python3 code to demonstrate matrix product using nested loops

list1 = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

res1 = 1
for i in list1:
	for j in i:
		res1 *= j

# Python3 code to do matrix product using chain() + loop

def prod1(val):
	res2 = 1
	for ele in val:
		res2 *= ele
	return res2


res2 = prod1(list(chain(*list1)))

# Using list comprehension + loop

def prod2(val):
	res3 = 1
	for ele in val:
		res3 *= ele
	return res3


res3 = prod2([ele for sub in list1 for ele in sub])

print('The total element product in lists is:\n', res1, '\n', res2, '\n', res3)
