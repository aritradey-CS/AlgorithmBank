# calculate its square root, the base and exponent for a power calculation, and the total and portion values for a percentage calculation. 

import math

def calculate_square_root(n):
    square_root = math.sqrt(n)
    return square_root

def calculate_power(base, exponent):
    result = base ** exponent
    return result

def calculate_percentage(total, portion):
    percentage = (portion / total) * 100
    return percentage

# Input from the user
number = float(input("Enter a number to calculate its square root: "))
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))
total = float(input("Enter the total value: "))
portion = float(input("Enter the portion value: "))

# Calculations
square_root_result = calculate_square_root(number)
power_result = calculate_power(base, exponent)
percentage_result = calculate_percentage(total, portion)

# Output
print("Square root of", number, "is", square_root_result)
print(base, "raised to the power of", exponent, "is", power_result)
print(portion, "is", percentage_result, "% of", total)
