list1 = [12, 10, 13, 15, 8, 9]
list2 = [12, 10, 13, 15, 8, 9]
list3 = [12, 10, 13, 15, 8, 9]

set1 = set(list1)

while set1:
    set1.discard(max(set1))
    print(set1, end=' ')

print('\r')

set2 = set(list2)

while set2:
    set2.pop()
    print(set2, end=' ')

print('\r')

set3 = set(list3)

for i in range(len(set3)):
    set3.remove(next(iter(set3)))
    print(set3, end=' ')
