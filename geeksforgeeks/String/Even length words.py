# Python code to print even length words using list comprehension

str1 = 'geeks for geek'

str2 = str1.split(' ')

res = [item for item in str2 if len(item) % 2 == 0]

print(*res)
