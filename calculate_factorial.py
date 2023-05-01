# Enter a number to calculate its factorial, a list of numbers to calculate their average, and the lengths of two sides of a right triangle to calculate the hypotenuse. 

import math

def calculate_factorial(n):
    factorial = math.factorial(n)
    return factorial

def calculate_average(numbers):
    average = sum(numbers) / len(numbers)
    return average

def calculate_hypotenuse(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

# Input from the user
number = int(input("Enter a number to calculate its factorial: "))
num_list = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in num_list]
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))

# Calculations
factorial_result = calculate_factorial(number)
average_result = calculate_average(numbers)
hypotenuse_result = calculate_hypotenuse(side_a, side_b)

# Output
print("Factorial of", number, "is", factorial_result)
print("Average of the given numbers is", average_result)
print("Hypotenuse length of the right triangle is", hypotenuse_result)
