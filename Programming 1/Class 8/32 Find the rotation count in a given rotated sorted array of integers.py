def find_rotation_count(arr):
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        prev = (mid - 1 + n) % n
        next_ = (mid + 1) % n

        if arr[mid] < arr[prev] and arr[mid] < arr[next_]:
            return mid

        if arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[mid] >= arr[low]:
            low = mid + 1

    return 0  # If the array is not rotated

# Take user input for the rotated sorted array
try:
    arr = list(map(int, input("Enter the rotated sorted array elements separated by space: ").split()))
    rotation_count = find_rotation_count(arr)

    print(f"The array is rotated {rotation_count} times.")
except ValueError:
    print("Invalid input. Please enter integers separated by space.")
