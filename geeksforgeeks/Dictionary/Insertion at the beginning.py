from collections import OrderedDict
dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
dict2 = OrderedDict([('manjeet', '4'), ('akash', '4')])

both = OrderedDict(list(dict2.items()) + list(dict1.items()))  # adding in a beginning of dict

print('Resultant dictionary:', both)

dict1.update({'manjeet': '4'})

dict1.move_to_end('manjeet', last=False)

print('Resultant dictionary:', dict1)

'''
# Python code to demonstrate
# insertion of items in beginning of ordered dict
from collections import OrderedDict

dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
dict2 = OrderedDict([('manjeet', '4'), ('akash', '4')])

both = OrderedDict(list(dict2.items()) + list(dict1.items())) # adding in beginning of dict

print('Resultant dictionary:', both)

# Python code to demonstrate insertion of items in beginning of ordered dict
# from collections import OrderedDict

# Initialising ordered_dict
# inordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])

# Inserting items in starting of dict

dict1.update({'manjeet': '4'})

dict1.move_to_end('manjeet', last=False)

print('Resultant dictionary:', dict1)
'''
