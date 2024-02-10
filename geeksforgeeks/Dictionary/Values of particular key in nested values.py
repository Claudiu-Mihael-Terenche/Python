dict1 = {'Gfg': {'a': 7, 'b': 9, 'c': 12}, 'is': {'a': 15, 'b': 19, 'c': 20}, 'best': {'a': 5, 'b': 10, 'c': 2}}

temp = 'c'

res1 = []
for value in dict1.values():
    if temp in value:
        res1.append(value[temp])

res2 = [sub[temp] for sub in dict1.values() if temp in sub.keys()]

res3 = [val[temp] for key, val in dict1.items() if temp in val]

print('The extracted values:\n', res1, '\n', res2, '\n', res3)

'''
# Using a for loop and if condition

dict1 = {'Gfg': {'a': 7, 'b': 9, 'c': 12}, 'is': {'a': 15, 'b': 19, 'c': 20}, 'best': {'a': 5, 'b': 10, 'c': 2}}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

temp = 'c'

res1 = []
for value in dict1.values(): # iterating over each value in dictionary
    if temp in value: # checking if key exists in current value
        res1.append(value[temp]) # appending value of key to the result list

# print('The extracted values:', res1)

# Python3 code to demonstrate working of extract values of particular Key in nested values
# using list comprehension + values() + keys()

# dict1 = {'Gfg' : {"a" : 7, "b" : 9, "c" : 12},
         # 'is' : {"a" : 15, "b" : 19, "c" : 20},
         # 'best' :{"a" : 5, "b" : 10, "c" : 2}}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# temp = 'c'

# using keys() and values() to extract values

res2 = [sub[temp] for sub in dict1.values() if temp in sub.keys()]

# print('The extracted values:', res2)

# Python3 code to demonstrate working of extract values of Particular Key in Nested Values
# using list comprehension

# test_dict = {'Gfg' : {"a" : 7, "b" : 9, "c" : 12},
			# 'is' : {"a" : 15, "b" : 19, "c" : 20},
			# 'best' :{"a" : 5, "b" : 10, "c" : 2}}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# temp = "c"

# using item() to extract key value pair as whole

res3 = [val[temp] for key, val in dict1.items() if temp in val]

print('The extracted values:\n', res1, '\n', res2, '\n', res3)
'''
