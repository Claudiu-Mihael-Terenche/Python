def count_triangles(nums):
    nums.sort()
    count = 0

    for i in range(len(nums) - 2):
        k = i + 2
        for j in range(i + 1, len(nums) - 1):
            while k < len(nums) and nums[i] + nums[j] > nums[k]:
                k += 1
            count += k - j - 1

    return count

def main():
    try:
        # Take user input for an unsorted array of positive integers
        input_str = input("Enter a list of positive integers separated by spaces: ")
        nums = list(map(int, input_str.split()))

        # Check if the input list has at least three elements
        if len(nums) < 3:
            print("Please enter at least three positive integers.")
            return

        # Count the number of possible triangles
        result = count_triangles(nums)

        # Display the result
        print("Number of possible triangles:", result)

    except ValueError:
        print("Please enter valid positive integers separated by spaces.")

if __name__ == "__main__":
    main()
