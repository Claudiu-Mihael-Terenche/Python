# Input ages of Ram, Shyam, and Ajay
ram_age = int(input("Enter Ram's age: "))
shyam_age = int(input("Enter Shyam's age: "))
ajay_age = int(input("Enter Ajay's age: "))

# Initialize a variable to keep track of the minimum age
min_age = min(ram_age, shyam_age, ajay_age)

# Initialize empty lists to store names of people with the minimum age
youngest_names = []

# Check each person's age and add their name to the list if they have the minimum age
if ram_age == min_age:
    youngest_names.append("Ram")
if shyam_age == min_age:
    youngest_names.append("Shyam")
if ajay_age == min_age:
    youngest_names.append("Ajay")

# Check if there is more than one person with the minimum age
if len(youngest_names) > 1:
    print("The youngest people are:", ", ".join(youngest_names))
else:
    print("The youngest person is:", youngest_names[0])
