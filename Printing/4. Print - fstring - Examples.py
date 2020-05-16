# ------------------------------------------------------------------------------
#   			String Formatting - fstring
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#  String Formatting - fstring -
#                                   Example - 1
# ------------------------------------------------------------------------------
# Python 3.6 and above version has new method - f string
greeting = 'Hello'
name = 'Paul'
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# See all available methods for name
print(dir(name))
print()
print('-'*80)


# ------------------------------------------------------------------------------
#  String Formatting - fstring -
#                                   Example - 2
# ------------------------------------------------------------------------------
age = 28
age_in_words = "2 years"
print(name + f" is {age} years old")
print(type(age))

print()
print('-'*80)



# ------------------------------------------------------------------------------
#  String Formatting - fstring -
#                                   Example - 3
# ------------------------------------------------------------------------------
print(f"Pi is approximately {22 / 7:12.50f}")

pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")

print()
print('-'*80)