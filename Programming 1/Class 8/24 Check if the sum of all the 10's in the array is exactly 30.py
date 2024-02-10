def check_sum_of_tens(arr):
    # Calculate the sum of all 10s in the array
    sum_of_tens = sum(num for num in arr if num == 10)

    # Check if the sum is exactly 30
    return sum_of_tens == 30

# Take user input for the array
try:
    input_str = input("Enter elements of the array separated by spaces: ")
    # Convert input string to a list of integers
    user_array = list(map(int, input_str.split()))
except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
else:
    # Check and display the result
    result = check_sum_of_tens(user_array)
    print(f"Result: {result}")
