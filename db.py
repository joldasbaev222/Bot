import sqlite3

conn = sqlite3.connect("JD.db")
db = conn.cursor()

db.execute(
    """
CREATE TABLE  paydalaniwshilar (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL UNIQUE,
email TEXT
);
"""
)

conn.commit()
print("Таблица 'users' успешно создана (или уже существовала).")
# db.close()