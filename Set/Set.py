# ------------------------------------------------------------------------------
# Sets - order is not maintained in Set
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#               Create Empty Set
# ------------------------------------------------------------------------------
#  empty_set = {}       # This isn't right! It's a dict
empty_set = set()       # This is the standard way of creating empty set


# ------------------------------------------------------------------------------
#               Initialize and Print Set
# ------------------------------------------------------------------------------
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)

# Automatically removes the duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)

# Sets are optimized for "in" operator
print('Math' in cs_courses)
print('-' * 80)
print()


# ------------------------------------------------------------------------------
#               Add method for Set
# ------------------------------------------------------------------------------
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)

cs_courses.add('Algo')
cs_courses.add('Compiler')
print(cs_courses)

print('-' * 80)
print()


# ------------------------------------------------------------------------------
#       set_1.intersection(set_2),
#       set_1.difference(set_2),
#       set_1.union(set_2)
#       set_1 & set_2     <--- Equivalent to intersection method
# ------------------------------------------------------------------------------
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses & art_courses)
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

print('-' * 80)
print()


# ------------------------------------------------------------------------------
#       set_1.issubset(set_2),
#       set_1.superset(set_2)
# ------------------------------------------------------------------------------
even = set(range(0, 40, 2))
squares_tupple = (4, 6, 16)
squares = set(squares_tupple)

print(even)
print(squares)

if squares.issubset(even):
    print("squares is a subset of even.")
if even.issuperset(squares):
    print("even is a superset of squares")

print('-' * 80)
print()


