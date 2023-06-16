# Python program that showcases mathematical intelligence by solving a quadratic equation:

import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots exist."

# Example usage
a = 2
b = -5
c = -3
roots = solve_quadratic_equation(a, b, c)
print("Roots:", roots)
