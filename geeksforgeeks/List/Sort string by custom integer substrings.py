import re
list1 = ['Good at 4', 'Wake at 7', 'Work till 6', 'Sleep at 11']
suborder_list = ['6', '7', '4', '11']

temp_dict = {item_d: key for key, item_d in enumerate(suborder_list)}

temp_list = sorted([[item_l, temp_dict[re.search('(\\d+)$', item_l).group()]]
                    for item_l in list1], key=lambda x: x[1])

res = [item_l for item_l in list(zip(*temp_list))[0]]

print('The sorted list:', res)

'''
# Python3 code to sort string by custom substrings using sorted() + zip() + lambda + regex()
import re
list1 = ['Good at 4', 'Wake at 7', 'Work till 6', 'Sleep at 11']

# printing original list
# print('The original list:', str(list1))

# initializing substring list

suborder_list = ['6', '7', '4', '11']

temp_dict = {item_d: key for key, item_d in enumerate(suborder_list)} # creating inverse mapping with index

# custom sorting
temp_list = sorted([[item_l, temp_dict[re.search('(\\d+)$', item_l).group()]]
                    for item_l in list1], key=lambda x: x[1])

res = [item_l for item_l in list(zip(*temp_list))[0]] # compiling result

print('The sorted list:', res)
'''
