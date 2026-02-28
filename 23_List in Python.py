# List in Python
# Lists are used to store multiple items in a single variable.To separate two items, you use a comma ( , ) . List uses the square brackets [ ]. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Sequence Type
# Element of the list can access by index
# They are mutable
# This program demonstrates various built-in functions and methods that can be used with lists in Python.

# The first block of code shows how to create a list and access its elements using indexing. It also shows how to change the value of an element in a list using indexing.
# The second block of code shows how to create a list with different data types and how to access the elements of the list and their types.
# The third block of code demonstrates how to use the clear() method to remove all elements from a list, the copy() method to create a copy of a list, the count() method to count the number of occurrences of an element in a list, the index() method to find the index of an element in a list, the len() function to find the length of a list, the max() and min() functions to find the maximum and minimum element in a list, the pop() method to remove an element from a list using an index, and the remove() method to remove an element from a list using its value.
# The fourth block of code shows how to use the append() method to add elements to a list, the extend() method to add elements from another list, and the insert() method to insert an element at a specific index in a list.
# The fifth block of code demonstrates how to use the range() function to create a list of numbers, the list() function to convert a string to a list, and the sort() method to sort the elements of a list in ascending or descending order. It also shows how to use the key parameter to sort the elements based on a specific key and the reverse parameter to sort the elements in descending order.

# List in Python
"""
Sequence Type
Mutable
a[5]
a={1,2,3,4,5}
a[0]
"""

# Creating and Modifying a List
a = [1,2,3,4,5]
print(a)        # [1, 2, 3, 4, 5]
print(type(a))  # <class 'list'>

a[0] = 100      # Change first element
print(a)        # [100, 2, 3, 4, 5]

print("-----------------------------")

# Slicing a List
a = [100,2,3,4,5]
print(a[1])     # 2
print(a[-1])    # 5
print(a[0:3])   # [100, 2, 3]
print(a[2:])    # [3, 4, 5]
print(a[:3])    # [100, 2, 3]

print("-----------------------------")

# Lists with Multiple Data Types
a = [1, True, "Shanmugavel", 2.5, [1,2,3,4]]
print(a)
print(a[0], type(a[0]))   # 1, int
print(a[1], type(a[1]))   # True, bool
print(a[2], type(a[2]))   # 'Shanmugavel', str
print(a[4][1])             # 2

print("-----------------------------")

# Clearing a List
a = [10,25,35,45]
a.clear()
print(a)  # []

print("-----------------------------")

# Copying a List
a = [10,25,35,45]
b = a.copy()
print(b)  # [10, 25, 35, 45]

print("-----------------------------")

# Counting, Index, Length, Max & Min
a = [10,25,35,45,25,58,25]
print(a.count(25))  # 3
print(a.index(25))  # 1
print(len(a))       # 7
print(max(a))       # 58
print(min(a))       # 10

# Removing elements
a.pop(0)            # remove by index
a.remove(25)        # remove by value

print("-----------------------------")

# 7. Adding Elements
names = ["Shanmugavel"]
names.append("Ragavan")       # add single element
names.extend(["Moorthi","Karthi"])  # add multiple elements
names.insert(0, "Siva")       # insert at index 0
names.pop()                   # remove last element
print(names)

names.pop(0)                  # remove first element
print(names)

print("-----------------------------")

# Using range(), converting string to list, Sorting
print(list(range(5)))     # [0,1,2,3,4]
print(list("Shanmugavel"))  # ['S','h','a','n','m','u','g','a','v','e','l']

a = [50,10,100,25,87]
a.sort()                   # ascending
a.sort(reverse=True)       # descending

a = ["Orange","Apple","Banana"]
a.sort()                   # alphabetically
a.sort(reverse=True)       # reverse alphabetically
a.sort(key=len)            # by length of string