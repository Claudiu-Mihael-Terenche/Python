# Python3 code to swap elements in String list using replace() + list comprehension
list1 = ['Gfg', 'is', 'best', 'for', 'Geeks']

res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e')
       for sub in list1]

print('List after performing character swaps:', res)
