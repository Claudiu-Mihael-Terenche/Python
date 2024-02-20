# Python3 code to extract indices of substring matches using list comprehension + enumerate()
list1 = ['Gfg is good', 'for Geeks', 'I love Gfg', 'Its useful']
K = 'Gfg'

res = [idx for idx, val in enumerate(list1) if K in val]

print('The indices list:', res)
