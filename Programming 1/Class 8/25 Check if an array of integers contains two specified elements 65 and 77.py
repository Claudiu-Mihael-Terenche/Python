def check_elements(arr, element1, element2):
    return element1 in arr and element2 in arr

# Take user input for the array
try:
    # Python 2
    user_input = raw_input("Enter the array of integers (comma-separated): ")
except NameError:
    # Python 3
    user_input = input("Enter the array of integers (comma-separated): ")

# Convert the user input to a list of integers
user_array = list(map(int, user_input.split(',')))

# Specify the elements to check
element1 = 65
element2 = 77

# Check if the array contains both specified elements
result = check_elements(user_array, element1, element2)

# Display the result
if result:
    print(f"The array contains both {element1} and {element2}.")
else:
    print(f"The array does not contain both {element1} and {element2}.")
