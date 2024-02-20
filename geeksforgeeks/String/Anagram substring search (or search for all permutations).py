str1 = 'BACDGABCDA'
pat = 'ABCD'

for i in range(len(str1) - len(pat) + 1):
    if sorted(pat) == sorted(str1[i:i + len(pat)]):
        print(i)
