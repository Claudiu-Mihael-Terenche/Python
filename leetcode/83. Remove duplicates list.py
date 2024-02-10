# 83. Remove duplicates from sorted list https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Claudiu Mihael Terenche, 6268599, FSD 10, 22.12.2023
"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""
# driver code
list1 = [1, 1, 2, 3, 3]

# Using set() method to remove duplicates
list2 = set(list1)

# print result without brackets
print(*list2)
