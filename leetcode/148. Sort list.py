# 148. Sort list https://leetcode.com/problems/sort-list/
# Claudiu Mihael Terenche, 6268599, FSD 10, 22.12.2023
"""
Given the head of a linked list, return the list after sorting it in ascending order.
Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
"""
# driver code
list1 = [-1, 5, 3, 4, 0]

# Using sorted() method to sort the items in numerical order
list2 = sorted(list1)

# print result without brackets
print(*list2)
