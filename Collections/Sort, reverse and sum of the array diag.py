arr1 = ([22, 50, 11, 2, 49])

# A. Write A Method SortArray To Sort One Dimensional Array In Descending Order

arr1_sorted = sorted(arr1)

print(arr1_sorted)

# B. Write A ProĀram To Print One Dimensional Array In Reverse Order

arr1_reversed = arr1[::-1]

print(arr1_reversed)

# C. Write A Program To Add The Diagonal Of Two-Dimensional Array

arr2 = [[22, 50, 11, 2, 49],
        [92, 63, 12, 64, 37],
        [75, 23, 64, 12, 99],
        [21, 25, 71, 69, 39],
        [19, 39, 58, 28, 83]]

print(sum([arr2[i][i] for i in range(len(arr2))]))
