# ------------------------------------------------------------------------------
#   			Database Example - Print Database Records
# ------------------------------------------------------------------------------
import sqlite3


# ------------------------------------------------------------------------------
#   			Method-1  -  Print Database Records
# ------------------------------------------------------------------------------
# Connect to Database
db = sqlite3.connect("contacts.sqlite")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

for row in cursor:
    print(row)

print()
print('-'*80)

# ------------------------------------------------------------------------------
#   			Method-2  -  Print Database Records
# ------------------------------------------------------------------------------
# Another way to print
cursor.execute("SELECT * FROM contacts")
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)


cursor.close()
# Close the database connection
db.close()