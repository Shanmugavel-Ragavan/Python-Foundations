# String and String Functions in Python
# 1. Python has several built-in functions associated with the string data type. These functions let us easily modify and manipulate strings. Creating Strings is the simplest and easy to use in Python. To create a string in Python, we simply enclose a text in single as well as double-quotes.


# . type() => The returns the type of the object.
# . upper() => All the characters in a given string are uppers case.
# . lower() => All the characters in a given string are lower case.
# . capitalize() => The first character is the upper case
# . The title() => The first character in every word of the string is an upper case.
# . count() => Finds the number of times a specified value in the given string.
# . find() => Finds the first occurrence of the specified value.
# . replace() => Replaces a specified phrase with another specified phrase.
# . isalnum() => Checks whether all the characters in a given string is alphanumeric or not
# . isalpha() => returns True if all the characters in the string are alphabets
# . islower() => Checks if all characters in the string are lowercase
# . isupper() => Checks if all characters in the string are uppercase
# . strip() => The used to trim whitespaces from the string object

# Creating Strings and Checking Type
s = "Shanmugavel"
print("String:", s)
print("Type:", type(s))  # <class 'str'>

# Common String Functions
s = "Shanmuga vel"
print("Original:", s)

print("Uppercase:", s.upper())        # Convert to uppercase
print("Lowercase:", s.lower())        # Convert to lowercase
print("Capitalized:", s.capitalize()) # Capitalize first character
print("Title Case:", s.title())       # Capitalize first character of each word

print("Count of 'a':", s.count("a"))  # Count occurrences of a substring
print("Ends with 'el':", s.endswith("el"))  # Check suffix
print("First occurrence of 'u':", s.find("u"))  # Find first index
print("Find 'a' starting from index 5:", s.find("a",5)) # Find after index 5

print("Replace 'a' with '5':", s.replace("a","5"))  # Replace substring

# String Checks
a = "ragavan123"

print("Is Upper:", a.isupper())      # All characters uppercase?
print("Is Lower:", a.islower())      # All characters lowercase?
print("Is Alphanumeric:", a.isalnum()) # Only letters and numbers?
print("Is Alphabetic:", a.isalpha()) # Only letters?

# Split Lines
m = "he\nis\ngood"
print("Original:\n", m)

print("Split lines:", m.splitlines())       # Split by line breaks
print("Split lines (keep line breaks):", m.splitlines(True)) 

# Split Strings
n = "Shanmugavel is a Good Boys"
print("Split by spaces:", n.split(" "))

n = "Shanmugavel,is,a,Good,Boys"
print("Split by comma:", n.split(","))

# Strip Whitespaces
v = "       VEL      "
print("Original length:", len(v))
print("After strip():", len(v.strip()))   # Remove spaces from both ends
print("After lstrip():", len(v.lstrip())) # Remove spaces from left
print("After rstrip():", len(v.rstrip())) # Remove spaces from right

# Partition Strings
r = "10-12-2024"
print("Partition by '-':", r.partition('-')) 
# Output: ('10', '-', '12-2024')