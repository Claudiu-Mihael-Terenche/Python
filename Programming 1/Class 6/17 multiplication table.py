def print_multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

if __name__ == "__main__":
    try:
        num = int(input("Input a number: "))
        print_multiplication_table(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
