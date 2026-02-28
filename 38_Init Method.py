# Init Method in Python

# 1.The __init__ method, also known as the constructor method, is a special method in Python classes that gets called automatically when a new instance of the class is created. The __init__ method is used to initialize the attributes of the class and set them to the default values.

# 2. This is a Python program defining a class named "user". The class has a constructor method __init__ that takes a name parameter and sets it as an instance variable "self.name". The class also has a method printall that prints the instance variable "self.name".

# 3. Two instances of the class, o1 and o2, are created with the names "Tutor Joes" and "Joes" respectively. The printall method is called on each instance to print its name, and the __dict__ attribute is printed to show the instance variables and their values.

# 4. Finally, the __dict__ attribute of the class itself is printed to show the class variables and their values, if any.

# Define Class with __init__ Constructor
class User:
    def __init__(self, name):
        print("Called when new instance is created")
        self.name = name  # Instance attribute

    def print_all(self):
        print("Name:", self.name)


# Create First Object
o1 = User("Shanmugavel")
o1.print_all()
print("o1 __dict__:", o1.__dict__)

# Create Second Object
o2 = User("Vel")
o2.print_all()
print("o2 __dict__:", o2.__dict__)

# View Class Namespace
print("\nUser Class __dict__:")
print(User.__dict__)


# Without Print in Constructor
class Users:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Users(name={self.name})"


u = Users("Shanmugavel")
print(u)
