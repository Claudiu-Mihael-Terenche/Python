from itertools import combinations

def find_four_element_combinations(arr, target_sum):
    result = []
    arr.sort()

    # Generate all combinations of four elements
    all_combinations = combinations(arr, 4)

    # Check each combination for the target sum
    for combo in all_combinations:
        if sum(combo) == target_sum:
            result.append(combo)

    return result

# Take user input for array and target sum
try:
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    target_sum = int(input("Enter the target sum: "))
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit()

# Find combinations and print the result
combinations_result = find_four_element_combinations(arr, target_sum)

if combinations_result:
    print(f"Combinations of four elements with sum {target_sum}:")
    for combo in combinations_result:
        print(combo)
else:
    print("No combinations found.")
