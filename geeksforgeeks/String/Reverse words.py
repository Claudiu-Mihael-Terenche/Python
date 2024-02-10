# Python code to reverse words in a given string

str1 = 'geeks quiz practice code'

str2 = str1.split()[::-1] # reversing words in a given string

item1 = []
for item2 in str2: item1.append(item2) # appending reversed words

res = ' '.join(item1)

print(res)
