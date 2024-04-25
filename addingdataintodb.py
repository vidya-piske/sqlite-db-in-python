import sqlite3

def addingdataintotable():
    item_name = input("Enter item_name:")
    quantity = input("Enter quantity:")
    price = input("Enter price:")
    
    db = sqlite3.connect('items.db')
    cur = db.cursor()
    cur.execute("INSERT INTO datatable (item_name, quantity, price) VALUES (?, ?, ?)", (item_name, quantity, price))
    db.commit()
    db.close()
    print("Data inserted")

def MainMenu():
    print("Select options from below:")
    print("1. Insert data into menu items")
    while True:
        user_input = input("Enter a value or ('Q' to quit):").upper()
        if user_input == 'Q': 
            break
        elif user_input == '1':
            addingdataintotable()

MainMenu()
