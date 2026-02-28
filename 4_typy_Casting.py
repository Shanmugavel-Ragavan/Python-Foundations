# Type Casting in Python

# 1. In Python, type casting is the process of converting one data type to another. Python is a dynamically-typed language, which means that the data type of a variable can change based on the value assigned to it. However, sometimes you may need to convert a variable from one data type to another.

# 2.There are several built-in functions in Python that can be used for type casting:

# . int(): Converts a value to an integer.
# . float(): Converts a value to a floating-point number.
# . str(): Converts a value to a string.
# . bool(): Converts a value to a Boolean (True or False).

# 3. This is a simple program in Python that performs the following operations:
# . Accepts two integer inputs from the user, a and b.
# . Adds a and b and stores the result in a variable c.
# . Converts the result stored in c to a string using the str() function.
# . Prints the message "Total : " followed by the result stored in c.
# 4. In this program, the user inputs are obtained using the input() function and then cast to integers using int(). The result of the addition of a and b is then stored in c, and to display it, the c is first converted to a string using str() before it's concatenated with the string "Total : " using the + operator. Finally, the result is displayed on the screen using the print() function.

# Basic Type Check
a = 10.0
print("Value:", a)
print("Type:", type(a))  # <class 'float'>

# Convert Float to Integer
a = 10.7
print("Original:", a, "Type:", type(a))

b = int(a)  # Converts float to integer (truncates decimal part)
print("After int():", b, "Type:", type(b))

# String Input and Concatenation
# Input as strings
a = input("Enter the value of A: ")
b = input("Enter the value of B: ")

# Without converting, '+' concatenates strings
c = a + b
print("Total (concatenated): " + c)
print("Type of a:", type(a))  # Always string

# Integer Input and Addition
# Convert input to integers
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

c = a + b
print("Total (numeric addition):", c)
print("Type of a:", type(a))

# Integer Input and String Conversion for Concatenation
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))

c = a + b
# Convert integer sum to string to concatenate with text
print("Total (as string): " + str(c))