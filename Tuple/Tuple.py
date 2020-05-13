# ------------------------------------------------------------------------------
#   3.  Python Tutorial for Beginners 4: Lists, Tuples, and Sets
#       Ref: https://youtu.be/W8KRzm-HUcc
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Mutable Example - List
# ------------------------------------------------------------------------------
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

# Changing list_1[0] will also change the value of list_2, since both lists point
# to same object in memory
list_1[0] = 'Art'

print(list_1)
print(list_2)

# ------------------------------------------------------------------------------
# Immutable Example - Tuple
# ------------------------------------------------------------------------------
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
#
# print(tuple_1)
# print(tuple_2)
#
# #  Since, Tuple is immutable, this line will give error:
# #  TypeError: 'tuple' object does not support item assignment
# tuple_1[0] = 'Art'
#
# print(tuple_1)
# print(tuple_2)


# ------------------------------------------------------------------------------
# How to create empty -
#                   1.  list
#                   2.  Tuple
#                   3.  Set
# ------------------------------------------------------------------------------
# # Empty Lists
# empty_list = []
# empty_list = list()
#
# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()
#
# # Empty Sets
# empty_set = {} # This isn't right! It's a dict
# empty_set = set()
