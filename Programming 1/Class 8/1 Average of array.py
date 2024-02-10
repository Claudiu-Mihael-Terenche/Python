def calculate_average(arr):
    if not arr:
        return None  # Avoid division by zero if the array is empty
    total = sum(arr)
    average = total / len(arr)
    return average

def main():
    try:
        n = int(input("Enter the number of elements in the array: "))
        if n <= 0:
            print("Please enter a valid positive integer for the number of elements.")
            return

        array = []
        for i in range(n):
            element = float(input(f"Enter element {i + 1}: "))
            array.append(element)

        avg = calculate_average(array)
        if avg is not None:
            print(f"The average of the array elements is: {avg:.2f}")
        else:
            print("The array is empty, so the average cannot be calculated.")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
