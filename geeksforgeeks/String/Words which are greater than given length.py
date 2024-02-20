str1 = 'hello geeks for geeks is computer science portal'
length = 4

res = [word for word in str1.split() if len(word) > length]

print(*res)
