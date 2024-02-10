dict1 = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}

K = 2

res = [dict(list(dict1.items())[i:i + K]) for i in range(0, len(dict1), K)]

print('The converted list:', res)

'''
# Python3 code to demonstrate working of
# Convert dictionary to K Keys dictionaries
# Using dictionary comprehension

# initializing dictionary

dict1 = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}

# printing original dictionary
# print("The original dictionary is : " + str(test_dict))

# initializing K

K = 2

# using dictionary comprehension to create list of sub-dictionaries
res = [dict(list(dict1.items())[i:i + K]) for i in range(0, len(dict1), K)]

print('The converted list:', res)
'''
