# Open a File in Python

# 1. File handling is an important part of any web application. Python has several functions for creating, reading, updating, and deleting files.

# Types Of File in Python

# . Binary file ( written in binary language, 0s, and 1s )
#      All binary files follow a specific format. We can open some binary files in the normal text editor but we can’t read the content present inside the file.
# . Text file
#      A text file exists stored as data within a computer file system. Text files don’t have any specific encoding and it can be opened in normal text editor itself.

# How to File Open
#      The key function for working with files in Python is the open() function. This function takes two parameters; filename, and mode.
#       Syntax :
#            file_object = open ( file_name , mode )
# . file_name is a string that represents the name of the file you want to open
# . modeis a string that represents how you want to open the file.

# Some Common Modes
# . 'r': read-only mode (default)
# . 'w': write mode (overwrites existing file or creates a new one)
# . 'a': append mode (appends to an existing file or creates a new one)
# . 'x': exclusive creation mode (creates a new file, fails if the file already exists)

# 2. Once the file is opened, you can perform various operations on it, such as reading or writing to it. It is important to close the file once you are done with it, using the close() method.

# 3. The code is how to open a file in Python using the open() function. The open() function takes two parameters: the first is the name of the file, and the second is the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, and 'a' for appending.

# In this example, the file "ram.txt" is opened in write mode using 'w'

# . The try block contains the code to open the file and perform operations on it.
# . The except block is used to handle any errors that may occur, such as the file not being found.
# . The else block will be executed if no errors occur, and it contains the code to close the file.
# . When the script is run, the file "ram.txt" is created if it doesn't exist and "This is New Line" is written in it.

# Read Entire File
try:
    with open("vel.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File Not Found")


# Read Lines
try:
    with open("vel.txt", "r") as file:
        print(file.readlines())
except FileNotFoundError:
    print("Error: File Not Found")


# Loop Through File
try:
    with open("vel.txt", "r") as file:
        for line in file:
            print(line.strip())  # strip() removes newline characters
except FileNotFoundError:
    print("Error: File Not Found")


# Write Mode (Overwrites File)
try:
    with open("vel.txt", "w") as file:
        file.write("Summa Iruda...\n")

    with open("vel.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: File Not Found")


# Append Mode
try:
    with open("vel.txt", "a") as file:
        file.write("Hi Shanmugavel\n")

    with open("vel.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: File Not Found")
