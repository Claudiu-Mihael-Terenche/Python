import re

list1 = ['Good at 4', 'Wake at 7', 'Work till 6', 'Sleep at 11']

subord_list = ['6', '7', '4', '11']

temp_dict = {itemd: key for key, itemd in enumerate(subord_list)}

temp_list = sorted([[iteml, temp_dict[re.search("(\d+)$", iteml).group()]] \
                    for iteml in list1], key=lambda x: x[1])

res = [iteml for iteml in list(zip(*temp_list))[0]]

print('The sorted list:', res)

'''
# Python3 code to sort string by custom substrings using sorted() + zip() + lambda + regex()
import re
list1 = ['Good at 4', 'Wake at 7', 'Work till 6', 'Sleep at 11']

# printing original list
# print('The original list:', str(list1))

# initializing substring list

subord_list = ['6', '7', '4', '11']

temp_dict = {itemd: key for key, itemd in enumerate(subord_list)} # creating inverse mapping with index

# custom sorting
temp_list = sorted([[iteml, temp_dict[re.search("(\d+)$", iteml).group()]] \
                    for iteml in list1], key=lambda x: x[1])

res = [iteml for iteml in list(zip(*temp_list))[0]] # compiling result

print('The sorted list:', res)
'''
