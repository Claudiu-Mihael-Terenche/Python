# Using replace()

def Replace(str1):
    str1 = str1.replace(', ', 'a')
    str1 = str1.replace('.', ', ')
    str1 = str1.replace('a', '.')
    return str1


str1 = '14, 625, 498.002'
print(Replace(str1))

# Approach 2: using split and join

def Replace(str2):
	str2 = 'b'.join(str2.split(', '))
	str2 =', '.join(str2.split('.'))
	str2 ='.'.join(str2.split('b'))
	return str2

str2 = '14, 625, 498.002'
print(Replace(str2))

# Approach 3: Python code to replace, with . and vice-versa using simple for loop and join method

def Replace(str3):
    arr = []

    for item in str31:
        if (item == '.'):
            arr.append(', ')
        elif (item == ','):
            arr.append('.')
            continue
        elif (item == ' '):
            continue
        else:
            arr.append(item)

    str32 = ''.join(arr)
    return str32


str31 = '14, 625, 498.002'
print(Replace(str31))
