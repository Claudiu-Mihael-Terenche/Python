list1 = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
subs = 'Geek'

res = len([item for item in list1 if subs in item])

print('All strings count with given substring are:', res)

'''
# Python code to count strings with substring string list using list comprehension + len()

list1 = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

# printing original list
# print ('The original list is:', str(list1))

# initializing substring

subs = 'Geek'

# using list comprehension + len() count strings with substring string list
res = len([item for item in list1 if subs in item])

print ('All strings count with given substring are:', res)
'''
