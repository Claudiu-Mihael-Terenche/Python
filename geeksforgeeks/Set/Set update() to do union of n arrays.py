# Function to combine n arrays

def combineAll(arr):
    result = set(arr[0]) # cast first array as set and assign it to variable named as result
    for array in arr[1:]: # now traverse remaining list of arrays and take it's update with result variable
        result.update(array)
    return list(result)


if __name__ == '__main__':
    arr = [[1, 2, 2, 4, 3, 6], [5, 1, 3, 4], [9, 5, 7, 1], [2, 4, 1, 3]]
    print(combineAll(arr))
