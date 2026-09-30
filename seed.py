import sqlite3

def seed_data(db_name="ecommerce.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        role TEXT DEFAULT 'Customer',
        wallet_balance REAL DEFAULT 0.00
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        product_type TEXT NOT NULL,
        base_price REAL NOT NULL,
        stock_quantity INTEGER DEFAULT 0
    );
    """)

    users = [
        (1, 'Alice Smith', 'alice@example.com', 'Customer', 500.00),
        (2, 'Bob Jones', 'bob@example.com', 'Customer', 150.00),
        (3, 'Store Manager', 'admin@store.com', 'Admin', 0.00)
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO Users (user_id, name, email, role, wallet_balance) VALUES (?, ?, ?, ?, ?)",
        users
    )

    products = [
        ('Wireless Headphones', 'Physical', 79.99, 25),
        ('Ergonomic Chair', 'Physical', 199.99, 10),
        ('SQL Advanced Guide PDF', 'Digital', 15.00, 9999),
        ('Python OOP Handbook', 'Digital', 20.00, 9999)
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO Products (title, product_type, base_price, stock_quantity) VALUES (?, ?, ?, ?)",
        products
    )

    conn.commit()
    conn.close()
    print("✅ Mock data inserted successfully into ecommerce.db")

if __name__ == "__main__":
    seed_data()
    