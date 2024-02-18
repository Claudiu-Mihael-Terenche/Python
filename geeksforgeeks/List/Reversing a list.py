# Using reverse()
list1 = [10, 11, 12, 13, 14, 15]
list2 = [10, 11, 12, 13, 14, 15]
list3 = [10, 11, 12, 13, 14, 15]

list1.reverse()

print(list1)

# Version 2: using reversed()

res2 = list(reversed(list2))

print(res2)

res3 = list3[::-1]

print(res3)
