# Python3 code to remove K length duplicates from string using loop + slicing

str1 = 'geeksforfreeksfo'

K = 3

memo = set()
res = []
for idx in range(0, len(str1) - K):
    sub = str1[idx: idx + K] # slicing K length substrings
    if sub not in memo: # checking for presence
        memo.add(sub)
        res.append(sub)

res = ''.join(res[item] for item in range(0, len(res), K))

print('The modified string:', res)
