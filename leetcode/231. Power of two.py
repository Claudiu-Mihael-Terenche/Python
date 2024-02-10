# 231. Power of two https://leetcode.com/problems/power-of-two/
# Claudiu Mihael Terenche, 6268599, FSD 10, 22.12.2023
"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1
"""
# driver code
n = 1

# using conditional statement taking into account 2 ** 0 == 1 as exception
if n == 1 or n % 2 == 0:
    print('True')
else:
    print('False')
