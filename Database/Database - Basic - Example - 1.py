# ------------------------------------------------------------------------------
#   			Database Example - Create Tables and Insert Data
# ------------------------------------------------------------------------------
import sqlite3

# Connect to Database
db = sqlite3.connect("contacts.sqlite")

# Create the database table
db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)")

# Insert data to the database table
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Hellos', 568471, 'sp@gmail.com')")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Paul', 1254780, 'skp@gmail.com')")



# ------------------------------------------------------------------------------
#   			Database Example - Query Database
# ------------------------------------------------------------------------------
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

for row in cursor:
    print(row)

print()
print('-'*80)


cursor.execute("SELECT * FROM contacts")
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)

cursor.close()
# Commit the changes
db.commit()
# Close the database connection
db.close()