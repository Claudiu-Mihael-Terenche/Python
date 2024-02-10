# Using list comprehension+ loop + max() + len()

str1 = 'geeksgeeks are geeks for all geeksgeeksgeeks'

sub_str = 'geeks'

max_sub = max([sub_str * n for n in range(len(str1) // len(sub_str) + 1) if sub_str * n in str1], key=len)

print('The maximum run of substring:', max_sub)
