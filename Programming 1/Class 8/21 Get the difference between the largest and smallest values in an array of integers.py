def find_difference(arr):
    if len(arr) < 1:
        print("Array must have a length of at least 1.")
        return None

    min_val = min(arr)
    max_val = max(arr)
    difference = max_val - min_val

    return difference

# Take user input to create an array
try:
    # Python 2
    input_func = raw_input
except NameError:
    # Python 3
    input_func = input

input_array = input_func("Enter integers separated by spaces: ")
user_array = list(map(int, input_array.split()))

result = find_difference(user_array)

if result is not None:
    print(f"Difference between the largest and smallest values: {result}")
