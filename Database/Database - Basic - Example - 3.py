# ------------------------------------------------------------------------------
#   			        Database Example - Update Record in Database
#   *** CAUTION  ***
#   RUN the following program in sequence to test this program:
#   1. Database - Basic - Example - 1.py
#   2. Database - Basic - Example - 2.py
#   3. Database - Basic - Example - 3.py
# ------------------------------------------------------------------------------
import sqlite3

# Connect to Database
db = sqlite3.connect("contacts.sqlite")

# Update Record in Database - execute update statement
update_sql = "UPDATE contacts SET email = 'updatedskp@gmail.com' WHERE phone = 1254780"
update_cursor = db.cursor()
update_cursor.execute(update_sql)

# Print relevant data
print("{} rows updated.".format(update_cursor.rowcount))

print()
print("Are connections the same? : {}".format(update_cursor.connection == db))

# Commit the updates to database
update_cursor.connection.commit()
update_cursor.close()


for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)


# Close the database connection
db.close()