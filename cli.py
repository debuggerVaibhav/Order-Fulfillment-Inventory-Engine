import sqlite3

def display_products():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    cursor.execute("SELECT product_id, title, product_type, base_price, stock_quantity FROM Products")
    products = cursor.fetchall()
    conn.close()

    print("\n" + "="*55)
    print(f"{'ID':<5} {'Title':<25} {'Type':<10} {'Price ($)':<8} {'Stock':<5}")
    print("="*55)
    for p in products:
        print(f"{p[0]:<5} {p[1]:<25} {p[2]:<10} ${p[3]:<7.2f} {p[4]:<5}")
    print("="*55)

def main_menu():
    while True:
        print("\n=== E-COMMERCE ENGINE TERMINAL ===")
        print("1. View Store Products")
        print("2. Check User Wallet Balance")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            display_products()
        elif choice == "2":
            user_id = input("Enter User ID: ").strip()
            conn = sqlite3.connect("ecommerce.db")
            cursor = conn.cursor()
            cursor.execute("SELECT name, wallet_balance FROM Users WHERE user_id = ?", (user_id,))
            user = cursor.fetchone()
            conn.close()
            if user:
                print(f"\nUser: {user[0]} | Wallet Balance: ${user[1]:.2f}")
            else:
                print("\n❌ User ID not found.")
        elif choice == "3":
            print("Exiting application...")
            break

if __name__ == "__main__":
    main_menu()
    