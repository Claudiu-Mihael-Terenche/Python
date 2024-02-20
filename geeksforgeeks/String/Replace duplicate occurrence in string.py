str1 = 'Gfg is best. Gfg also has Classes now. Classes help understand better.'
repl_dict1 = {'Gfg': 'It', 'Classes': 'They'}

list1 = str1.split()

res1 = ' '.join([repl_dict1.get(val)
                 if val in repl_dict1.keys() and list1.index(val) != idx
                 else val for idx, val in enumerate(list1)])

print('The string after replacing:', res1)

'''
# Python3 code to demonstrate working of
# Replace duplicate Occurrence in String
# Using keys() + index() + list comprehension

# initializing string
str1 = 'Gfg is best . Gfg also has Classes now. Classes help understand better . '

# printing original string
# print('The original string is:', str(str1))

# initializing replace mapping
repl_dict1 = {'Gfg' : 'It', 'Classes' : 'They' }

# Replace duplicate Occurrence in String
# Using keys() + index() + list comprehension
list1 = str1.split()
res1 = ' '.join([repl_dict1.get(val)
                if val in repl_dict1.keys() and list1.index(val) != idx
                else val for idx, val in enumerate(list1)])

# printing result
print('The string after replacing:', str(res1))

# initializing string
# str2 = 'Gfg is best . Gfg also has Classes now. Classes help understand better.'

# printing original string
# print("The original string is : " + str(test_str))

# initializing replace mapping
# repl_dict2 = {'Gfg': 'It', 'Classes': 'They'}

# Replace duplicate Occurrence in String
# Using set() + loop + list comprehension
words = str1.split()
seen = set()
res2 = [repl_dict1[word] if word in repl_dict1 and word not in seen and not seen.add(word)
       else word for word in words]

# join the list of words to form the final string
res2 = ' '.join(res2)

# printing result
print('The string after replacing:', str(res2))
'''
