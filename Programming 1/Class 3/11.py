def is_valid_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


def main():
    try:
        a = float(input("Enter the length of side A: "))
        b = float(input("Enter the length of side B: "))
        c = float(input("Enter the length of side C: "))

        if is_valid_triangle(a, b, c):
            print("The triangle with sides {}, {}, and {} is valid.".format(a, b, c))
        else:
            print("The triangle with sides {}, {}, and {} is not valid.".format(a, b, c))
    except ValueError:
        print("Invalid input. Please enter valid side lengths.")


if __name__ == "__main__":
    main()
