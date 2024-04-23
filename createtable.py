import sqlite3

def main():
    try:
        db = sqlite3.connect('restaurant_items.db')
        cur = db.cursor()

        tablequery = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, item_name TEXT, quantity INTEGER, price INTEGER)"
        cur.execute(tablequery)

        print("Table created")

        # Commit the transaction to save the changes
        db.commit()

    except sqlite3.Error as e:
        print("SQLite error:", e)
        print("Unable to create table")
    
    finally:
        # Close the database connection
        db.close()

if __name__ == "__main__":
    main()
