# Python3 code to create mirror image of string using string slicing and lookup dictionary
str1 = 'void'
mir_dict = {'b': 'd', 'd': 'b', 'i': 'i', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x'}

str1 = str1[::-1]  # reverse the input string

res = ''
for item in str1:
    if item in mir_dict:
        res += mir_dict[item]
    else:
        res = 'Not possible'
        break

print('The mirror string:', res)
