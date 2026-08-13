# Import for the math library.
import math

# The user inputs the coordinates of x1
x1 = float(input("Enter the first x-coordinate: "))

# The user inputs the coordinates of y1
y1 = float(input("Enter the first y-coordinate: "))

# The user inputs the coordinates of x2
x2 = float(input("Enter the second x-coordinate: "))

# The user inputs the coordinates of y2
y2 = float(input("Enter the second y-coordinate: "))

# Calculate the distance between the two points using the distance formula.
distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

#The distance between the two points is now printed.
print("The distance between the two points is", distance)


"""
REFLECTION:
Using a library like math makes it easier to calculate and solve different mathematical problems. The math library has many built-in functions that can be used to perform calculations, such as square roots, trigonometric functions, and logarithms. In this case, we used the math.pow() function to calculate the square of the differences in coordinates, which is a key step in calculating the Euclidean distance between two points.
"""