# File: FunctionExamples.py
# Date: 7/16/2024
# Description: This program contains multiple different functions, each with a different action
# Covering: Functions

import math
# Write a function to return the sum of three numbers.
def sum3Numbers (x, y, z):
    return x + y + z

# Write a function to return the product of three numbers.
def multiply3Numbers( x, y, z ):
    return x * y * z

# Write a function to return the sum of up to 3 numbers.  It should
# accept 1, 2, or 3 parameters.
def sumUpTo3Numbers (x, y = 0, z = 0):
    return x + y + z

# Write a function to return the product of up to 3 numbers.  It
# should accept 1, 2, or 3 parameters.
def multiplyUpTo3Numbers (x, y = 1, z = 1):
    return x * y * z

# Write a function that takes 2 numbers as input and prints them
# out in ascending order.  Make sure it works if they are equal.
def printInOrder( x, y ):
    if(x >= y):
        return y, x
    elif(y >= x):
        return x, y

# Write a function that returns the area of a square, given the length of a side.
# Print an error message if side is negative. 
def areaOfSquare( side ):
    if(side < 0):
        return "Negative value entered"
    else:
        return pow(side, 2)

# Write a function that returns the perimeter of a square, given
# the length of a side.  Print an error message if side is negative.
def perimeterOfSquare( side ):
    if(side < 0):
        return "Negative value entered"
    else:
        return side * 4

# Write a function that returns the area of a circle, given the
# radius.  Use math.pi. Print an error message if radius is negative.
def areaOfCircle( radius ):
    if(radius < 0):
        return "Negative value entered"
    else:
        return math.pi * (pow(radius, 2))

# Write a function that returns the circumference of a circle given
# the radius.  Use math.pi. Print an error if radius is negative.
def circumferenceOfCircle( radius ):
    if(radius < 0):
        return "Negative value entered"
    else:
        return math.pi * 2 * radius

# Write a function: given parameters d1, d2, x, returns whether
# both d1 and d2 are both factors of (evenly divide) x.
def bothFactors( d1, d2, x ):
    return (x % d1 == 0) and (x % d2 == 0)

# Given a value x, compute and print out the area and circumference of a circle with
# radius x and the area and perimeter of a square with side x.  Use your previous 
# functions for these computations.  Leave a blank line above and below the printing.
def squareAndCircle( x ):
    print("\nCircle with radius " + str(x) + " has:")
    print("\tArea: " + str(areaOfCircle(x)))
    print("\tCircumference: " + str(circumferenceOfCircle(x)))
    print("Square with side " + str(x) + " has:")
    print("\tArea: " + str(areaOfSquare(x)))
    print("\tPerimeter: " + str(perimeterOfSquare(x)) + "\n")

# Write a function that returns the factorial of a positive
# integer n.  Use a for loop to compute the factorial.  You can
# assume the input is an integer, but print an error message if
# it's not positive and return None.
# Note: for loop, range() does not inclusive
def factorial( n ):
    if n < 0:
        return "Input must be positive."
    fac = 1
    for x in range(1, n + 1):
        fac *= x
    return fac

# Write a function that returns the number of digits in the
# decimal representation of a number n.  You can assume that
# n is a positive integer.
# Note: len() returns the number of items
def numberLength( n ):
    return len(str(n))

# Write a function that sums positive numbers entered by the user
# and returns the sum.  You can assume that user inputs are
# numbers (float or int).  If the number entered is negative, print 
# an error message and continue;  don't add it to the sum.  There 
# can be any number of inputs.  Stop when the user enters 0. 
def sumPositiveNumbers():
    num = 1
    sum = 0
    while num != 0:
        num = float(input("Enter a number: "))
        if(num < 0):
            print("Illegal input.")
            continue
        sum += num
    return sum

# Testing all the functions
def main():
    print(sum3Numbers(5, 6, 7))
    print(multiply3Numbers(3.2, 6, -19.123))
    print(sumUpTo3Numbers(12.9))
    print(sumUpTo3Numbers(12.9, 3))
    print(sumUpTo3Numbers(12.9, 3, 14.7))
    print(multiplyUpTo3Numbers(12.9))
    print(multiplyUpTo3Numbers(12.9, 3))
    print(multiplyUpTo3Numbers(12.9, 3, -2.7))
    print(printInOrder(2.1, -10))
    print(printInOrder(2.1, 10))
    print(printInOrder(2, 2))
    print(areaOfSquare(-10))
    print(areaOfSquare(10))
    print(perimeterOfSquare(-10.2))
    print(perimeterOfSquare(10.2))
    print(areaOfCircle(-10))
    print(areaOfCircle(10))
    print(circumferenceOfCircle(-10))
    print(circumferenceOfCircle(10))
    print(bothFactors(-2, 3, 20))
    print(bothFactors(-2, 3, 30))
    squareAndCircle(10)
    print(factorial(-10))
    print(factorial(10))
    print(numberLength(21))
    print(numberLength(1234567))
    print(sumPositiveNumbers())

main()