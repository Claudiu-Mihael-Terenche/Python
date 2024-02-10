import re


def is_valid_password(password):
    # Check if the password has at least ten characters
    if len(password) < 10:
        return False

    # Check if the password consists of only letters and digits
    if not re.match("^[a-zA-Z0-9]+$", password):
        return False

    # Check if the password contains at least two digits
    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        return False

    # If all checks pass, the password is valid
    return True


# Example usage:
password = input('Input the password: ')
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")
