from collections import Counter
list1 = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
K = 2

res1 = [num for num, cnt in Counter(list1).items() if cnt > K]

res2 = list(filter(lambda num: Counter(list1)[num] > K, Counter(list1)))

print('The required elements:\n', *res1, '\n', *res2)

'''
# Python3 code to extract elements with frequency greater than K using list comprehension + Counter()
from collections import Counter


list1 = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]

# printing string
# print("The original list : " + str(list1))

# initializing K

K1 = 2

res1 = [num for num, cnt in Counter(list1).items() if cnt > K1] # using list comprehension to bind result

# printing results
# print('The required elements:', str(res1))

# Version 2: using filter and lambda
# from collections import Counter

# list2 = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
# K2 = 2

freq_dict = Counter(list1)

res2 = list(filter(lambda num: freq_dict[num] > K1, freq_dict))

print('The required elements:\n', *res1, '\n', *res2)
'''
