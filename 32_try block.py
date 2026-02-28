# Try Block in Python

# In Python, the try block is used to enclose code that might raise an exception. If an exception is raised within the try block, the code in the corresponding except block is executed. This allows you to handle errors and exceptions in a controlled way, rather than letting the program crash.

# The try block in Python is used to enclose code that might raise an exception. If an exception is raised within the try block, it is caught by the associated except block, which can then handle the exception as desired. The basic structure of a try-except block in Python is as follows:

# Syntax:
#    try:
#               # code that might raise an exception
#    except ExceptionType1:
#               # code to handle ExceptionType1
#    except ExceptionType2:
#               # code to handle ExceptionType2
#    except:
#               # code to handle any other exception
#    else:
#               # code to run if no exception was raised
#    finally:
#               # code that will always be executed, regardless of whether an exception was raised or not


# The else block is optional, and is only executed if no exceptions were raised within the try block. The finally block is also optional, but is always executed after the try block, regardless of whether an exception was raised or not.


# Basic Try-Except
try:
    a = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)

# Try-Except-Else
try:
    a = 10 / 25
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("A Value:", a)

# Try-Except-Else-Finally
try:
    a = 10 / 25
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("A Value:", a)
finally:
    print("Thank You")

# Common Built-in Exceptions
# NameError
try:
    print("--")
except NameError:
    print("Variable is not defined")

# ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Denominator can't be zero")

# ValueError
try:
    number = int("Vel")
except ValueError:
    print("Please enter numbers only")

# IndexError
try:
    numbers = [10, 20, 30, 40]
    print(numbers[10])
except IndexError:
    print("Invalid index")

# FileNotFoundError
try:
    with open("text.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

# Multiple Exceptions
try:
    a = 10 / 20
    print("Division Result:", a)

    b = [10, 20, 30, 40]
    print(b[10])

except ZeroDivisionError:
    print("Denominator can't be zero")

except IndexError:
    print("Invalid index")

# Catching Multiple Exceptions Together (Modern Way)
try:
    value = int("Hello")
except (ValueError, TypeError) as e:
    print("Error occurred:", e)

# Getting All Built-in Exceptions (Optional Info)
import builtins

exceptions = [name for name in dir(builtins) if name.endswith("Error")]
print("\nTotal Built-in Error Types:", len(exceptions))
print(exceptions[:10], "...")  # Print first 10
