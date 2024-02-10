# 151. Reverse words in a string https://leetcode.com/problems/reverse-words-in-a-string/
# Claudiu Mihael Terenche, 6268599, FSD 10, 22.12.2023
"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"
"""
# driver code
str1 = 'the sky is blue'
# reversing words in a given string using split() method to keep words
str2 = str1.split()[::-1]
item1 = []
for item2 in str2:
    # appending reversed words
    item1.append(item2)
# printing reverse words
print(' '.join(item1))
