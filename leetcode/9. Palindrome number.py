# 9. Palindrome number https://leetcode.com/problems/palindrome-number/
# Claudiu Mihael Terenche, 6268599, FSD 10, 22.12.2023
"""
Given an integer x, return true if x is a palindrome, and false otherwise.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore, it is not a palindrome.
"""
# A palindrome is a word, phrase, or sequence that reads the same backward as forward.
# driver code
num1 = -121

# Using str() function to transform the number into a string
str1 = str(num1)

'''
# Using conditional statement to check if the new created string is the same as its reverse.
if str1 == str1[::-1]:
    print(num1, 'the number is a palindrome')
else:
    print(num1, 'the number is not a palindrome')
'''

res = str1 == str1[::-1]
print('Is the number ' + str(num1) + ' palindrome?:', res)
