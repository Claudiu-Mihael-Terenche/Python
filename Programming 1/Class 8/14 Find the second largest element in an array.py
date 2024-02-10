def find_second_largest(arr):
    # Ensure that the array has at least two elements
    if len(arr) < 2:
        return "Array should have at least two elements"

    # Sort the array in descending order
    arr.sort(reverse=True)

    # Return the second element, which is the second-largest
    return arr[1]

# Get input from the user
try:
    # Convert input elements to integers
    input_array = [int(x) for x in input("Enter the array elements separated by space: ").split()]

    # Find the second largest element
    result = find_second_largest(input_array)

    # Display the result
    print("The second largest element is:", result)

except ValueError:
    print("Invalid input. Please enter integers separated by space.")
except Exception as e:
    print(f"An error occurred: {e}")
