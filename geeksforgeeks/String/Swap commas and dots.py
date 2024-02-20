# Using replace()
str1 = '14, 625, 498.002'

str1 = str1.replace(', ', 'a')
str1 = str1.replace('.', ', ')
str1 = str1.replace('a', '.')

print(str1)

# Approach 2: using split and join
str2 = '14, 625, 498.002'

str2 = 'b'.join(str2.split(', '))
str2 = ', '.join(str2.split('.'))
str2 = '.'.join(str2.split('b'))

print(str2)


# Approach 3: Python code to replace, with 'and' vice versa using simple for loop and join method

def replace3(str03):
    arr = []

    for item in str03:
        if item == '.':
            arr.append(', ')
        elif item == ',':
            arr.append('.')
            continue
        elif item == ' ':
            continue
        else:
            arr.append(item)

    str03 = ''.join(arr)
    return str03


str3 = '14, 625, 498.002'
print(replace3(str3))
