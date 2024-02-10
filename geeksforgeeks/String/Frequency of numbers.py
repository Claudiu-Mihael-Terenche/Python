# Python3 code to print frequency of numbers in string using map

str1 = 'geeks4feeks is no. 1 4 geeks'

res1 = sum(map(str.isdigit, str1))

print('Count of numerics in string:', res1)
