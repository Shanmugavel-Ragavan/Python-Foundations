# Instance Attributes in Python

# A class is a blueprint for the creation of different objects. When the objects get created to form the class, they no longer depend on the class attribute. Also, the class has no control over the attributes of the instances created.

# Syntax of Object:
#       object_name = class_name ( arguments )

# Example of Object:
#       s = student ( )

# The code is defining a class called user with one class attribute, course with value Java. The user.__dict__ is a dictionary that contains the class and its attributes and methods. It will print the class attribute course in the form of dictionary.

# user.course is used to access the class attribute value which is Java.
# o = user() creates an object o of the class user. o.__dict__ will print an empty dictionary because the object o does not have any instance attribute.
# o.course will print the class attribute value which is Java.
# o.course = "C++" will change the value of class attribute to C++ for object o .
# o.__dict__ will print the dictionary with class attribute course with value C++.
# o2 = user() creates another object o2 of the class user. o2.course will print the class attribute value which is Java because object o2 does not have any instance attribute to change the class attribute value.


# Define Class with Class Attribute
class User:
    course = "Python"  # Class attribute (shared by all instances)


# Access Class Attribute
o = User()

print("Class __dict__:", User.__dict__)  # Shows class namespace
print("Class Attribute (User.course):", User.course)

print(
    "Object __dict__ before change:", o.__dict__
)  # Empty (no instance attributes yet)
print("Access via object (o.course):", o.course)

# Create Instance Attribute
o.course = "C++"  # This creates an instance attribute (does NOT change class attribute)

print("\nObject __dict__ after change:", o.__dict__)  # {'course': 'C++'}
print("o.course:", o.course)  # Instance attribute
print("User.course:", User.course)  # Still Python (class attribute)

# Create Another Object
o2 = User()
print("\no2.course:", o2.course)  # Still Python (inherits class attribute)


# Best Practice (Using init)
class Users:
    def __init__(self, course):
        self.course = course  # Instance attribute


u1 = Users("Python")
u2 = Users("Java")

print(u1.course)  # Python
print(u2.course)  # Java