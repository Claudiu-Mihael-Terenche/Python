# Python3 code to check substring presence in a strings list using list comprehension + any()
list1 = ['Gfg', 'is', 'Best']
list2 = ['I love Gfg', 'Its Best for Geeks', 'Gfg means CS']

res = [True if any(item1 in item2 for item2 in list2) else False for item1 in list1]

print('The match list:', res)
