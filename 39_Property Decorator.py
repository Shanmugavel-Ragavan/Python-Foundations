# Property Decorator in Python

# 1. Python @property is one of the built-in decorators. The main purpose of any decorator is to change your class methods or attributes. A decorator feature in Python wraps in a function, appends several functionalities to existing code and then returns it. Methods and functions are known to be callable as they can be called. Therefore, a decorator is also a callable that returns callable. @property decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property().

# 2. This is a Python program that defines a class named "user". The class has a constructor method __init__ that takes two parameters, "name" and "age", and sets them as instance variables "self.name" and "self.age" respectively.

# 3. The class also has a property method "msg" decorated with @property. This method returns a string that combines the name and age of the instance as "name is age years old".

# 4. An instance of the class named "o" is created with the name "Tutor Joes" and age 25. The values of the instance variables "name", "age", and "msg" are printed using dot notation. Then, the value of the "age" instance variable is changed to 45 and the "msg" property is printed again, showing the updated value.


# Define Class with @property
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def msg(self):
        return f"{self.name} is {self.age} years old"


# Create Object
o = User("Shanmugavel", 20)

print("Name:", o.name)
print("Age:", o.age)
print("Message:", o.msg)  # Accessed like an attribute (no parentheses)

# Modify Instance Attribute
o.age = 21
print("Updated Message:", o.msg)


# (Getter + Setter)
class Users:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Use underscore for internal variable

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @property
    def msg(self):
        return f"{self.name} is {self.age} years old"


u = Users("Vel", 25)
print(u.msg)

u.age = 30
print(u.msg)

# u.age = -5   # This will raise ValueError
