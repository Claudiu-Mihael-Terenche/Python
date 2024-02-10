def reverse_array(arr):
    return arr[::-1]

# Take input from the user
try:
    input_string = input("Enter integers separated by spaces: ")
    input_array = list(map(int, input_string.split()))

    # Reverse the array
    reversed_array = reverse_array(input_array)

    # Display the result
    print("Original Array:", input_array)
    print("Reversed Array:", reversed_array)

except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
