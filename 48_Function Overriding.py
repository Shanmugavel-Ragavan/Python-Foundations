# Function Overriding in Python

# 1. Function overriding in Python is the ability of a subclass to provide a different implementation of a method that is already defined in its superclass. In other words, it is the process of redefining a method in a derived class that already exists in the base class. This is useful when a subclass wants to change the behavior of a method inherited from its superclass. The method in the subclass is said to override the method in the superclass and the subclass method is called instead of the superclass method when the method is called on an instance of the subclass.

# 2. The code defines two classes, Employee and Trainee, which have inheritance relationship with the Trainee class inheriting from the Employee class.

# 3. The Employee class has two methods, WorkingHrs and printHrs. The WorkingHrs method sets the number of working hours for an employee to 50. The printHrs method prints the number of working hours.

# 4. The Trainee class overrides the WorkingHrs method of the Employee class and sets the number of working hours for a trainee to 60. The resetHrs method resets the working hours to the original value of 50 by using the super keyword to call the WorkingHrs method of the Employee class.

# 5. Finally, objects of the Employee and Trainee classes are created and the WorkingHrs and printHrs methods are called to demonstrate the inheritance and method overriding concepts. The resetHrs method is also called on the trainee object to reset the working hours to 50.


# Base Class
class Employee:
    def working_hrs(self):
        self.hrs = 50  # Default working hours for employee

    def print_hrs(self):
        print("Total Working Hours:", self.hrs)


# Derived Class (Overrides working_hrs)
class Trainee(Employee):
    def working_hrs(self):
        self.hrs = 60  # Override: Trainee works 60 hours

    def reset_hrs(self):
        super().working_hrs()  # Call parent class method to reset to 50


# Using the Classes
# Employee object
employee = Employee()
employee.working_hrs()
employee.print_hrs()  # Output: 50

# Trainee object
trainee = Trainee()
trainee.working_hrs()
trainee.print_hrs()  # Output: 60

# Reset Trainee hours using super()
trainee.reset_hrs()
trainee.print_hrs()  # Output: 50
