import sqlite3


def connect():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title VARCHAR , author VARCHAR , year INTEGER, isbn INTEGER);")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(f"INSERT INTO book VALUES (NULL,?,?,?,?);", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM book;")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM book WHERE title=? OR author=? OR year=? or isbn=?;", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(identity):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id =?;", (identity,))
    conn.commit()
    conn.close()


def update(identity, title, author, year, isbn):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, identity))
    conn.commit()
    conn.close()


connect()
# # insert(title="Sad boy", author="Kiera McElroy", year=2122, isbn=1283912310)
# print(view())
#
# delete(5)
update(4, "Sad Man", "Kiera McElroy", 2022, 321321)
# print(view())
# print(search(author="Siobhan Dockerty"))
