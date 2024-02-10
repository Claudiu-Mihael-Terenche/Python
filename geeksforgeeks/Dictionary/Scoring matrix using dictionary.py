list1 = [['gfg', 'is', 'best'], ['gfg', 'is', 'for', 'geeks']]

dict1 = {'gfg' : 5, 'is' : 10, 'best' : 13, 'for' : 2, 'geeks' : 15}

res = [sum(dict1[word] if word.lower() in dict1 else 0 for word in sub) for sub in list1]

print('The row scores:', res)

'''
# Python3 code to demonstrate working of
# Scoring Matrix using Dictionary
# Using list comprehension + sum()

list1 = [['gfg', 'is', 'best'], ['gfg', 'is', 'for', 'geeks']]

# printing original list
# print("The original list is : " + str(test_list))

dict1 = {'gfg' : 5, 'is' : 10, 'best' : 13, 'for' : 2, 'geeks' : 15}

# Scoring Matrix using Dictionary using list comprehension + sum()
res = [sum(dict1[word] if word.lower() in dict1 else 0 for word in sub) for sub in list1]

print('The row scores:', res)
'''
