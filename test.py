import sqlite3

conn = sqlite3.connect("mydatabase.db")
print("Connected successfully!")

conn.close()