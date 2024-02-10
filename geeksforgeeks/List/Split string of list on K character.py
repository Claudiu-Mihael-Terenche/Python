list1 = ['Gfg is best', 'for Geeks', 'Preparing']

K = ' '

res1 = [word for phrase in list1 for word in phrase.split(K)]

res2 = K.join(list1).split(K)

print('The extended list after split strings:\n', res1, '\n', res2)

'''
# Using list comprehension

list1 = ['Gfg is best', 'for Geeks', 'Preparing']
K = ' '

# split string of list on K character using list comprehension
res1 = [word for phrase in list1 for word in phrase.split(K)]

# print('The extended list after split strings:', res1)

# Version 2: Python3 code to split string of list on K character using join() + split()

# initializing list 
# list2 = ['Gfg is best', 'for Geeks', 'Preparing']

# printing original list
# print('The original list is:', str(list2))

# K2 = ' '

# split string of list on K character using join() + split()

res2 = K.join(list1).split(K)

print('The extended list after split strings:\n', res1, '\n', res2)
'''
