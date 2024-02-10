def is_divisible_by_5_and_11(number):
    if number % 5 == 0 and number % 11 == 0:
        return True
    else:
        return False

# Get input from the user
num = int(input("Enter a number: "))

if is_divisible_by_5_and_11(num):
    print(f"{num} is divisible by both 5 and 11.")
else:
    print(f"{num} is not divisible by both 5 and 11.")
