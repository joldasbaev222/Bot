import sqlite3

conn = sqlite3.connect("jd.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
)
""")

# 5 ta odam qoʻshamiz (agar bo'lmasa)
cursor.execute("INSERT INTO users (name, phone) VALUES (?, ?)", ("Alisher", "+998901112233"))
cursor.execute("INSERT INTO users (name, phone) VALUES ('Azizbek', '+998907778899')")
cursor.execute("INSERT INTO users (name, phone) VALUES ('Azamat', '+998935554433')")
cursor.execute("INSERT INTO users (name, phone) VALUES ('Gulnaz', '+998933336677')")
cursor.execute("INSERT INTO users (name, phone) VALUES ('Malika', '+998909991122')")

conn.commit()


print("Bazaģa 5 adam qosildi!")