# ------------------------------------------------------------------------------
#    Python Function  - Examples
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
#    Simple Function
# ------------------------------------------------------------------------------
# def hello_func():
#     print("Hello Function!")
#
# hello_func()
# hello_func()
# hello_func()


# ------------------------------------------------------------------------------
#    Use return type of a function
# ------------------------------------------------------------------------------
# def hello_func():
#     return "Hello Function!"
#
# print(hello_func().upper())
# print(hello_func().lower())
# print(len(hello_func()))


# ------------------------------------------------------------------------------
#    Function - Parameter, Argument
# ------------------------------------------------------------------------------
# def hello_func(greeting):                         # <--- greeting is a parameter
#     return '{} Function.'.format(greeting)
#
# print(hello_func('Hello'))                         # <--- 'Hello' is an argument
# print(hello_func('Hi'))                            # <--- 'Hello' is an argument


# ------------------------------------------------------------------------------
#    Function - Parameter Default value
# ------------------------------------------------------------------------------
# def hello_func(greeting, name='You'):             # <--- greeting is a parameter
#     return '{}, {}.'.format(greeting, name)
#
# print(hello_func('Hello', 'Sukumar'))              # <--- 'Hello' is an argument
# print(hello_func('Hello'))                         # <--- 'Hello' is an argument
# print(hello_func('Hi'))                            # <--- 'Hello' is an argument


# ------------------------------------------------------------------------------
#    Function parameters -   *args, **kwargs
# ------------------------------------------------------------------------------
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# # Here, 'Math', 'Art' are  --->     positional argument
# # and, 'John' & 22 are     --->     keyword argument
# student_info('Math', 'Art', name='John', age=22)


# ------------------------------------------------------------------------------
#    Function parameters -   *args, **kwargs
# ------------------------------------------------------------------------------
def student_info(*args, **kwargs):
    """This is a sample docstring example
    Place all the relevant function information here in the docstring"""
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

# student_info(courses, info)  --> This is not the right way of passing
# args will unpack the value as: (['Math', 'Art'], {'name': 'John', 'age': 22})
# and kwarsg will unpack as:     {}

# student_info(courses, info)           #  <--- DO NOT USE THIS

student_info(*courses, **info)          #  <--- USE THIS INSTEAD


