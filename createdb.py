import sqlite3  

def main():
    try:
        db = sqlite3.connect("restaurant_items.db")
        print("Database created", db)
    except:
        print("Failed to create Database")

if __name__ == "__main__":
    main()