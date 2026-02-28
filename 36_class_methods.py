# Class Method in Python

# This code defines a class called Student with class attributes name and age and a class method printall(). The printall() method is defined within the class and it prints the values of class attributes name and age.

# Student.printall() calls the class method and prints the values of class attributes name and age.
# print(Student.__dict__) prints the class attributes and methods in a dictionary form.
# getattr(Student, "printall") gets the attribute of the class Student by the name of the attribute which is printall and returns the function definition.
# getattr(Student, "printall")() gets the attribute of the class Student by the name of the attribute which is printall and calls the function.
# Student.__dict__['printall']() gets the attribute of the class Student by the name of the attribute which is printall from the class dictionary and calls the function.
# All three ways of calling the class method printall() will print the same output which is "Name : Tutor Joes", "Age : 25"

# Define Class with Class Method


class Student:
    name = "Shanmugavel"
    age = 20

    @classmethod
    def print_all(cls):
        print("Name:", cls.name)
        print("Age:", cls.age)


# Calling Class Method
Student.print_all()

# View Class Namespace
print("\nClass Dictionary:")
print(Student.__dict__)

# Using getattr()
print("\nUsing getattr():")
method = getattr(Student, "print_all")
print(method)  # Shows method reference
method()  # Calls the method

# Accessing from __dict__

print("\nUsing __dict__:")
Student.__dict__["print_all"].__get__(None, Student)()


# Instance vs Class vs Static Method Example
class Demo:
    class_var = "Class Variable"

    def instance_method(self):
        print("Instance Method")

    @classmethod
    def class_method(cls):
        print("Class Method:", cls.class_var)

    @staticmethod
    def static_method():
        print("Static Method")


d = Demo()

d.instance_method()
Demo.class_method()
Demo.static_method()
