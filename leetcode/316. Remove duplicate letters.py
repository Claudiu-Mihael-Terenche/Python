# 316. Remove duplicate letters https://leetcode.com/problems/remove-duplicate-letters/
# Claudiu Mihael Terenche, 6268599, FSD 10, 22.12.2023
"""
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.
Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
"""
# driver code
str1 = 'cbacdcbc'

# eliminating the duplicates
str2 = ''
for item in str1:
    if item not in str2:
        str2 = str2 + item

# print result without brackets
print(*sorted(str2))
