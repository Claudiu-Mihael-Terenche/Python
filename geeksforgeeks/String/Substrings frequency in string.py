# Python3 code to find all substrings frequencies in string using list comprehension
str1 = 'abababa'

res = dict()
for ele in [str1[idx: j] for idx in range(len(str1)) for j in range(idx + 1, len(str1) + 1)]:
    res[ele] = 1 if ele not in res.keys() else res[ele] + 1

print('Extracted frequency dictionary:', res)
