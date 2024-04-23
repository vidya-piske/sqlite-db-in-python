import sqlite3

def addcolumn():
    db = sqlite3.connect('restaurant_items.db')
    cur = db.cursor()
    cur.execute(
       '''CREATE TABLE new_table(
        id INTEGER PRIMARY KEY,
        item_name TEXT,
        quantity INTEGER,
        price REAL
       )
    ''')
    cur.execute('INSERT INTO new_table (item_name, quantity, price) SELECT item_name, quantity, price FROM users')
    cur.execute('DROP TABLE users')
    cur.execute('ALTER TABLE new_table RENAME to users')
    cur.execute('CREATE UNIQUE INDEX idx_id ON users (id)')
    print("ID column added as primary key")

    db.commit()
    db.close()

addcolumn()

