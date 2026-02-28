# Set in Python
# Set are used to store multiple items in a single variable. To separate two items, you use a comma ( , ) . A set is like a list except that it uses parentheses { } . Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# Set are unordered
# A set doesn't allow duplicate elements
# Set cannot be changed
# The program creates two sets: "names" and "a".

# The "names" set is initially created with three elements 'Ram', 'Sam', and 'Ravi'. The set is printed and its type is also printed to show that it is a set.
# The for loop iterates through each element in the set and prints it. Then, a new element 'Sara' is added to the set using the "add" method.
# Another set "a" is created and its elements are added to the names set using the "update" method.
# The "remove" and "discard" methods are used to remove elements from the set. The "pop" method is used to remove an arbitrary element from the set.
# The "clear" method is used to remove all elements from the set and "del" is used to delete the entire set.
# A new set "names" is created with duplicate elements, but sets only store unique elements, so the duplicate elements are removed.
# Then, the program demonstrates set operations such as union, intersection, symmetric difference and set comparison methods such as isdisjoint, issubset, and issuperset.

# The "union" method is used to combine the elements of two sets and the "update" method updates the set with the elements from another set.
# The "intersection" method returns the common elements in both sets and the "intersection_update" method updates the set with the common elements.
# The "symmetric_difference" method returns the elements that are unique to each set and the "symmetric_difference_update" method updates the set with the unique elements.
# The "isdisjoint" method returns True if two sets have no common elements and False otherwise. The "issubset" method returns True if a set is a subset of another set and False otherwise.
# The "issuperset" method returns True if a set is a superset of another set and False otherwise.

# Creating and Accessing Sets
names = {"Ram", "Sam", "Ravi"}
print(names)        # {'Ravi', 'Sam', 'Ram'} → unordered
print(type(names))  # <class 'set'>

# Accessing elements using a for loop
for name in names:
    print(name)

# Adding an element
names.add("Sara")
print(names)

# 2. Updating, Removing, and Clearing Sets
a = {"Kumar", "Sundar", "Suresh"}
names.update(a)      # Add multiple elements
print(names)

names.remove("Sara")  # Removes "Sara", raises error if not found
names.discard("Suresh") # Removes "Suresh", no error if not found
names.pop()           # Removes an arbitrary element
names.clear()         # Removes all elements
print(names)          # set()

# 3. Sets Automatically Remove Duplicates
names = {"Ram", "Ram", "Sam", "Ravi", "Kumar", "Sundar", "Suresh"}
print(names)  
# Output: {'Ravi', 'Sam', 'Ram', 'Kumar', 'Sundar', 'Suresh'}

# Set Operations: Union and Update
a = {1, 2, 3, 4}
b = {"a", "b", "c", "d"}

c = a.union(b)  # returns a new set with all elements
print(c)        # {1, 2, 3, 4, 'a', 'b', 'c', 'd'}

a.update(b)     # adds elements of b to a in place
print(a)        # {1, 2, 3, 4, 'a', 'b', 'c', 'd'}

# Set Operations: Intersection and Symmetric Difference
a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}

# Intersection
c = a.intersection(b)       # {5}
print(c)
a.intersection_update(b)    # updates a to keep only common elements
print(a)                    # {5}

# Symmetric Difference
c = a.symmetric_difference(b)   # elements in either set, not both
print(c)                        # {6, 7, 8, 9}
a.symmetric_difference_update(b) # updates a to symmetric difference
print(a)                        # {6, 7, 8, 9}

# Set Comparison Methods
a = {5, 6, 7}
b = {5, 6, 7}

print(a.isdisjoint(b))  # False → sets share common elements
print(a.issubset(b))    # True  → all elements of a are in b
print(a.issuperset(b))  # True  → all elements of b are in a