list1 = ['gfg', ' ', ' ', 'is', '		 ', 'best']

res = [item for item in list1 if item.strip()]

print('List after filtering non-empty strings:', res)

'''
# Python3 code to remove multiple empty spaces from string list using list comprehension + strip()

# initializing list

list1 = ['gfg', ' ', ' ', 'is', '		 ', 'best']

# printing original list
# print('The original list is:', str(list1))

# remove multiple empty spaces from string list using list comprehension + strip()

res = [item for item in list1 if item.strip()]

print('List after filtering non-empty strings:', res)
'''
