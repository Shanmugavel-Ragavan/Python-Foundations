# Input Function in Python Programming

# 1. The input() function takes the user's input in the next single line, so whatever user writes in a signle line would be assign to to a variable. The input ( ) function helps to enter data at run time by the user and returns it as a string. This function prompts the user for an input from the keyboard.

# 2. Once the user has give the input and pressed enter One of the most important things to note here is that we're storing whatever the user entered into a variable. The output function print ( ) is used to display the result of the program on the screen after execution.

# 3. Use the int ( ) Function to Check if the Input Is an Integer in Python. The int ( ) function can convert a given string integer value to an integer type. Use the float ( ) Function to Check if the Input Is an decimal number in Python. The float ( ) function can convert a given string decimal number value to an float type.

# The program takes input from the user in three different forms:

# 1. A string input, taken using the input() function, stored in the "name" variable, and its type and value are printed.
# 2. Two integer inputs, taken using the input() function and converted to integers using int(), stored in the variables "a" and "b", their sum is calculated and stored in "c", and the sum and type of "a" are printed.
# 3. Two float inputs, taken using the input() function and converted to float using float(), stored in the variables "a" and "b", their sum is calculated and stored in "c", and the sum and type of "a" are printed.

# Getting input in Python

# String Input
name = input("Enter Name: ")
print("Type:", type(name))
print("Value:", name)

# String Concatenation (without conversion)
a = input("Enter Value of A: ")
b = input("Enter Value of B: ")
c = a + b  # Concatenates strings
print("Concatenated:", c)
print("Type of A:", type(a))

# Integer Input and Addition
a = int(input("Enter Value of A: "))
b = int(input("Enter Value of B: "))
c = a + b
print("Sum:", c)
print("Type of A:", type(a))

# Float Input and Addition
a = float(input("Enter Value of A: "))
b = float(input("Enter Value of B: "))
c = a + b
print("Sum:", c)
print("Type of A:", type(a))


# Multiple Values in Single Line

# 1. The program takes input from the user in the form of three names separated by either space or comma, stored in the variables name1, name2, name3. In the first input, the input() function is used to take the input, and the split() function is used to separate the names by space and store them in the respective variables. The values of the variables are then printed.

# 2. In the second input, the input() function is used to take the input, and the split() function is used to separate the names by a comma and store them in the respective variables. The values of the variables are then printed.

# Space-separated input
name1, name2, name3 = input("Enter 3 names (space-separated): ").split()
print("Name 1:", name1)
print("Name 2:", name2)
print("Name 3:", name3)

# Comma-separated input
name1, name2, name3 = input("Enter 3 names (comma-separated): ").split(',')
print("Name 1:", name1.strip())
print("Name 2:", name2.strip())
print("Name 3:", name3.strip())


# Multiple Line String Input in Python

# 1. The program defines a string variable a containing a multi-line text string. The data type of the variable a is str. The program then uses the print function to display the data type of a, which is str, and the value of a which is the text string itself.

# 2. The program is a Python script that takes multi-line input from the user in the form of a paragraph.

# 1. A list "para" is initialized.
# 2. The user is prompted to "Enter a Para : "
# 3. The "while" loop is used to get multi-line input.
# . The line input is taken using the "input()" function and stored in the variable "line".
# . The "if" condition checks if the line is not empty, if it is not, the line is added to the list "para" using the "append()" method.
# . If the line is empty, the loop breaks.
# 4. The list "para" is printed.
# 5. The "join()" method is used to join the list "para" with a line break and store it in the variable "output".
# 6. The final output is printed.

# Static multi-line string
text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.
"""
print("Type:", type(text))
print(text)

# Simple list
para = [25, 22, 33]
print(para)

# List type and accessing elements
print("Type:", type(para))
print("Third element:", para[2])

# Joining list of strings
para_str = ["25", "22", "33"]
print("Joined with '|':", '|'.join(para_str))

# Multi-line input from user
para = []
print("Enter a paragraph (Press Enter on empty line to finish):")

while True:
    line = input()
    if not line:  # Stop input when the user presses Enter on empty line
        break
    para.append(line)

# Combine all lines into a single string
output = "\n".join(para)

print("\nFinal Paragraph:")
print(output)