"""Sort an array of positive integers from an array.
In the sorted array the value of the first element should be maximum, the second value should be a minimum,
third should be the second maximum, the fourth should be the second minimum and so on."""
def sort_alternate(arr):
    # Sort the array in ascending order
    arr.sort()

    # Initialize an array to store the result
    result = [0] * len(arr)

    # Fill the result array with alternating max and min values
    i, j = 0, len(arr) - 1
    for k in range(len(arr)):
        if k % 2 == 0:
            result[k] = arr[j]
            j -= 1
        else:
            result[k] = arr[i]
            i += 1

    return result

# Take user input for the array
input_str = input("Enter space-separated positive integers: ")
user_array = list(map(int, input_str.split()))

# Call the function and display the result
result_array = sort_alternate(user_array)
print("Sorted Array with Alternating Max and Min Values:", result_array)
