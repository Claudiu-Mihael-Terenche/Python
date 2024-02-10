# Python3 code to reverse sort a string using join() + sorted() + reverse

str1 = 'geekforgeeks'

res = ''.join(sorted(str1, reverse=True))

print('String after reverse sorting:', res)
