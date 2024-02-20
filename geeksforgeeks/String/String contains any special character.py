import string


# Using string.punctuation

def check_string(str1):
    for item in str1:
        if item in string.punctuation:
            print('String is not accepted')
            return
    print('String is accepted')


# Example usage
check_string('Geeks$For$Geeks')  # Output: String is not accepted
check_string('Geeks For Geeks')  # Output: String is accepted
