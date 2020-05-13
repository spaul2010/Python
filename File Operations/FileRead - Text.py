# ------------------------------------------------------------------------------
#    File Operations - Read Text File
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Small Files:      f.read()                  ---> Read entire content and print
# ------------------------------------------------------------------------------
# with open("original.txt", "r") as f:
#     f_contents = f.read()
#     print(f_contents)



# ------------------------------------------------------------------------------
#           f.readline()                            ---> Read one line at a time
# ------------------------------------------------------------------------------
# with open("original.txt", "r") as f:
#     f_contents = f.readline()
#     print(f_contents, end='')
#
#     f_contents = f.readline()
#     print(f_contents, end='')



# ------------------------------------------------------------------------------
#  Big Files:      f.readlines()       ---> Read entire file and store in a list
# ------------------------------------------------------------------------------
# with open("original.txt", "r") as f:
#     f_contents = f.readlines()
#     print(f_contents)



# ------------------------------------------------------------------------------
#  ******     For Extremely Large File  *******
#                USE THIS METHOD
# This is efficient for extremely large file.
# ------------------------------------------------------------------------------
# with open("original.txt", "r") as f:
#     for line in f:
#         print(line, end='')
#


# ------------------------------------------------------------------------------
#  ******     For Extremely Large File  *******
#                USE THIS METHOD
#             Read a chunk of file at a time
# This is another way to read extremely large file.
# ------------------------------------------------------------------------------
# with open("original.txt", "r") as f:
#     size_to_read = 10
#
#     f_contents = f.read(size_to_read)
#
#     while(len(f_contents) > 0):
#         print(f_contents, end='')
#         f_contents = f.read(size_to_read)


# ------------------------------------------------------------------------------
#           f.tell()                          ---> Current File Pointer position
# ------------------------------------------------------------------------------
# with open("original.txt", "r") as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#
#     print(f.tell())


# ------------------------------------------------------------------------------
#           f.seek()                          ---> Change File Pointer Position
# ------------------------------------------------------------------------------
with open("original.txt", "r") as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end='*')

    # This helps the file pointer to go back to starting of the file
    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents, end='')
