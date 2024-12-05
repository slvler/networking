import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")


username1, password1 = "john1", hashlib.sha256("john1".encode()).hexdigest()
username2, password2 = "john12", hashlib.sha256("john12".encode()).hexdigest()
username3, password3 = "john123", hashlib.sha256("john123".encode()).hexdigest()
username4, password4 = "john1234", hashlib.sha256("john1234".encode()).hexdigest()

cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()