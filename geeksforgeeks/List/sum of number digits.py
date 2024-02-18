# Creating an expression without changing to a string
list1 = [12, 67, 98, 34]
# sum of number digits in list (creating an expression)

res = list(sum(int(digit) for digit in str(num)) for num in list1)

print('List integer summation:', list(res))
