# ------------------------------------------------------------------------------
#   	Exception Handling - Try Except Else
#       ELSE Clause:
#                   Else part in the try block executes only when
#                   there was no exception raised.
# ------------------------------------------------------------------------------
import sys


def getInput(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(1)
        finally:
            print("The finally clause always executes.!")



first_number = getInput("Please enter first number ")
second_number = getInput("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("Division performed successfully")
