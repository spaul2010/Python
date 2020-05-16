# ------------------------------------------------------------------------------
#   			Usage of String Replacement Field
# ------------------------------------------------------------------------------
age = 25
print("My name is {0} years.".format(age))
print()
print('-'*80)


# ------------------------------------------------------------------------------
#   String Replacement Field - Another example
# ------------------------------------------------------------------------------
greeting = 'Hello'
name = 'Sukumar'
year = 2020
message = '{}, {}. Welcome! \nCurrent year is {}'.format(greeting, name, year)
print(message)
print()
print('-'*80)


# ------------------------------------------------------------------------------
#   String Replacement Field -

#   Manual field specification -
#                   "There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
# ------------------------------------------------------------------------------
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print()
print('-'*80)


# ------------------------------------------------------------------------------
#   String Replacement Field -
#
#   Automatic field specification -
#                           "There are {} days in {}, {}, {}, {}, {}, {} and {}"
# Note: manual and Automatic field specification can not be mixed.
# ------------------------------------------------------------------------------
print("There are {} days in {}, {}, {}, {}, {}, {} and {}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print()
print('-'*80)


# ------------------------------------------------------------------------------
#   String Replacement Field - Another example
# ------------------------------------------------------------------------------
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
print()
print('-'*80)


# ------------------------------------------------------------------------------
#   Multi-line String Replacement Field using Tripple quotes
# ------------------------------------------------------------------------------
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))

print()
print('-'*80)
