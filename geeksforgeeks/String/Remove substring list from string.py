# Using loop + replace()
str1 = 'gfg is best for all geeks'
sub_list = ['best', 'all']

for sub in sub_list:
    str1 = str1.replace(sub + ' ', '')

print('The string after substring removal:', str1)
