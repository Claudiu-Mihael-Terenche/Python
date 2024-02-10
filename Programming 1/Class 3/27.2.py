def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))

    if is_valid_number(length) and is_valid_number(breadth):

        area = length * breadth
        perimeter = 2 * (length + breadth)

        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")

        if area > perimeter:
            print("The area is greater than the perimeter.")
        else:
            print("The area is not greater than the perimeter.")
    else:
        print("Invalid input. Please enter valid numbers for length and breadth.")

if __name__ == "__main__":
    main()

