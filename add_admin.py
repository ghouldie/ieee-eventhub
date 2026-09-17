import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect("events.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
""")

username = "admin"
password = "ieee123"

password_hash = generate_password_hash(password)

connection.execute("""
INSERT OR IGNORE INTO admins (username, password_hash)
VALUES (?, ?)
""", (username, password_hash))

connection.commit()
connection.close()

print("Admin berhasil dibuat!")
print("Username: admin")
print("Password: ieee123")