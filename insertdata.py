import sqlite3

myuser = (
    (1, 'manchuria', 2, 200),
    (2, 'veg biryani', 1, 300),
    (3, 'noodles', 1, 100),
    (4, 'corn', 2, 400),
)

# myuser = (
#     (5, 'soup', 2, 200),
# )

# new_column =((6,'manchow',1,100),)

db = sqlite3.connect('restaurant_items.db')
 
with db:
    cur = db.cursor()
    cur.executemany('INSERT INTO users VALUES (?,?,?,?)', myuser)
    print("Data inserted")



if item_name exist in table:
    print("Duplicate Item name")
else:
    #insert