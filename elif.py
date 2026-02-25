import math

# Coefficients of the quadratic equation ax² + bx + c = 0
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Determine the nature of the roots
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two distinct real roots: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One repeated root: {root}")
else:
    print("No real roots (complex roots)")