import sqlite3


def create_table():
    connection = sqlite3.connect("lite.db")
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (ID INT, item VARCHAR, quantity INT, price REAL)")
    connection.commit()
    connection.close()


def insert(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cur = connection.cursor()
    cur.execute(f"INSERT INTO store VALUES ('%s', %s, %s;)" % (item, quantity, price))
    connection.commit()
    connection.close()


def select(query):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store WHERE ID = ?;", (query,))
    rows = cur.fetchall()
    conn.close()
    return rows


def update(quantity, price, identity):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE ID=?;", (quantity, price, identity))
    conn.commit()
    conn.close()


def delete(identity):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM STORE WHERE ID = %s;" % identity)
    conn.commit()
    conn.close()


create_table()
insert(item="test", quantity=12, price=15)
update(quantity=5, price=2.5, identity=5526)
print(select(query=input("ID: ")))
delete(identity=input("ID: "))
