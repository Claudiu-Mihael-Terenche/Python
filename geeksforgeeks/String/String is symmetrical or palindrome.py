str = 'amaama'

half = int(len(str) / 2)

first_str = str[:half]
second_str = str[half:]

res1 = first_str == second_str

print('Is the string ' + str + ' symmetrical?:', res1)

res2 = first_str == second_str[::-1]

print('Is the string ' + str + ' palindrome?:', res2)

str1 = 'A man, a plan, a canal: Panama'

str1 = str1.translate({ord(item): None for item in ' ,:'}).lower()

res = str1 == str1[::-1]

print('Is the string ' + str1 + ' palindrome?:', res)

'''
# Using slicing method

str = 'amaama'
half = int(len(str) / 2)

first_str = str[:half]
second_str = str[half:]

# symmetric
if first_str == second_str:
	print(str, 'string is symmetrical')
else:
	print(str, 'string is not symmetrical')

# palindrome
if first_str == second_str[::-1]: # ''.join(reversed(second_str)) [slower]
	print(str, 'string is palindrome')
else:
	print(str, 'string is not palindrome')

res1 = first_str == second_str
print('Is the string ' + str + ' symmetrical?:', res1)

res2 = first_str == second_str[::-1]
print('Is the string ' + str + ' palindrome?:', res2)

# 125. Valid palindrome https://leetcode.com/problems/valid-palindrome/
# Claudiu Mihael Terenche, 6268599, FSD 10, 22.12.2023
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

str1 = 'A man, a plan, a canal: Panama'

# We need to eliminate the special characters, to concatenate the words in a single word.
# Also, we need to change all the letters to lower cases.

# Using translate() method to eliminate the special characters,
# and lower() method to change the letters to lower cases.

str1 = str1.translate({ord(item): None for item in ' ,:'}).lower()

# Using conditional statement to check if the new created string is the same as its reverse.
if str1 == str1[::-1]:
    print(str1, 'string is palindrome')
else:
    print(str1, 'string is not palindrome')

res = str1 == str1[::-1]

print('Is the string ' + str1 + ' palindrome?:', res)
'''
