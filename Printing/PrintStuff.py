# ------------------------------------------------------------------------------
#   1.  Python Tutorial for Beginners 2: Strings - Working with Textual Data
#       Ref: https://youtu.be/k9TUPpGqYTo
# ------------------------------------------------------------------------------
message = "Hello World"
print(message)

message = 'Hello Universe'
print(message)

# Single quote inside a double quote
message = "Sukumar's World"
print(message)

# Double quote inside a single quote
message = 'Sukumar"s World'
print(message)

# Single quote inside Single quote with escape character
message = 'Sukumar\'s World'
print(message)

# Double quote inside double quote with escape character
message = "Sukumar\"s World"
print(message)

# Tripple quote
message = """Hello all,
How are you all doing?"""
print(message)

# Tripple quote
message = '''Hello all,
I hope you all are doing good.'''
print(message)

# Length of string
message = "Hello World"
print(len(message))

# Access single character
message = "Hello World"
print(message[0])
print(message[10])
# print(message[11])  # Index Error

# Access range of characters
message = "Hello World"
print(message[0:5])  # All the char between the starting of 0 and upto 5 but including 5th index.
print(message[:5])  # If you want the slice from the starting of the string, it can be blank
print(message[6:11])  # All the char between the starting of 6 and upto 11 but including 11th index.
print(message[6:])  # End point is blank here, so it will evaluate till the end of the string

# ------------------------------------------------------------------------------
# String Methods -
#                       1. str.lower()
#                       2. str.upper()
#                       3. str.count()
#                       4. str.find()       # Find the index of the particular char
#                       5. str.replace()
# ------------------------------------------------------------------------------
# Upper Case, Lower Case
message = "Hello World"
print(message.lower())
print(message.upper())

print(message.count('l'))

print(message.find('World'))
print(message.find('l'))
print(message.find('Universe'))  # Returns -1, if it can't find the substr

print()
print(message)
message.replace("World", "Universe")  # This method will not work, since the original string has not changed here
# replace() will return the new string after replacement
print(message)

new_message = message.replace("World", "Universe")
print(new_message)

# String Concatenation; This method is not advised to use
# Python3 has better solution
greeting = 'Hello'
name = 'Sukumar'
message = greeting + ', ' + name + '. Welcome!'
print(message)

# Better method to string concatenation
# This method is heaavily used for complex string concatenation and print
greeting = 'Hello'
name = 'Sukumar'
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# Python 3.6 and above version has new method - f string
greeting = 'Hello'
name = 'Sukumar'
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# See all available methods for name
print(dir(name))
