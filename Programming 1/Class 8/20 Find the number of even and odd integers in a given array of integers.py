def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

def main():
    try:
        # Taking user input for the array of integers
        input_numbers = input("Enter a list of integers separated by space: ")
        numbers = list(map(int, input_numbers.split()))

        # Counting even and odd numbers
        even_count, odd_count = count_even_odd(numbers)

        # Displaying the results
        print(f"Even numbers: {even_count}")
        print(f"Odd numbers: {odd_count}")

    except ValueError:
        print("Invalid input. Please enter integers separated by space.")

if __name__ == "__main__":
    main()
