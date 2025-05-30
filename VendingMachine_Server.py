import socket
import sqlite3
from sqlite3 import Error
import datetime

def create_database():
    try:
        conn = sqlite3.connect('items.db')
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS items")

        cursor.execute('''CREATE TABLE items
                          (id INTEGER PRIMARY KEY, item TEXT NOT NULL, price REAL NOT NULL)''')

        items_data = [
            (101, 'Water', 1.00),
            (102, 'Water', 1.00),
            (103, 'Water', 1.00),
            (104, 'Water', 1.00),
            (205, 'Energy Drink', 3.00),
            (206, 'Energy Drink', 3.00),
            (207, 'Energy Drink', 3.00),
            (208, 'Energy Drink', 3.00),
            (309, 'Choco Spheres', 4.00),
            (310, 'Choco Spheres', 4.00),
            (311, 'Choco Spheres', 4.00),
            (312, 'Choco Spheres', 4.00),
            (413, 'Juice', 2.00),
            (414, 'Juice', 2.00),
            (415, 'Juice', 2.00),
            (416, 'Juice', 2.00)
        ]
        cursor.executemany("INSERT INTO items (id, item, price) VALUES (?, ?, ?)", items_data)

        conn.commit()
        conn.close()
        print("Database created successfully")

    except Error as e:
        print(f"Error creating database: {e}")


def update_database(client, item_id):
    conn = sqlite3.connect('items.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()

    if item:
        item_info = f"Item ID: {item[0]}, Item: {item[1]}, Price: {item[2]}"
        client.send("Item found: ".encode() + str(item_info).encode())
        
        cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
        conn.commit()
        print(f"Item with ID {item_id} removed from the database.")
        
    else:
        print("Item not found")
        client.send("Item not found".encode())

    conn.close()

def handle_client(client, addr):
    log_file = open("transaction_log.txt", "a")

    print(f"Connected to {addr}")
    
    purchased_items = []

    while True:
        data = client.recv(1024).decode("utf-8")
        if not data:
            break

        if data == "cancel":
            reset_database()
            print("Database reset")
            purchased_items.clear()
            continue

        item_id = int(data)
        if item_id == 0:
            continue
        
        update_database(client, item_id)
        
        purchased_items.append(item_id)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for item_id in purchased_items:
        item_info = f"Item ID: {item_id}"
        log_file.write(f"Transaction at {timestamp}: {item_info} purchased\n")

    log_file.close()

def reset_database():
    try:
        conn = sqlite3.connect('items.db')
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS items")

        cursor.execute('''CREATE TABLE items
                          (id INTEGER PRIMARY KEY, item TEXT NOT NULL, price REAL NOT NULL)''')

        items_data = [
            (101, 'Water', 1.00),
            (102, 'Water', 1.00),
            (103, 'Water', 1.00),
            (104, 'Water', 1.00),
            (205, 'Energy Drink', 3.00),
            (206, 'Energy Drink', 3.00),
            (207, 'Energy Drink', 3.00),
            (208, 'Energy Drink', 3.00),
            (309, 'Choco Spheres', 4.00),
            (310, 'Choco Spheres', 4.00),
            (311, 'Choco Spheres', 4.00),
            (312, 'Choco Spheres', 4.00),
            (413, 'Juice', 2.00),
            (414, 'Juice', 2.00),
            (415, 'Juice', 2.00),
            (416, 'Juice', 2.00)
        ]
        cursor.executemany("INSERT INTO items (id, item, price) VALUES (?, ?, ?)", items_data)

        conn.commit()
        conn.close()
        print("Database reset successfully")

    except Error as e:
        print(f"Error resetting database: {e}")


def main():
    host = 'localhost'
    port = 65432

    create_database()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    server.listen()
    print(f"Server listening on {host}:{port}")

    while True:
        client, addr = server.accept()
        handle_client(client, addr)

if __name__ == "__main__":
    main()
