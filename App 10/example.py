import sqlite3

# Establish a connection & cursor
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Query Data before insertion
cursor.execute("SELECT band, city, date FROM events WHERE band='Tiger'")
rows = cursor.fetchall()
print("Before insertion:", rows)

# Insert new rows
new_rows = [('Cats', 'Cat City', 'Sept 17, 2022'),
            ('Dogs', 'Pickletown', 'June 5, 2022')]
cursor.executemany("INSERT INTO events VALUES (?, ?, ?)", new_rows)
connection.commit()

# Query the data again to confirm insertion
cursor.execute("SELECT band, city, date FROM events")
rows = cursor.fetchall()
print("After insertion:", rows)

# Close the connection
connection.close()
