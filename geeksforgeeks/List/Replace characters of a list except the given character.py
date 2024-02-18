list1 = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
repl_chr = '$'
ret_chr = 'G'

res = [item if item == ret_chr else repl_chr for item in list1]

print('List after replacement:', res)

'''
# Python3 code to replace all characters except K using list comprehension and conditional expressions

# initializing lists

list1 = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']

# printing original list
# print('The original list:', str(list1))

# initializing repl_chr

repl_chr = '$'

ret_chr = 'G' # initializing retain character

# list comprehension to remake list after replacement
res = [item if item == ret_chr else repl_chr for item in list1]

print('List after replacement:', res)
'''
