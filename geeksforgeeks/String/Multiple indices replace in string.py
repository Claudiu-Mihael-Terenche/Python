# Using replace() method inside a loop
str1 = 'Geeksforgeeks is best'
list1 = [2, 4, 7, 10]
char = '*'

for index in list1:
    str1 = str1[:index] + char + str1[index + 1:]

print('The string after performing replace:', str1)
