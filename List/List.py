# ------------------------------------------------------------------------------
#   3.  Python Tutorial for Beginners 4: Lists, Tuples, and Sets
#       Ref: https://youtu.be/W8KRzm-HUcc
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# 1. Create List and Print List
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

# ------------------------------------------------------------------------------
# 2. Length of the list
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
print(len(courses))

# ------------------------------------------------------------------------------
# 3. Access individual list element
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses[0])
print(courses[1])
print(courses[2])
print(courses[3])

# Backward Access
print(courses[-1])
print(courses[-2])
print(courses[-3])
print(courses[-4])

# ------------------------------------------------------------------------------
# List Slice
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
print()
print(courses[0:2])
print(courses[:2])
print(courses[2:])
print()

# ------------------------------------------------------------------------------
# List Methods -
#                   1.  list.append(new_list_item)
#                   2.  list.insert(location, value)
#              ***  3.  list.extend()               # Useful for concatenate two lists
#                   4.  list.remove(list_item)
#                   5.  list.pop()                  # By default removes the last value
#
#                   6.  list.reverse()
#                   7.  list.sort()                 # Alters the original list
#                   8.  list.sort(reverse=True)     # Alters the original list
#                   9.  sorted(list)                # Does not alter the original list
#                  10.  new_list = sorted(list)     # Get the new sorted list
#
#                  11.  min(list)
#                  12.  max(list)
#                  13.  sum(list)

#                  14.  list.index(list_item)
#
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#  list.append(new_list_item)
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.append('Art')
print(courses)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
#  list.insert(location, value)
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.insert(0, 'Art')
print(courses)
print('-' * 80)
print()

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

courses.insert(0, courses_2)  # Result: [['Art', 'Education'], 'History', 'Math', 'Physics', 'CompSci']
print(courses)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
#  list.extend()               # Useful for concatenate two lists
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
#  list.remove(list_item)
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
courses.remove('Math')
print(courses)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
#  list.pop()                  # By default removes the last value
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
courses.pop()
print(courses)

popped = courses.pop()
print(popped)
print(courses)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
#  list.reverse()
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
courses.reverse()
print(courses)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
#  list.sort()
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

print(courses)
print(nums)
print()

courses.sort()
nums.sort()

print(courses)
print(nums)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
#  Reverse Sorting - list.sort(reverse=True)
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

print(courses)
print(nums)
print()

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
#  sorted(list)    - This example will create problem
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

print(courses)
print(nums)
print()

sorted(courses)
sorted(nums)

print(courses)
print(nums)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
#  sorted(list)    - This example is the right way to use sorted()
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

print(courses)
print(nums)
print()

sorted_courses = sorted(courses)
sorted_nums = sorted(nums)

print(sorted_courses)
print(sorted_nums)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
#  min(), Max(), sum()
# ------------------------------------------------------------------------------
nums = [1, 5, 2, 4, 3]

print(nums)
print()

print(min(nums))
print(max(nums))
print(sum(nums))

print('-' * 80)
print()

# ------------------------------------------------------------------------------
#  list.index()
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)
print()

print(courses.index('CompSci'))

print('-' * 80)
print()

# ------------------------------------------------------------------------------
# Other useful functions for List -
#                       1.  "in" operator with list
#                       2.  Iterate over list with for loop
#                       3.  enumerate(list)                 # For index and Value
#                       4.  enumerate(list, start = 1)      # Indext start from 1
#                       5.  ''.join(list)                   # Convert list to string
#                       6.  str.split(delimeter)
# ------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
print('Math' in courses)
print('Art' in courses)
print()

for item in courses:
    print(item)

print()
for index, course in enumerate(courses):
    print(index, course)

print()
for index, course in enumerate(courses, start=1):
    print(index, course)

print()
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_str = ', '.join(courses)
print(courses_str)

courses_str = ' <--> '.join(courses)
print(courses_str)

new_list = courses_str.split(' <--> ')
print(new_list)
