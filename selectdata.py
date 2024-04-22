import sqlite3

db = sqlite3.connect('restaurant_items.db')

with db:
    cur = db.cursor()
    selectquery = "SELECT * from users"
    cur.execute(selectquery)

    row = cur.fetchall()

    for data in row:
        print(data)
        
