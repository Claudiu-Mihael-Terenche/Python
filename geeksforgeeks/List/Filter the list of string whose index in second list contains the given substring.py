list1 = ['Gfg', 'is', 'not', 'best', 'and', 'not', 'for', 'CS']
list2 = ['Its ok', 'all ok', 'no', 'looks ok', 'ok', 'wrong', 'ok', 'thats ok']

sub_str = 'ok'

res = [item1 for item1, item2 in zip(list1, list2) if sub_str in item2]

print('The extracted list:', res)

'''
# Python3 code to extract elements filtered by substring from other list using list comprehension + zip()

# initializing list

list1 = ['Gfg', 'is', 'not', 'best', 'and', 'not', 'for', 'CS']
list2 = ['Its ok', 'all ok', 'no', 'looks ok', 'ok', 'wrong', 'ok', 'thats ok']

# printing original lists
# print('The original list 1 is:', str(list1))
# print('The original list 2 is:', str(list2))

# initializing substr

sub_str = 'ok'

# using list comprehension to perform task
res = [item1 for item1, item2 in zip(list1, list2) if sub_str in item2]

print('The extracted list:', res)
'''
