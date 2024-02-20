str1 = 'gekseforgeeks'
arg_str = 'geeks'

res = min(str1.count(char) // arg_str.count(char) for char in set(arg_str))

print('Possible substrings count:', res)
