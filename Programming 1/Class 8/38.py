""" Replace every element with the next greatest element (from the right side) in a given array of integers.
There is no element next to the last element, therefore replace it with -1."""
def replace_with_next_greatest(arr):
    n = len(arr)

    # Initialize the rightmost element as -1
    max_from_right = -1

    # Iterate the array from right to left
    for i in range(n - 1, -1, -1):
        # Store the original value at index i
        original_value = arr[i]

        # Replace the element with the next greatest element from the right
        arr[i] = max_from_right

        # Update max_from_right if the original value is greater
        max_from_right = max(max_from_right, original_value)

    return arr

# Take user input for the array of integers
try:
    input_str = input("Enter the array of integers separated by spaces: ")
    input_arr = list(map(int, input_str.split()))

    # Call the function to replace elements with the next greatest
    result_arr = replace_with_next_greatest(input_arr)

    # Display the result
    print("Array after replacing with next greatest elements:", result_arr)

except ValueError:
    print("Please enter valid integers separated by spaces.")
