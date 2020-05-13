# ------------------------------------------------------------------------------
#   2.  Python Tutorial for Beginners 3: Integers and Floats - Working with Numeric Data
#       Ref: https://youtu.be/khKv-8q7YmY
# ------------------------------------------------------------------------------

num = 3
print(type(num))

num = 3.14
print(type(num))

# ------------------------------------------------------------------------------
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2
# ------------------------------------------------------------------------------
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)  # Python 2 will give 1, but python3 will result 1.5
print(3 // 2)  # Python3 Integer Division/Floor Division
print(3 ** 2)  # 3 to the power 2
print(3 % 2)  # Useful to find out if a number is even or odd

print()
print(3 * 2 + 1)
print(3 * (2 + 1))

print()
num = 1
print(num)

num = num + 1
print(num)

num += 1  # += operator for increment
print(num)

num *= 10
print(num)

# useful built-in functions -
#                               1. abs(-3)
#                               2. round(3.75)
#                               3. round(3.75, 1)
print(abs(-3))
print(round(3.75))  # Result 4
print(round(3.75, 1))  # Result 3.8

# ------------------------------------------------------------------------------
# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2
# ------------------------------------------------------------------------------
num_1 = 3
num_2 = 2

print()
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

# String addition - String, and Integer Casting

num_1 = '100'
num_2 = '200'

print(num_1 + num_2)  # Result: 100200

print(int(num_1) + int(num_2))  # Result = 300
