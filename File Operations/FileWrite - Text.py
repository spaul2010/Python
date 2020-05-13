# ------------------------------------------------------------------------------
#    File Operations - Write Text File
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
#   File Operations
#                         1. File Write
# ------------------------------------------------------------------------------
# cities = ["Hyderabad", "Mumbai", "Kolkata", "Delhi", "Bengaluru"]
#
# with open("cities.txt", "w") as city_file:
#     for city in cities:
#         print(city, file=city_file)
#         # Use flush [arameter if you want to write the content in the file immediately
#         # print(city, file=city_file, flush=True)
#

# ------------------------------------------------------------------------------
#   File Operations
#                         1. File Write & then Read back the data
# ------------------------------------------------------------------------------
cities = []

with open("cities.txt","r") as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))     # removes \n for each item read from file

print(cities)
for city in cities:
    print(city)