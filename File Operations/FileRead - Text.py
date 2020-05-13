# ------------------------------------------------------------------------------
#    File Operations - Read Text File
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
#   File Operations
#                         1. File read      [open() function]
# ------------------------------------------------------------------------------
# file_handler = open(r'C:\Users\Sukumar Paul\Desktop\UDEMY_Python_MasterClass\CoreyVideo\original.txt', 'r')
#
# for line in file_handler:
#     print(line)
#
# file_handler.close()


# ------------------------------------------------------------------------------
#   File Operations -
#                         2. Conditional File read      [open() function]
# ------------------------------------------------------------------------------
# file_handler = open(r'C:\Users\Sukumar Paul\Desktop\UDEMY_Python_MasterClass\CoreyVideo\original.txt', 'r')
#
# for line in file_handler:
#     if "thought" in line.lower():
#         print(line, end ='')
#
# file_handler.close()


# ------------------------------------------------------------------------------
#   File Operations -
#                         3. With Open <> as File_handler
# ------------------------------------------------------------------------------
# with open("original.txt", "r") as file_handler:
#     for line in file_handler:
#         if "thought" in line.lower():
#             print(line, end ='')



# ------------------------------------------------------------------------------
#   File Operations -
#                         4. file.readline()        # Read one line at a time
# ------------------------------------------------------------------------------
# with open("original.txt", "r") as file_handler:
#     line = file_handler.readline()
#     while line:
#         print(line, end='')
#         line = file_handler.readline()



# ------------------------------------------------------------------------------
#   File Operations -
#                         5. file.readlines()   # Read the entire file at one go
# ------------------------------------------------------------------------------
with open("original.txt", "r") as file_handler:
    # Read the entire file at one go and put each line in the return list
    # BE CAREFUL - If the FILE is VERY LARGE
    # DON'T USE THIS METHOD FOR LARGE FILE
    lines = file_handler.readlines()
print(lines)

for line in lines:
    print(line, end='')

