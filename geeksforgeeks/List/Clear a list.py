list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 3]
list4 = [1, 2, 3]
list5 = [1, 2, 3]

list1.clear()

list2 *= 0

del list3[:]

list4 = list4[:0]

print('List after clear:\n', list1, '\n', list2, '\n', list3, '\n', list4)

'''
# Using clear()

list1 = [1, 2, 3]; list2 = [1, 2, 3]; list3 = [1, 2, 3]; list4 = [1, 2, 3]; list5 = [1, 2, 3]

# print('List before clear:', *list)

# clearing list

list1.clear()
list2 = []
list3 *= 0
del list4[:]
list5 = list5[:0]

print('List after clear:\n', list1, '\n', list2, '\n', list3, '\n', list4, '\n', list5)

# Version 2: by reinitializing the list
# list2 = [1, 2, 3]

# printing list before deleting
# print('List before deleting is:', str(list2))

# deleting list using reinitialization
# list2 = []

# printing list after reinitialization
# print('List after clearing using reinitialization:', str(list2))

# Version 3: using “*= 0”
# initializing lists
# list3 = [1, 2, 3]

# printing list before deleting
# print('List before clearing is:', str(list))

# list3 *= 0
# printing list after reinitialization
# print('List after clearing using *=0:', str(list3))

# Version 4: using del
# list4 = [1, 2, 3]

# printing list before deleting
# print('List before deleting is:', str(list4))

# deleting list using del
# del list4[:]
# print('List after clearing using del:', str(list4))

# Version 5: using slicing
# initializing list
# list51 = [1, 2, 3, 4, 5]

# print('List before clearing:', list51)
# clearing list using slicing
# list52 = list51[:0]
# print('List after clearing using Slicing:', list52)
'''
