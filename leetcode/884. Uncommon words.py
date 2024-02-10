# 884. Uncommon words from two sentences https://leetcode.com/problems/uncommon-words-from-two-sentences/
# Claudiu Mihael Terenche, 6268599, FSD 10, 22.12.2023
"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
"""
# Python3 program to find a list of uncommon words using the set() and difference() method

# function to return all uncommon words
def UncommonWords(str1, str2):
    # split the strings str1 and str2 into words and create sets
    A = set(str1.split())
    B = set(str2.split())

    # find the uncommon words in A and B and combine them
    uncommonWords = A.difference(B).union(B.difference(A))

    # convert the set to a list and return
    return list(uncommonWords)


# driver code
str1 = 'this apple is sweet'
str2 = 'this apple is sour'

# print required answer without brackets
print(*UncommonWords(str1, str2))
