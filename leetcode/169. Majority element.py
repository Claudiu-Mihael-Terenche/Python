# 169. Majority element https://leetcode.com/problems/majority-element/
# Claudiu Mihael Terenche, 6268599, FSD 10, 22.12.2023
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
# Python 3 code to print the most frequent character in string using collections.Counter() + max()
from collections import Counter

# initializing string
list1 = [2, 2, 1, 1, 1, 2, 2]

# using collections.Counter() + min() to get least frequent character in string
res1 = max(Counter(list1), key=Counter(list1).get)

# printing result
print('The majority element in list1 is:', str(res1))
