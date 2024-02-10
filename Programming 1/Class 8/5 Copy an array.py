"""def copy_array(original_array):
    # Create an empty array to store the copy
    copied_array = []

    # Iterate through each element in the original array
    for element in original_array:
        # Add the element to the copied array
        copied_array.append(element)

    # Return the copied array
    return copied_array

# Example usage:
original_array = [1, 2, 3, 4, 5]
copied_array = copy_array(original_array)

# Print the original and copied arrays
print("Original Array:", original_array)
print("Copied Array:", copied_array)"""

def copy_array(original_array):
    # Iterate through the original array and create a copy
    copied_array = []
    for element in original_array:
        copied_array.append(element)
    return copied_array

# Take input from the user
user_input = input("Enter elements of the array separated by space: ")
original_array = [int(x) for x in user_input.split()]

# Copy the array
copied_array = copy_array(original_array)

# Display the original and copied arrays
print("Original Array:", original_array)
print("Copied Array:", copied_array)
