# Using lambda function
str1 = 'thishasboth29'
str2 = 'geeksforgeeks'

res1 = any(item.isalpha() for item in str1) and any(item.isdigit() for item in str1)
res2 = any(item.isalpha() for item in str2) and any(item.isdigit() for item in str2)

print('str1', res1, '\nstr2', res2)
