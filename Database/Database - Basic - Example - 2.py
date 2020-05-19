# ------------------------------------------------------------------------------
#   			Database Example - Print Database Records
# ------------------------------------------------------------------------------
import sqlite3

# Connect to Database
db = sqlite3.connect("contacts.sqlite")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

for row in cursor:
    print(row)

print()
print('-'*80)

# Another way to print
cursor.execute("SELECT * FROM contacts")
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)

cursor.close()
# Close the database connection
db.close()