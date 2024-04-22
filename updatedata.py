import sqlite3

# Connect to the SQLite database
db = sqlite3.connect('restaurant_items.db')

with db:
    item_name = "chicken biryani"
    id = 2

    cur = db.cursor()

    # Update the item_name column
    cur.execute("UPDATE users SET item_name = ? WHERE id = ?", (item_name, id))

    # Commit the transaction
    db.commit()

    print("Data updated")
