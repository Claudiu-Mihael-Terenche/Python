# Python3 code to demonstrate working of remove redundant substrings from a string list
# using list comprehension + join() + enumerate()
list1 = ['Gfg', 'Gfg is best', 'Geeks', 'Gfg is for Geeks']

list1.sort(key=len)

res = [val for idx, val in enumerate(list1) if val not in ', '.join(list1[idx + 1:])]

print('The filtered list:', res)
