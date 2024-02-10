def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]  # [2:] is used to remove the '0b' prefix from the binary representation

if __name__ == "__main__":
    try:
        decimal_input = int(input("Input a Decimal Number: "))
        binary_output = decimal_to_binary(decimal_input)
        print("Binary number is:", binary_output)
    except ValueError:
        print("Invalid input! Please enter a valid decimal number.")
