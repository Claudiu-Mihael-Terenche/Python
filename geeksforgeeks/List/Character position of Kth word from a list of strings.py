list1 = ['geekforgeeks', 'is', 'best', 'for', 'geeks']

K = 20

res = [item[0] for sub in enumerate(list1) for item in enumerate(sub[1])]

res = res[K]

print('Index of character at Kth position word:', res)

'''
# Python3 code to find word index for K position in strings list using enumerate() + list comprehension

list1 = ['geekforgeeks', 'is', 'best', 'for', 'geeks']

# printing original list
# print("The original list is : " + str(list1))

K = 20

# enumerate to get indices of all inner and outer list
res = [item[0] for sub in enumerate(list1) for item in enumerate(sub[1])]

res = res[K] # getting index of word

print('Index of character at Kth position word:', res)
'''
