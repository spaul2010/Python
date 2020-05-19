# ------------------------------------------------------------------------------
#   			Database Example - Create Tables and Insert Data
# ------------------------------------------------------------------------------
import sqlite3


# Step-1:	Connect to Database
db = sqlite3.connect("contacts.sqlite")

# Step-2:	Create the database table; Only if does not exists
db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)")

# Step-3:	Insert data to the database table
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Hellos', 568471, 'sp@gmail.com')")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Paul', 1254780, 'skp@gmail.com')")

# Step-4:	Commit the changes into the database
db.commit()

# Step-5:	Close the database connection
db.close()
