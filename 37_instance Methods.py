# Instance Method in Python
# This code defines a class called Student which has a class attribute name and age and a class method printall(). The printall() method takes one parameter self and gender.

# When creating an object of the class, o=Student(), you can call the printall() method using the object and providing the additional parameter gender as an argument. For example, o.printall("Male") or by using the class name and passing the object and the argument as Student.printall(o,"Male").

# When you try to call o.printall() or Student.printall(o) without providing the required parameter gender you get TypeError as "Missing 1 required positional argument: 'gender'"

# This is because, in method definition, we have defined two parameters self and gender and if we call the method without providing both the parameters, it will raise an error.

# Define Class with Instance Method
class Student:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    def print_all(self, gender):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", gender)


# Create Object
o = Student("Shanmugavel", 20)

# Correct Method Calls
o.print_all("Male")  # Recommended way
Student.print_all(o, "Male")  # Alternative way (manual self passing)
