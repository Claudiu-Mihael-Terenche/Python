# Get temperature in Fahrenheit from the user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9

# Display the result
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius")
