# Python3 code reverse all strings in string list using list comprehension

list1 = ['geeks', 'for', 'geeks', 'is', 'best']

res = [item[::-1] for item in list1]

print ('The reversed string list is:', res)
