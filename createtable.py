import sqlite3

def main():
    try:
        db=sqlite3.connect('restaurant_items.db')

        cur = db.cursor()

        tablequery = "CREATE TABLE users (id INT,item_name TEXT,quantity INT, price INT)"

        cur.execute(tablequery)

        print("Table created")
    
    except sqlite3.Error as e:
        print("Unable to create table")

if __name__ == "__main__":
    main()