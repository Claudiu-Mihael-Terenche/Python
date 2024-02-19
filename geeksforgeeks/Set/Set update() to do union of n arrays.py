# Function to combine n arrays

def combine_all(arr):
    result = set(arr[0])  # cast a first array as a set and assign it to variable named as a result
    for array in arr[1:]:  # now traverse the remaining list of arrays and take its update with result variable
        result.update(array)
    return list(result)


if __name__ == '__main__':
    arr1 = [[1, 2, 2, 4, 3, 6], [5, 1, 3, 4], [9, 5, 7, 1], [2, 4, 1, 3]]
    print(combine_all(arr1))
