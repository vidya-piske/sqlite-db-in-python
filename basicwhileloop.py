import sqlite3

def fetchItems():
    db = sqlite3.connect('restaurant_items.db')
    cur = db.cursor()
    cur.execute('SELECT * FROM users')  
    rows = cur.fetchall()  
    print("View All Items")
    for row in rows:
        print(row) 
    db.commit()
    db.close()

def AddItems():
    item_name = input("Enter item name:")
    quantity = int(input("Enter quantity:")) 
    price = float(input("Enter price:")) 

    db = sqlite3.connect('restaurant_items.db')
    with db:
        cur = db.cursor()
        cur.execute('INSERT INTO users VALUES (?,?,?)', (item_name, quantity, price))
        print("Data inserted")

def ModifyItems():
    fetchItems()  # Display all items before modification

    item_id_to_modify = input("Enter the item ID to modify: ")

    db = sqlite3.connect('restaurant_items.db')
    with db:
        cur = db.cursor()
        cur.execute('SELECT * FROM users WHERE id=?', (item_id_to_modify,))
        row = cur.fetchone()

        if not row:
            print("Item not found.")
            return 

        print("Existing Details:")
        print("Item ID:", row[0])
        print("Item Name:", row[1])
        print("Quantity:", row[2])
        print("Price:", row[3])

        new_item_name = input("Enter new item name (leave blank to keep unchanged): ").strip()
        new_quantity = input("Enter new quantity (leave blank to keep unchanged): ").strip()
        new_price = input("Enter new price (leave blank to keep unchanged): ").strip()

        # Check if any field is left blank, if so, keep the existing value
        if not new_item_name:
            new_item_name = row[1]
        if not new_quantity:
            new_quantity = row[2]
        if not new_price:
            new_price = row[3]

        # Update the item with new details
        cur.execute('UPDATE users SET item_name=?, quantity=?, price=? WHERE id=?',
                    (new_item_name, new_quantity, new_price, item_id_to_modify))
        print("Item modified successfully.")

def DeleteItem():
    fetchItems()

    item_id_to_delete = input("Enter the item ID to delete: ")

    db = sqlite3.connect('restaurant_items.db')
    with db:
        cur = db.cursor()
        cur.execute('SELECT * FROM users WHERE id=?', (item_id_to_delete,))
        row = cur.fetchone()

        if not row:
            print("Item not found.")
            return

        print("Item to Delete:")
        print("Item ID:", row[0])
        print("Item Name:", row[1])
        print("Quantity:", row[2])
        print("Price:", row[3])

        confirm_delete = input("Are you sure you want to delete this item? (Y/N): ").strip().upper()

        if confirm_delete == 'Y':
            cur.execute('DELETE FROM users WHERE id=?', (item_id_to_delete,))
            print("Item deleted successfully.")
        else:
            print("Deletion canceled.")

def DeleteAll():
    confirm_delete = input("Are you sure you want to delete all the items? This action cannot be undone. (Y/N): ").strip().upper()
    if confirm_delete == 'Y':
        db = sqlite3.connect('restaurant_items.db')
        with db:
            cur = db.cursor()
            cur.execute("DELETE FROM users")
            print("All items deleted successfully")
    else:
        print("Deletion cancelled")

def MainMenu():
    print("Please select below options")
    print("1. View All Items")
    print("2. Add new item to the menu")
    print("3. Modify existing item name, qty, price")
    print("4. Delete Item")
    print("5. Delete All")

    while True:
        userinput = input("Enter a value or ('Q' to quit):").upper()
        if userinput == 'Q':
            break
        elif userinput == '1':
            fetchItems()
            MainMenu()
        elif userinput == '2':
            AddItems()
            MainMenu()
        elif userinput == '3':
           ModifyItems()
           MainMenu()
        elif userinput == '4':
            DeleteItem()
            MainMenu()
        elif userinput == '5':
            DeleteAll()
            MainMenu()

MainMenu()