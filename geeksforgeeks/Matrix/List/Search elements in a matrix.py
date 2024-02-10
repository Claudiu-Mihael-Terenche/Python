# Using any() + list comprehension

list1 = [[4, 5, 6], [10, 2, 13], [1, 11, 18]]

res = any(13 in sub for sub in list1)

print('Is 13 present in Matrix?:', res)
