def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    nums_set = set(nums)
    longest_sequence = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_sequence = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_sequence += 1

            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence

# Take user input for an array of integers
user_input = input("Enter an unsorted array of integers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Find the length of the longest consecutive sequence
result = longest_consecutive_sequence(nums)

# Display the result
print(f"The length of the longest consecutive sequence is: {result}")
