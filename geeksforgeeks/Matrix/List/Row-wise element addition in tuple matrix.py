# Using enumerate() + list comprehension
list1 = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
list2 = [6, 7, 8]

res = [[sub + (list2[idx], ) for sub in val] for idx, val in enumerate(list1)]

print('The matrix after row elements addition:', res)
