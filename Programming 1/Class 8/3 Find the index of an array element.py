"""def find_index(arr, element):
    try:
        index = arr.index(element)
        return index
    except ValueError:
        return f"The element '{element}' is not present in the array."

# Example usage:
my_array = [10, 20, 30, 40, 50]
search_element = 30

result = find_index(my_array, search_element)

print(result)"""

def find_element_index(arr, element):
    try:
        index = arr.index(element)
        return index
    except ValueError:
        return -1  # Return -1 if the element is not found in the array

# Take input from the user for the array
arr = input("Enter the array (space-separated elements): ").split()

# Take input from the user for the element to find
element = input("Enter the element to find: ")

try:
    # Try converting elements to appropriate data types (e.g., int or float)
    arr = [int(x) for x in arr]
    element = int(element)
except ValueError:
    print("Invalid input. Please enter valid integers.")

# Call the function to find the index of the element
index = find_element_index(arr, element)

# Display the result
if index != -1:
    print(f"The index of {element} in the array is: {index}")
else:
    print(f"{element} is not present in the array.")
