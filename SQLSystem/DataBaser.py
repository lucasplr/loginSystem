import sqlite3

conn = sqlite3.connect('UserData.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    User TEXT NOT NULL UNIQUE,
    Password TEXT NOT NULL
);
""")

print('Conectado ao banco de dados')

