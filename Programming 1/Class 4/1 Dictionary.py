import random

# Generate a random integer between 1 and 12
random_number = random.randint(1, 12)

# Define a dictionary to map numbers to months
month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Check if the random number is in the dictionary
if random_number in month_dict:
    month_name = month_dict[random_number]
    print(f"The randomly chosen month is {month_name}.")
else:
    print("Invalid number generated.")
