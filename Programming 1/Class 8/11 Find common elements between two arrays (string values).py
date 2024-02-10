def find_common_elements(array1, array2):
    common_elements = set(array1) & set(array2)
    return list(common_elements)

# Take input from the user
array1 = input("Enter elements of the first array (comma-separated): ").split(',')
array2 = input("Enter elements of the second array (comma-separated): ").split(',')

# Find and display common elements
common_elements = find_common_elements(array1, array2)

if common_elements:
    print(f"Common elements: {', '.join(common_elements)}")
else:
    print("No common elements found.")
