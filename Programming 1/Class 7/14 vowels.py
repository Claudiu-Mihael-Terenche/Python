char = input('Enter a single character from the alphabet: ')

# Check if the input is a single character and a letter
if len(char) == 1 and char.isalpha():
    # Convert the input to lowercase to handle both uppercase and lowercase letters
    letter = char.lower()

    # Check if the letter is a vowel
    if letter in ('a', 'e', 'i', 'o', 'u'):
        print("Input letter is Vowel")
    else:
        print("Input letter is Consonant")
else:
    print("Error: Please enter a single letter from the alphabet.")
