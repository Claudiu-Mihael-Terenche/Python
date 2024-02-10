# Using list comprehension

list1 = ['4', 'kg', 'butter', 'for', '40', 'bucks']

res = [elem.replace('4', '1') for elem in list1] # using list comprehension to modify the list

print('Modified list:', res)
