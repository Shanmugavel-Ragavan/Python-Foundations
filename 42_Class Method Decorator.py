# Class Method Decorator in Python

# 1. This program defines a Python class "student" with the following attributes and methods:

# . count attribute: This is a class attribute that is shared by all objects of the class. It is initialized to 0.
# . __init__ method: This method is called when an object of the class is created. It initializes the name and age attributes with the passed values, and increments the count class attribute by 1 each time a new object is created.
# . printDetail method: This method prints the values of the name and age attributes.
# . total method: This method is a class method and returns the value of the count attribute, which keeps track of the total number of objects created.

# 2. The program then creates two objects o and a of the "student" class, passing the respective name and age as arguments. The printDetail method is then called on each object to print their details. Finally, the value of the count attribute is accessed using both the class name and an object reference, which returns the same result.


# Define Class with Class Attribute and Class Method
class Student:
    count = 0  # Class attribute shared by all instances

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1  # Increment count whenever a new object is created

    def print_detail(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def total(cls):
        """Return total number of Student instances"""
        return cls.count


# Create Objects and Access Methods
o1 = Student("Shanmugavel", 20)
o1.print_detail()
print("Total Admission:", o1.total())  # Access via object

o2 = Student("Vel", 19)
o2.print_detail()
print("Total Admission:", Student.total())  # Access via class
