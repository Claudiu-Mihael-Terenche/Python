from itertools import chain
# Python3 code to demonstrate matrix product using nested loops
list1 = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

res1 = 1
for i in list1:
    for j in i:
        res1 *= j


# Python3 code to do matrix product using chain() + loop

def prod2(val):
    res02 = 1
    for ele in val:
        res02 *= ele
    return res02


res2 = prod2(list(chain(*list1)))


# Using list comprehension + loop

def prod3(val):
    res03 = 1
    for ele in val:
        res03 *= ele
    return res03


res3 = prod3([ele for sub in list1 for ele in sub])

print('The total element product in lists is:\n', res1, '\n', res2, '\n', res3)
