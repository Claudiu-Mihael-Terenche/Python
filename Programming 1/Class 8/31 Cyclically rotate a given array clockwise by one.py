def rotate_array_clockwise(arr):
    n = len(arr)
    last_element = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last_element

# Take user input for the array
input_str = input("Enter the array elements separated by spaces: ")
user_array = list(map(int, input_str.split()))

# Perform cyclic rotation
rotate_array_clockwise(user_array)

# Display the rotated array
print("Rotated array:", user_array)
