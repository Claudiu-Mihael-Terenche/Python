tup = [("Amanda", 28), ("Senate", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]

res = sorted(tup, key=lambda x: x[0])

print(res)

'''
# Python program to sort a list of
# tuples using sorted()

# Function to sort the list
# reverse = None (Sorts in Ascending order)
# key is set to sort using first element of
# sublist lambda has been used

# def Sort_Tuple(tup): return sorted(tup, key=lambda x: x[0])

# tup = [("Amanda", 28), ("Senate", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]

# print(Sort_Tuple(tup))

tup = [("Amanda", 28), ("Senate", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]

res = sorted(tup, key=lambda x: x[0])

print(res)
'''
