# Python3 code to print frequency of numbers in string using list comprehension
str1 = 'geeks4geeks is no. 1 4 geeks'

res1 = sum(1 for char in str1 if char.isdigit())

print('Count of numerics in string:', res1)
