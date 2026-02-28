# Property Method in Python

# 1. This program defines a Python class "student" with the following attributes and methods:

# . __init__ method: This method is called when an object of the class is created. It initializes the _total attribute with the passed value.
# . average method: This method calculates the average of the _total attribute and returns the result.
# . getter method: This method returns the value of the _total attribute.
# . setter method: This method sets the value of the _total attribute to the passed value. However, it checks if the passed value is less than 0 or greater than 500. If so, it prints "Invalid Total and can't Change."
# . total property: This property is created using the property method and links the getter and setter methods with the _total attribute.
# 2. The program then creates an object o of the "student" class and passes 450 as the argument for total. It then prints the total attribute and the result of the average method.

# 3. Finally, it sets the value of total to 350, which is considered valid, hence it is set to the new value. The updated values of the total attribute and the result of the average method are then printed.


# Define Class with Getter/Setter via property()
class Student:
    def __init__(self, total):
        self._total = total  # Internal attribute

    # Method to calculate average
    def average(self):
        return self._total / 5.0

    # Getter method
    def getter(self):
        return self._total

    # Setter method with validation
    def setter(self, t):
        if t < 0 or t > 500:
            print("Invalid Total and can't change")
        else:
            self._total = t

    # Link property with getter and setter
    total = property(getter, setter)


# 2️⃣ Create Object
o = Student(450)

print("Total   :", o.total)  # Uses getter
print("Average :", o.average())

# Try Invalid Total
o.total = 550  # Invalid → prints warning
print("Total   :", o.total)
print("Average :", o.average())

# Set Valid Total
o.total = 350  # Valid → updates internal value
print("Total   :", o.total)
print("Average :", o.average())
