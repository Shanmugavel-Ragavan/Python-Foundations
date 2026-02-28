# Single Inheritance in Python

# Single Inheritance in Python refers to a situation where a derived class inherits from a single base class. The derived class inherits all the attributes and methods of the base class and can also have additional attributes and methods of its own. This is the simplest form of inheritance, where a child class inherits from one parent class. The child class can access all the public and protected methods and attributes of the parent class.

#   Syntax :
#          class base1 :
#               body of base class
#          class derived( base1) :
#               body of derived class

# This program defines two classes, Nokia and Nokia1100. The Nokia class contains two class-level attributes, company and website, and a method contact_details which prints the company's address. The Nokia1100 class is a subclass of the Nokia class, and it contains two instance-level attributes, name and year, and a method product_details which prints the product details.

# An object of the Nokia1100 class is created and referred to by the name mobile. The product_details and contact_details methods are called on the mobile object, printing the product details and company's address, respectively.


# Base Class
class Nokia:
    company = "Nokia India"
    website = "www.nokia-india.com"  # Fixed typo

    def contact_details(self):
        print("Address: Cherry Road, Near By Bus Stand, Chennai")


# Derived Class
class Nokia1100(Nokia):  # Inherits from Nokia
    def __init__(self):
        self.name = "Nokia 1100"
        self.year = 1998

    def product_details(self):
        print(f"Name    : {self.name}")
        print(f"Year    : {self.year}")
        print(f"Company : {self.company}")
        print(f"Website : {self.website}")


# Create Object and Access Methods
mobile = Nokia1100()
mobile.product_details()  # Derived class method
mobile.contact_details()  # Base class method (inherited)
