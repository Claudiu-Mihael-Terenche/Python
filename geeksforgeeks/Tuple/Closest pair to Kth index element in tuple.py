# Using a lambda function and the min() function
list1 = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
tup = (17, 23)
K = 1

res = min(list1, key=lambda item: abs(item[K - 1] - tup[K - 1]))  # using a lambda function and the min() function

print('The nearest tuple to Kth index element is:', res)
