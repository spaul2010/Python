# ------------------------------------------------------------------------------
#    File Operations - Write Text File
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#       f.write()                                           ---> Write to a file
# ------------------------------------------------------------------------------
cities = ["Hyderabad", "Mumbai", "Kolkata", "Delhi", "Bengaluru"]

with open("test_city.txt", "w") as f:
    for city in cities:
        f.write(city)
        f.write('\n')

# Read back the file contents
with open("test_city.txt", "r") as rf:
    for line in rf:
        print(line, end='')
