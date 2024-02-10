def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"


def main():
    try:
        a = float(input("Enter the length of side A: "))
        b = float(input("Enter the length of side B: "))
        c = float(input("Enter the length of side C: "))

        if a + b > c and b + c > a and a + c > b:
            triangle = triangle_type(a, b, c)
            print(f"The given sides form a {triangle}.")
        else:
            print("The given sides do not form a valid triangle.")
    except ValueError:
        print("Please enter valid numerical values for the side lengths.")


if __name__ == "__main__":
    main()
