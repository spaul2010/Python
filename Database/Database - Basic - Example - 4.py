# ------------------------------------------------------------------------------
#   			Database Example - Print Specific Record
# ------------------------------------------------------------------------------
import sqlite3

# Connect to Database
db = sqlite3.connect("contacts.sqlite")

name = input("Please enter a name to search for: ")

# Watch out for comma after name -->  ... WHERE name = ?", (name,))
for row in db.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
    print(row)

db.close()