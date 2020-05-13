# ------------------------------------------------------------------------------
#   4.  Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs
#       Ref: https://youtu.be/daefaLgNkw0
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# 1.        Create Dictionary
#           Print Dictionary
# ------------------------------------------------------------------------------
student = {'name': 'John', 'age': 55, 'courses': ['Math', 'CompSci']}
print(student)

print('-' * 80)
print()

# ------------------------------------------------------------------------------
# 2. Access -
#             individual dictionary element (1st method)  <-- Not Recommend to use
# ------------------------------------------------------------------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['name'])
print(student['age'])
print(student['courses'])

print('-' * 80)
print()

# This following line will get keyError, since the key does not exists in the Dictionary
# KeyError: 'phone'
# print(student['phone'])

# ------------------------------------------------------------------------------
# 3. Access -
#             individual dictionary element (2nd method)  <--- Recommended to use
# ------------------------------------------------------------------------------
# Better way to access/get the dictionary items
# Program does not break if the dictionary key is not found,
# instead dict.get() returns None and have a way to define the
# return value if the key is not found
print(student.get('name'))
print(student.get('age'))
print(student.get('courses'))

print(student.get('Phone', 'Not Found'))

print('-' * 80)
print()

# ------------------------------------------------------------------------------
# 4. Update Dictionary -
#                           Method - 1
# ------------------------------------------------------------------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['name'] = 'Jane'
student['phone'] = '555-55555'

print()
print(student)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
# 5. Update Dictionary -
#                           Method - 2
# ------------------------------------------------------------------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

print(student)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
# 6. Delete Dictionary Element -
#                                   Method - 1
# ------------------------------------------------------------------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

del student['age']

print(student)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
# 7. Delete Dictionary Element -
#                                   Method - 2
# ------------------------------------------------------------------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

age = student.pop('age')

print(student)
print(age)
print('-' * 80)
print()

# ------------------------------------------------------------------------------
# 8. len(Dictionary)
# ------------------------------------------------------------------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

print(len(student))
print('-' * 80)
print()

# ------------------------------------------------------------------------------
# 9.    dict.keys()
#       dict.values()
#       dict.items()
# ------------------------------------------------------------------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

print(student.keys())
print(student.values())
print(student.items())

print('-' * 80)
print()

# ------------------------------------------------------------------------------
# 10.    Iterate Dictionary
# ------------------------------------------------------------------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

print()
for key in student.keys():
    print(key)

print()
for val in student.values():
    print(val)

print()
for key, value in student.items():
    print(key, value)

print('-' * 80)
print()

# ------------------------------------------------------------------------------
# 11.    Sort Dictionary    <--- Not recommended to use, better way available
# ------------------------------------------------------------------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

print()

# ordered_keys = list(student.keys())
# ordered_keys.sort()

ordered_keys = sorted(list(student.keys()))
for key in ordered_keys:
    print(key + " - " + str(student[key]))

print('-' * 80)
print()

# ------------------------------------------------------------------------------
# 12.    Sort Dictionary    <--- Recommended to use
# ------------------------------------------------------------------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

print()

for key in sorted(student.keys()):
    print(key + " - " + student[key])

print('-' * 80)
print()
