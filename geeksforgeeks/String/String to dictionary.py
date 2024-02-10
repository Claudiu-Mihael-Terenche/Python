import ast

str1 = '{"Jan" : "January", "Feb" : "February", "Mar" : "March"}'

dict1 = ast.literal_eval(str1)

str2 = 'Jan = January; Feb = February; Mar = March'

dict2 = dict(subString.split('=') for subString in str2.split(';'))

str31 = 'Jan, Feb, March'; str32 = 'January | February | March'

keys = str31.split(', ')

values = str32.split('|')

dict3 = {}
dict3 = dict(zip(keys, values))

print('\n', dict1, '\n', dict2, '\n', dict3)

'''
# Python implementation of converting a string into a dictionary

# importing ast module
import ast

# initialising string dictionary
str = '{"Jan" : "January", "Feb" : "February", "Mar" : "March"}'

# converting string into dictionary
dictionary = ast.literal_eval(str)

# printing the generated dictionary
print(dictionary)

# Python implementation of converting
# a string into a dictionary

# initialising string
str = 'Jan = January; Feb = February; Mar = March'

# At first the string will be splitted
# at the occurrence of ';' to divide items
# for the dictionaryand then again splitting
# will be done at occurrence of '=' which
# generates key:value pair for each item
dictionary = dict(subString.split('=') for subString in str.split(';'))

# printing the generated dictionary
print(dictionary)

# Python implementation of converting
# a string into a dictionary

# initialising first string
str1 = 'Jan, Feb, March'
str2 = 'January | February | March'

# splitting first string
# in order to get keys
keys = str1.split(', ')

# splitting second string
# in order to get values
values = str2.split('|')

# declaring the dictionary
dictionary = {}

# Assigning keys and its
# corresponding values in
# the dictionary
dictionary = dict(zip(keys, values))

# printing the generated dictionary
print(dictionary)
'''
