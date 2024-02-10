def move_zeros_to_end(arr):
    non_zeros = [num for num in arr if num != 0]
    zeros = [0] * (len(arr) - len(non_zeros))
    result = non_zeros + zeros
    return result

# Taking user input for the array
user_input = input("Enter elements of the array separated by spaces: ")
user_array = list(map(int, user_input.split()))

# Calling the function to move zeros to the end
result_array = move_zeros_to_end(user_array)

# Displaying the result
print("Original Array:", user_array)
print("Modified Array:", result_array)
