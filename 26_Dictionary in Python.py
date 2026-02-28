# Dictionary in Python
# A Python dictionary is a collection of key-value pairs where each key is associated with a value. dictionary are used to store multiple items in a single variable. To separate two items, you use a comma ( , ) . A dictionary is like a list except that it uses parentheses { key : value } .

# They are Immutable
# A set doesn’t allow duplicate elements
# The key cannot be changed
# This program demonstrates the usage of dictionaries in Python. A dictionary is a collection of key-value pairs, where each key is unique. Initially, a dictionary 'user' is created with key-value pairs of user's name, age, and marital status.

# The print statements show the dictionary, its type and the values corresponding to the keys "name" and "age".
# The keys() method returns the keys of the dictionary, and the values() method returns the values of the dictionary.
# The items() method returns a view of the dictionary's key-value pairs.
# For loops are used to iterate over the keys, values and items of the dictionary and print them.
# The in keyword is used to check if the "gender" key is present in the dictionary.
# The dictionary values can be updated using the update() method and the [] operator.
# The pop() method is used to remove the key-value pair with the given key, and the clear() method is used to remove all key-value pairs from the dictionary.
# Another dictionary 'users' is created that contains two dictionaries - 'user1' and 'user2' - as its values.

# The for loop is used to iterate over the keys of the dictionary, 'users', and print the values of the key "name" of each dictionary 'user1' and 'user2'.



# Creating and Accessing Dictionaries
user = {
    "name" : "Shanmugavel",
    "age" : 20,
    "isMarried" : False
}

print(user)
print(type(user))

print(user["name"])      # Access using []
print(user.get("age"))   # Access using get()

# Dictionary Methods
print(user.keys())    # All keys
print(user.values())  # All values
print(user.items())   # Key-value pairs

# Looping Through Dictionary
# Loop through keys
for x in user:
    print(x, user[x])
    
# Loop through values
for x in user.values():
    print(x)

# Loop through keys
for x in user.keys():
    print(x)

# Loop through key-value pairs
for x, y in user.items():
    print(x, y)
    
# Checking if Key Exists
if "gender" in user:
    print("Present")
else:
    print("Not Present")    
    
# Modifying Dictionary
user.update({"gender" : "male"})
print(user)

# Change Value
user["age"] = 25
print(user)

# Remove Elements
user.pop("age")   # Remove specific key
print(user)

user.clear()      # Remove all elements
print(user)

# Nested Dictionary Example
users = {
    "user1": {
        "name": "Ram",
        "age": 25
    },
    "user2": {
        "name": "Sam",
        "age": 30
    }
}

for key in users:
    print(users[key]["name"])