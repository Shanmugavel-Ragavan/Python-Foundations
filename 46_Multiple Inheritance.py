# Multiple Inheritance in Python

# 1. Multiple Inheritance is a feature of object-oriented programming where a class can inherit attributes and methods from multiple parent classes. In Python, a class can inherit from multiple parent classes by specifying multiple base classes in the class definition, separated by commas. The class that inherits from multiple parent classes is called a derived or child class, while the parent classes are known as base or parent classes.

#   Syntax :
#          class Parent1 :
#                   # attributes and methods of Parent1
#          class Parent2 :
#                   # attributes and methods of Parent2
#          class Child( Parent1, Parent2 ) :
#                   # attributes and methods of Child


# Parent Classes
class Father:
    def fishing(self):
        print("Fishing in Rivers")

    def chess(self):
        print("Playing Chess From Father")


class Mother:
    def cooking(self):
        print("Cooking Food")

    def chess(self):
        print("Playing Chess From Mother")


# Child Class inheriting from Father and Mother
class Son(Mother, Father):  # Multiple inheritance
    def ride(self):
        print("Riding Bicycle")


# Create Object and Access Methods
o = Son()
o.ride()  # Child's own method
o.fishing()  # Inherited from Father
o.cooking()  # Inherited from Mother
o.chess()  # Method Resolution Order (MRO) chooses Mother's chess()
