str1 = 'gfg is best for geeks'
dict1 = {'geeks': 1, 'best': 6}

str1 = ' '.join([word for word in str1.split() if word not in dict1.keys()])

print('The string after replace:', str1)

'''
# Python3 code to demonstrate working of
# Remove Dictionary Key Words
# Using List Comprehension and Join() Method

str1 = 'gfg is best for geeks'

# Printing original string
# print("The original string is : " + str(test_str))

dict1 = {'geeks': 1, 'best': 6}

# Remove Dictionary Key Words
# using List Comprehension and Join() Method

str1 = ' '.join([word for word in str1.split() if word not in dict1.keys()])

print('The string after replace:', str1)
'''
