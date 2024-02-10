list1 = ['Gfg', 'Gfg is best', 'Geeks', 'Gfg is for Geeks']

list1.sort(key=len)

res = [item for idx, item in enumerate(list1) if item not in ', '.join(list1[idx + 1:])]

print('The filtered list:', res)

'''
# Python3 code to remove redundant substrings from strings list using list comprehension + join() + enumerate()

# initializing list

list1 = ['Gfg', 'Gfg is best', 'Geeks', 'Gfg is for Geeks']

# printing original list
# print('The original list:', str(list1))

# using list comprehension to iterate for each string and perform join in one liner

list1.sort(key = len)

res = [item for idx, item in enumerate(list1) if item not in ', '.join(list1[idx + 1:])]

print('The filtered list:', res)
'''
