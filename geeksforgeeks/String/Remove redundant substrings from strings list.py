# Python3 code to demonstrate working of remove redundant substrings from strings list using list comprehension + join() + enumerate()

list = ['Gfg', 'Gfg is best', 'Geeks', 'Gfg is for Geeks']

list.sort(key=len)

res = [val for idx, val in enumerate(list) if val not in ', '.join(list[idx + 1:])]

print('The filtered list:', res)
