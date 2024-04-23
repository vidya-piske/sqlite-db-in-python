import sqlite3

id = input("Enter Item ID: ")

# Printing the input
print("You entered:", id)

item_name = input("Enter Item name: ")

# Printing the input
print("You entered:", item_name)

qty = input("Enter Qty: ")

# Printing the input
print("You entered qty:", qty)

price = input("Enter Price for "+item_name+":")

# Printing the input
print("You entered price:", price)

data = ((id, item_name,qty,price),)

db = sqlite3.connect('restaurant_items.db')
 
with db:
    cur = db.cursor()
    cur.executemany('INSERT INTO users VALUES (?,?,?,?)', data)
    print("Data inserted")

