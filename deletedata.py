import sqlite3

db = sqlite3.connect('restaurant_items.db')

with db:
    id = 1  # Assuming id is an integer

    cur = db.cursor()

    # Pass id as a tuple
    cur.execute("DELETE FROM users WHERE ID = ?", (id,))
    db.commit()

    print("Data Deleted")
