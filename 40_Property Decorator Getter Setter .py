# Property Decorator Getter Setter in Python

# 1. In Python, property decorators are used to define getter, setter, and deleter methods for class properties. They allow for the encapsulation of data, by controlling access to the underlying data. Property decorators are applied to methods and define how a property value can be retrieved, set, or deleted.

# . Getter: A getter is a method that is used to retrieve the value of a property. The getter method is decorated with the @property decorator and has no arguments.
# . Setter: A setter is a method that is used to set the value of a property. The setter method is decorated with the @<property_name>.setter decorator and takes one argument, the new value for the property.

# 2. This program defines a Python class "student" with the following attributes and methods:

# . __init__ method: This method is called when an object of the class is created. It initializes the _total attribute with the passed value.
# . average method: This method calculates the average of the _total attribute and returns the result.
# . total property: This property acts as a getter for the _total attribute. It returns the value of _total.
# . total.setter: This acts as a setter for the _total attribute. It sets the value of _total to the passed value. However, it checks if the passed value is less than 0 or greater than 500. If so, it prints "Invalid Total and can't Change."

# 3. The program then creates an object o of the "student" class and passes 450 as the argument for total. It then prints the total attribute and the result of the average method.

# 4. Finally, it sets the value of total to 550, which is greater than 500, hence it is considered as invalid and "Invalid Total and can't Change." is printed.


# Define Class with Getter and Setter
class Student:
    def __init__(self, total):
        self._total = total  # Use underscore for internal attribute

    # Method to calculate average
    def average(self):
        return self._total / 5.0

    # Getter for total
    @property
    def total(self):
        return self._total

    # Setter for total with validation
    @total.setter
    def total(self, t):
        if t < 0 or t > 500:
            print("Invalid Total and can't change")
        else:
            self._total = t


# Create Object
o = Student(450)

print("Total   :", o.total)  # Access using getter
print("Average :", o.average())

# Try to Set Invalid Total
o.total = 550  # Invalid
print("Total   :", o.total)
print("Average :", o.average())

# Set Valid Total
o.total = 400  # Valid
print("Total   :", o.total)
print("Average :", o.average())
