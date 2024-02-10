def remove_duplicates(arr):
    # Use a set to store unique elements
    unique_elements = set()

    # Use a list to maintain the order of elements
    result = []

    for element in arr:
        if element not in unique_elements:
            result.append(element)
            unique_elements.add(element)

    return result

# Take user input for the array
user_input = input("Enter elements of the array separated by spaces: ")
input_array = list(map(int, user_input.split()))

# Remove duplicates and get the updated array
updated_array = remove_duplicates(input_array)

# Print the updated array and its length
print("Updated Array:", updated_array)
print("Updated Array Length:", len(updated_array))
