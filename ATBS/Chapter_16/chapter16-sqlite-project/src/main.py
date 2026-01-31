import sqlite3

# Connect to the database file (creates if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create a students table (if not already there)
conn.execute(
    "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)"
)

# Insert sample data
conn.execute(
    "INSERT INTO students (name, grade) VALUES (?, ?)", ("Alex", 8.7)
)
conn.execute(
    "INSERT INTO students (name, grade) VALUES (?, ?)", ("Elena", 9.2)
)
conn.commit()

# Fetch and display all students
rows = conn.execute("SELECT * FROM students").fetchall()
for r in rows:
    print(r)

# Close the connection to the database
conn.close()