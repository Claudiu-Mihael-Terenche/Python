from operator import itemgetter

dict1 = {'Nikhil': {'English': 5, 'Maths': 2, 'Science': 14},
         'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
         'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}}

res1 = {key: dict(sorted(val.items(), key=itemgetter(1))) for key, val in dict1.items()}

res2 = {key: dict(sorted(val.items(), key=lambda ele: ele[1])) for key, val in dict1.items()}

print('The sorted dictionary:\n', res1, '\n', res2)

'''
# Using dictionary comprehension and itemgetter
from operator import itemgetter

dict1 = {'Nikhil': {'English': 5, 'Maths': 2, 'Science': 14},
'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}}

# printing original dictionary
# print("The original dictionary : " + str(test_dict))

# Sort Nested keys by Value
# Using dictionary comprehension and itemgetter

res1 = {key: dict(sorted(val.items(), key=itemgetter(1))) for key, val in dict1.items()}

# print('The sorted dictionary:', res1)

# Python3 code to demonstrate working of
# Sort Nested keys by Value
# Using sorted() + generator expression + lambda

# initializing dictionary
# test_dict = {'Nikhil': {'English': 5, 'Maths': 2, 'Science': 14},
             # 'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
             # 'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}}

# printing original dictionary
# print("The original dictionary : " + str(test_dict))

# Sort Nested keys by Value
# Using sorted() + generator expression + lambda

res2 = {key: dict(sorted(val.items(), key=lambda ele: ele[1])) for key, val in dict1.items()}

print('The sorted dictionary:\n', res1, '\n', res2)
'''
