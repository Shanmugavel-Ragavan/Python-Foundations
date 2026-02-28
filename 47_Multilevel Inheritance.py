# Multilevel Inheritance in Python

# 1.Multilevel Inheritance is a mechanism in object-oriented programming where a class inherits from another class, which in turn inherits from another class. This process continues until the topmost class is reached. In this way, inheritance relationships form a hierarchy of classes, with the base class being at the top, and the derived classes being at the bottom. The derived class inherits the attributes and behavior of the class it inherits from and can also add new attributes and behavior to those inherited.

#   Syntax :
#          class base1 :
#                   body of base class
#          class derived1( base1 ) :
#                   body of derived class
#          class derived2( derived1 ) :
#                   body of derived class

# 2. This code demonstrates multilevel inheritance in Python, where a derived class (Son) inherits from a base class (Father), and the base class (Father) in turn inherits from another base class (GrandFather). The class Son is able to access the methods ownHouse and ownBike from GrandFather and Father classes respectively. The class Son also has its own method ownBook.


# Base Class
class GrandFather:
    def own_house(self):
        print("Grandfather's House")


# Intermediate Class
class Father(GrandFather):  # Inherits from GrandFather
    def own_bike(self):
        print("Father's Bike")


# Derived Class
class Son(Father):  # Inherits from Father
    def own_book(self):
        print("Son has a Book")


# Create Object and Access Methods
o = Son()
o.own_house()  # Inherited from GrandFather
o.own_bike()  # Inherited from Father
o.own_book()  # Own method
