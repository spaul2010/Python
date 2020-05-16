# ------------------------------------------------------------------------------
#   			String Formatting
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#  String Formatting -
#                           1. Field Index
#                           2. Field Width
# ------------------------------------------------------------------------------
for i in range(1, 13):
    # {0:2}  --> 0 is the field index and 2 is the field width, separated by ':'
    # {1:4}  --> 1 is the field index and 4 is the field width, separated by ':'
    # {2:4}  --> 2 is the field index and 4 is the field width, separated by ':'
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()
print('-'*80)


# ------------------------------------------------------------------------------
#  String Formatting -
#                       1. Field Alignment
#                       2. Left Alignment using   '<'
#                       3. Right Alignment using  '>'   (Default alignment)
#                       4. Center Alignment using '^'
#   {1:<3}
#           - 1 is Field Index
#           :   is the separator
#           <   is for Left Alignment
#           3   is Field Width
# ------------------------------------------------------------------------------
for i in range(1, 13):
    print("No. {0:>2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()
print('-'*80)


# ------------------------------------------------------------------------------
#  String Formatting -
#                       1. Floating Point Numbers
# ------------------------------------------------------------------------------
print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))
print()
print('-'*80)


# ------------------------------------------------------------------------------
#  String Formatting -
#                       1. Automatic Field Specification with Field Width
# ------------------------------------------------------------------------------
for i in range(1, 13):
    print("No. {:>3} squared is {:>6} and cubed is {:>6}".format(i, i ** 2, i ** 3))