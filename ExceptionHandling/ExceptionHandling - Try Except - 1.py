# ------------------------------------------------------------------------------
#   			Exception Handling - Example - 1
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#   			Example - Handle ZeroDivisionError
# ------------------------------------------------------------------------------
a = 10

try:
    result = a / 0
except ZeroDivisionError:
    print("Exception Occurred : a can not be divided by zero!!!")

print()
# ------------------------------------------------------------------------------
#   			Example - Handle RecursionError
# ------------------------------------------------------------------------------
def factorial(n):
    """ Calculates n! recursively
    n! can be defined as n * (n-1)!
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# Main Code
try:
    print(factorial(100000))
except RecursionError:
    print("This program calculate  factorials that large")

print("Program Terminating")
