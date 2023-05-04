# radius of the circle

import math

def calculate_area_of_circle(radius):
    area = math.pi * radius**2
    return area

def calculate_hypotenuse(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

def calculate_factorial(n):
    factorial = math.factorial(n)
    return factorial

# Input from the user
circle_radius = float(input("Enter the radius of the circle: "))
triangle_side_a = float(input("Enter the length of side A of the triangle: "))
triangle_side_b = float(input("Enter the length of side B of the triangle: "))
number = int(input("Enter a number to calculate its factorial: "))

# Calculations
circle_area = calculate_area_of_circle(circle_radius)
triangle_hypotenuse = calculate_hypotenuse(triangle_side_a, triangle_side_b)
factorial_result = calculate_factorial(number)

# Output
print("Area of the circle:", circle_area)
print("Hypotenuse of the triangle:", triangle_hypotenuse)
print("Factorial of", number, "is", factorial_result)
