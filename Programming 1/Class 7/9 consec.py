def are_consecutive(num1, num2, num3):
    # Sort the numbers
    nums = [num1, num2, num3]
    nums.sort()

    # Check if the numbers are consecutive
    if nums[0] + 1 == nums[1] and nums[1] + 1 == nums[2]:
        return True
    else:
        return False

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = are_consecutive(num1, num2, num3)

print(f"The numbers {num1}, {num2}, {num3} are consecutive: {result}")
