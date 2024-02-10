def second_smallest(arr):
    if len(arr) < 2:
        return "Array should have at least two elements."

    smallest = float('inf')
    second_smallest = float('inf')

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest

# Take input from the user
try:
    n = int(input("Enter the number of elements in the array: "))
    if n < 2:
        print("Array should have at least two elements.")
    else:
        array = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]
        result = second_smallest(array)
        print(f"The second smallest element is: {result}")
except ValueError:
    print("Please enter a valid integer.")
