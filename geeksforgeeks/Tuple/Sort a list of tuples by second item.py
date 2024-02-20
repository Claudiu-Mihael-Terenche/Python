tup = [('ravish', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]
K = 1

tup.sort(key=lambda x: x[K])

print(tup)

'''
# Python program to sort a list of tuples by the second Item using sort()

# function to sort the list by second item of tuple

def Sort_Tuple(tup):
tup.sort(key=lambda x: x[1]) # reverse = None (sorts in ascending order) key is set to sort
return tup                   # using second element of sublist lambda has been used

tup = [('ravish', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]

print(Sort_Tuple(tup))

tup = [('ravish', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]

K = 1

tup.sort(key=lambda x: x[K])

print(tup)
'''
