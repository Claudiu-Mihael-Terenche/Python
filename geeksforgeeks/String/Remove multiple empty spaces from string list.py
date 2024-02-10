list1 = ['gfg', ' ', ' ', 'is', '		 ', 'best']

res1 = []
for item1 in list1:
    if item1.find(' ') == -1:
        res1.append(item1)

res2 = [item for item in list1 if not item.isspace()]

res3 = [item for item in list1 if item.strip()]

print('List after filtering non-empty strings:\n', res1, '\n', res2, '\n', res3)

'''
# Python3 code to remove multiple empty spaces from string list using find()

# initializing list
list1 = ['gfg', ' ', ' ', 'is', '		 ', 'best']

# printing original list
# print('The original list is:', str(list1))

# remove multiple empty spaces from string list using find()
res1 = []
for item1 in list1:
    if item1.find(' ') == -1:
        res1.append(item1)

# printing result
print('List after filtering non-empty strings:', str(res1))

# Version 2: using str.isspace()
# initializing list
list2 = ['gfg', ' ', ' ', 'is', ' ', 'best']

# printing original list
# print('The original list is:', str(list2))

# remove multiple empty spaces from string list
res2 = [item2 for item2 in list2 if not item2.isspace()]

# printing result
print('List after filtering non-empty strings:', str(res2))

# Version 3: Python3 code to remove multiple empty spaces from string list using list comprehension + strip()

# initializing list
list3 = ['gfg', ' ', ' ', 'is', '		 ', 'best']

# printing original list
# print('The original list is:', str(list3))

# remove multiple empty spaces from string list using list comprehension + strip()
res3 = [item3 for item3 in list3 if item3.strip()]

# printing result
print('List after filtering non-empty strings:', str(res3))
'''
