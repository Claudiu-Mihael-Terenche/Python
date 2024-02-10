def compute_average_except_extremes(arr):
    if len(arr) < 3:
        print("Array should have at least three elements.")
        return None

    min_val = min(arr)
    max_val = max(arr)

    arr.remove(min_val)
    arr.remove(max_val)

    average = sum(arr) / len(arr)
    return average

def main():
    try:
        # Taking user input for the array of integers
        input_str = input("Enter space-separated integers: ")
        user_input = list(map(int, input_str.split()))

        # Computing the average except the largest and smallest values
        result = compute_average_except_extremes(user_input)

        if result is not None:
            print("Average value (excluding the largest and smallest):", result)

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
