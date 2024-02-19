str1 = 'geekforgeeks best for geeks'
lookup_dict = {'best': 'good and better', 'geeks': 'all CS aspirants'}

res = ' '.join(lookup_dict.get(ele, ele) for ele in str1.split())

print('Replaced string:', res)

'''
# Using list comprehension + join()
# Python3 code to demonstrate working of
# Replace words from Dictionary
# Using list comprehension + join()

str1 = 'geekforgeeks best for geeks'

# printing original string
# print("The original string is : " + str(test_str))

# lookup Dictionary

lookup_dict = {'best': 'good and better', 'geeks': 'all CS aspirants'}

# one-liner to solve problem
res = ' '.join(lookup_dict.get(ele, ele) for ele in str1.split())

print('Replaced string:', res)
'''
