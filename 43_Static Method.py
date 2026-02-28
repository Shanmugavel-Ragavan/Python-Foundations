# Static Method in Python

# 1. A static method in Python is a method that belongs to a class rather than an instance of the class. It can be called on the class itself, rather than on an instance of the class. Static methods are defined using the @staticmethod decorator, and do not have access to any class-specific state. They are typically used for utility functions that don't need to access any instance-specific data.

# 2. This code demonstrates the use of a static method in Python. A static method is a method that belongs to a class rather than an instance of the class. In the example, the welcome() method is a static method that can be called on the class itself or on an instance of the class. The @staticmethod decorator is used to define a static method. The code creates two instances of the student class, s1 and s2, and demonstrates that the welcome() method can be called on both the class and the instances.


# Define Class with Static Method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_detail(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @staticmethod
    def welcome():
        """Static method: does not access instance or class attributes"""
        print("Welcome to our institution")


# Create Objects and Call Methods
s1 = Student("Shanmugavel", 20)
s1.print_detail()
s1.welcome()  # Can be called via instance
Student.welcome()  # Can also be called via class

s2 = Student("Ragavan", 19)
s2.print_detail()
s2.welcome()
