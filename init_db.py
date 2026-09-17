import sqlite3

connection = sqlite3.connect("events.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    date TEXT NOT NULL,
    location TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

event_count = connection.execute(
    "SELECT COUNT(*) FROM events"
).fetchone()[0]

if event_count == 0:
    connection.execute("""
    INSERT INTO events
    (title, description, date, location, status)
    VALUES (?, ?, ?, ?, ?)
    """, (
        "IEEE Technology Seminar",
        "A seminar discussing current developments in technology and engineering.",
        "2026-10-15",
        "Institut Teknologi Bandung",
        "Upcoming"
    ))

    connection.execute("""
    INSERT INTO events
    (title, description, date, location, status)
    VALUES (?, ?, ?, ?, ?)
    """, (
        "IEEE Coding Workshop",
        "A beginner-friendly workshop focused on programming fundamentals.",
        "2026-11-02",
        "ITB Jatinangor",
        "Upcoming"
    ))

connection.commit()
connection.close()

print("Database successfully initialized!")