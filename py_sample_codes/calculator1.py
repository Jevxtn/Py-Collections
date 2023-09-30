# Create a calculator that can add, subtract, multiply or divide depending upon the input from the user.
# Bonus: Add the ability to calculate square, cube, square root and cube root.

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def square_root(x):
    return math.sqrt(x)

def cube_root(x):
    return x ** (1/3)

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Cube")
print("7. Square Root")
print("8. Cube Root")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
    elif choice in ('5', '6', '7', '8'):
        num = float(input("Enter a number: "))

        if choice == '5':
            print(num, "squared is", square(num))

        elif choice == '6':
            print(num, "cubed is", cube(num))

        elif choice == '7':
            print("Square root of", num, "is", square_root(num))

        elif choice == '8':
            print("Cube root of", num, "is", cube_root(num))
    else:
        print("Invalid input")