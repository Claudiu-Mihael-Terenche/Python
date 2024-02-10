def calculate_sum_and_average():
    try:
        n = int(input("Enter the number of elements: "))
        if n <= 0:
            print("Please enter a positive integer for the number of elements.")
            return

        numbers = []
        for i in range(n):
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)

        # Calculate sum and average
        total_sum = sum(numbers)
        average = total_sum / n

        print(f"Sum: {total_sum}")
        print(f"Average: {average}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculate_sum_and_average()
