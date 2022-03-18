import sqlite3

print("Creating DB")
conn = sqlite3.connect("fb.db")
print("DB created")
conn.execute(
    """CREATE TABLE if not exists facebook (id INTEGER PRIMARY KEY AUTOINCREMENT,
    username char(100) NOT NULL UNIQUE, email char(100) NOT NULL,
    password char(100) NOT NULL, cookie char(128) UNIQUE)"""
)
conn.execute("INSERT INTO facebook (username, email, password) VALUES ('Vivien', 'vivien@facebook.com', 'TEST123')")
conn.execute("INSERT INTO facebook (username, email, password) VALUES ('Elsa', 'elsa@facebook.com', 'TEST124')")
conn.execute("INSERT INTO facebook (username, email, password) VALUES ('Anna', 'anna@facebook.com', 'TEST125')")
conn.commit()
print("Table created")
