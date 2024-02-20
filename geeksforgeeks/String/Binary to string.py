def binary_to_decimal1(binary):
    str1 = int(binary, 2)
    return str1


bin_data = '10001111100101110010111010111110011'

str_data1 = ' '

for i1 in range(0, len(bin_data), 7):
    temp_data = bin_data[i1:i1 + 7]

    decimal_data = binary_to_decimal1(temp_data)

    str_data1 = str_data1 + chr(decimal_data)

print('The binary value after string conversion is:', str_data1)


def binary_to_decimal2(binary):
    # binary1 = binary
    decimal, i02, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i02)
        binary = binary // 10
        i02 += 1
    return decimal


str_data2 = ' '

for i2 in range(0, len(bin_data), 7):
    temp_data = int(bin_data[i2:i2 + 7])

    decimal_data = binary_to_decimal2(temp_data)

    str_data2 = str_data2 + chr(decimal_data)

print('The binary value after string conversion is:', str_data2)

'''
# Using int() function
# Python3 code to demonstrate working of
# Converting binary to string
# Using BinarytoDecimal(binary)+chr()


# Defining BinarytoDecimal() function

def BinaryToDecimal1(binary):
    str1 = int(binary, 2) # Using int function to convert to string
    return str1


bin_data = '10001111100101110010111010111110011'

# print binary data
# print("The binary value is:", bin_data)

# initializing a empty string for
# storing the string data

str_data1 = ' '
# slicing the input and converting it in decimal and then converting it in string
for i in range(0, len(bin_data), 7):
    temp_data = bin_data[i:i + 7] # slicing the bin_data from index range [0, 6] and storing it in temp_data

    # passing temp_data in BinarytoDecimal() function to get decimal value of corresponding temp_data
    decimal_data = BinaryToDecimal1(temp_data)

    # Decoding the decimal value returned by BinarytoDecimal() function, using chr() function which return the
    # string corresponding character for given ASCII value, and store it in str_data
    str_data1 = str_data1 + chr(decimal_data)

print('The binary value after string conversion is:', str_data1)


# Python3 code to demonstrate working of
# Converting binary to string
# Using BinarytoDecimal(binary)+chr()


# Defining BinarytoDecimal() function

def BinaryToDecimal2(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)


# bin_data = '10001111100101110010111010111110011'

# print binary data
# print("The binary value is:", bin_data)

# initializing a empty string for
# storing the string data

str_data2 = ' '
# slicing the input and converting it in decimal and then converting it in string
for i in range(0, len(bin_data), 7):
    # slicing the bin_data from index range [0, 6] and storing it as integer in temp_data
    temp_data = int(bin_data[i:i + 7])

    # passing temp_data in BinarytoDecimal() function to get decimal value of corresponding temp_data
    decimal_data = BinaryToDecimal2(temp_data)

    # Decoding the decimal value returned by BinarytoDecimal() function, using chr() function which return the
    # string corresponding character for given ASCII value, and store it in str_data
    str_data2 = str_data2 + chr(decimal_data)

print('The binary value after string conversion is:', str_data2)
'''
