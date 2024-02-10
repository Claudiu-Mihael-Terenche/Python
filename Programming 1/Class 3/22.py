def check_insurance_eligibility(marital_status, gender, age):
    if marital_status == "married":
        return True
    elif marital_status == "unmarried":
        if gender == "male" and age > 30:
            return True
        elif gender == "female" and age > 25:
            return True
    return False


def main():
    marital_status = input("Enter marital status (married/unmarried): ")
    gender = input("Enter gender (male/female): ")
    age = int(input("Enter age: "))

    if check_insurance_eligibility(marital_status, gender, age):
        print("The driver is eligible for insurance.")
    else:
        print("The driver is not eligible for insurance.")


if __name__ == "__main__":
    main()

