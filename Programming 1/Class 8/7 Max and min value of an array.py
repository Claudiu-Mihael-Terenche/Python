def find_max_min(arr):
    if not arr:
        return None, None  # Return None for both max and min if the array is empty

    max_val = min_val = arr[0]  # Initialize max and min with the first element

    for num in arr:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num

    return max_val, min_val

# Take input from the user
try:
    input_str = input("Enter elements of the array separated by spaces: ")
    input_arr = list(map(int, input_str.split()))

    # Call the function to find max and min
    max_value, min_value = find_max_min(input_arr)

    # Display the results
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")

except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
except Exception as e:
    print(f"An error occurred: {e}")
