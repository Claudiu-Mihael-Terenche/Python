# Using lambda function

checkString = lambda str: any(item.isalpha() for item in str) and any(item.isdigit() for item in str)


print(checkString('thishasboth29'))

print(checkString('geeksforgeeks'))
