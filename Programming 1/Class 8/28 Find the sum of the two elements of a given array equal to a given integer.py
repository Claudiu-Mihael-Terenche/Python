def find_pairs_with_sum(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

# Input array from the user
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Target sum from the user
target_sum = int(input("Enter the target sum: "))

# Finding pairs with the target sum
result_pairs = find_pairs_with_sum(arr, target_sum)

# Displaying the result
if result_pairs:
    print(f"Pairs with the sum {target_sum}: {result_pairs}")
else:
    print("No pairs found with the given sum.")
