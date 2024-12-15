import sqlite3

# Establish Connection and Cursor
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Create Table
cursor.execute("CREATE TABLE 'events' ('band' TEXT, 'city' TEXT,'date' TEXT)")

# Insert New Rows
new_rows = [
    ("Cats", "Meow City", "2025-01-15"),
    ("Dogs", "Bow-Wow City", "2025-01-15"),
    ("Parrots", "Squawk City", "2025-01-30")
]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# Query All Data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print("All Data:", rows)

# Query All Data Based on Condition
cursor.execute("SELECT * FROM events WHERE date='2025-01-15'")
rows = cursor.fetchall()
print("All Data from 2025-01-15:", rows)

# Query Specific Columns Based on Condition
cursor.execute("SELECT band, city FROM events WHERE date='2025-01-15'")
rows = cursor.fetchall()
print("Band and City Columns from 2025-01-15:", rows)
