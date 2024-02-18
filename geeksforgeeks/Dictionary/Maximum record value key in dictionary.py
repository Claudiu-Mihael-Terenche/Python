dict1 = {'gfg': {'Manjeet': 5, 'Himani': 10},
         'is': {'Manjeet': 8, 'Himani': 9},
         'best': {'Manjeet': 10, 'Himani': 15}}

key = 'Himani'

res = max(dict1, key=lambda sub: dict1[sub][key])

print('The required key is:', res)

'''
# Python3 code to demonstrate working of
# Maximum record value key in dictionary
# Using max() + lambda function

# initializing dictionary

dict1 = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
         'is' : {'Manjeet' : 8, 'Himani' : 9},
         'best' : {'Manjeet' : 10, 'Himani' : 15}}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# initializing search key

key = 'Himani'

# Maximum record value key in dictionary
# Using max() + lambda function

res = max(dict1, key=lambda sub: dict1[sub][key])

print('The required key is:', res)
'''
