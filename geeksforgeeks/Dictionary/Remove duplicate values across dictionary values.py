from collections import Counter

dict1 = {'Manjeet': [1, 4, 5, 6], 'Akash': [1, 8, 9], 'Nikhil': [10, 22, 4], 'Akshat': [5, 11, 22]}

cnt = Counter()
for idx in dict1.values(): cnt.update(idx)

res1 = {idx: [key for key in j if cnt[key] == 1] for idx, j in dict1.items()}

flat_list = [val for sublist in dict1.values() for val in sublist]

unique_values = [val for val, count in Counter(flat_list).items() if count == 1]

res2 = {key: [val for val in values if val in unique_values] for key, values in dict1.items()}

print('Uncommon elements records:\n', res1, '\n', res2)

'''
# Python3 code to demonstrate working of
# Remove duplicate values across Dictionary Values
# Using Counter() + list comprehension
from collections import Counter

dict1 = {'Manjeet': [1, 4, 5, 6], 'Akash': [1, 8, 9], 'Nikhil': [10, 22, 4], 'Akshat': [5, 11, 22]}

# printing original dictionary
# print("The original dictionary : " + str(test_dict))

# Remove duplicate values across Dictionary Values
# Using Counter() + list comprehension

cnt = Counter()
for idx in dict1.values(): cnt.update(idx)

res1 = {idx: [key for key in j if cnt[key] == 1] for idx, j in dict1.items()}

# print('Uncommon elements records:', res1)

# Using list comprehension and dictionary
# Python3 code to demonstrate working of
# Remove duplicate values across Dictionary Values
# from collections import Counter

# initializing dictionary
# dict2 = {'Manjeet': [1, 4, 5, 6], 'Akash': [1, 8, 9], 'Nikhil': [10, 22, 4], 'Akshat': [5, 11, 22]}

# printing original dictionary
# print("The original dictionary : " + str(test_dict))

# Remove duplicate values across Dictionary Values

flat_list = [val for sublist in dict1.values() for val in sublist]

unique_values = [val for val, count in Counter(flat_list).items() if count == 1]

res2 = {key: [val for val in values if val in unique_values] for key, values in dict1.items()}

print('Uncommon elements records:\n', res1, '\n', res2)
'''
