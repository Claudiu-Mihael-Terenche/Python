def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    missing_number = total_sum - arr_sum
    return missing_number

# Take user input for the array
user_input = input("Enter numbers separated by spaces: ")
user_array = list(map(int, user_input.split()))

# Find the missing number
result = find_missing_number(user_array)

# Display the result
print(f"The missing number is: {result}")
