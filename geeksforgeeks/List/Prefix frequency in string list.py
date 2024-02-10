list1 = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']

sub = 'gfg'

res = sum(sub.startswith(sub) for sub in list1)

print('Strings count with matching frequency:', res)

'''
# Python3 code to prefix frequency in list using sum() + startswith()

# initializing list

list1 = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']

# printing original list
# print('The original list is:', str(test_list1))

# initializing substring

test_sub = 'gfg'

res = sum(sub.startswith(test_sub) for sub in list1) # prefix frequency in list using sum() + startswith()

print('Strings count with matching frequency:', res)
'''
