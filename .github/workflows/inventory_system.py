import json

# Sample data structure for the inventory
inventory = {}

# Functions to manage inventory
def load_inventory():
    global inventory
    try:
        with open('inventory.json', 'r') as file:
            inventory = json.load(file)
    except FileNotFoundError:
        inventory = {}

def save_inventory():
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file, indent=4)

def add_product(product_id, name, quantity, price):
    if product_id in inventory:
        print("Product ID already exists.")
        return
    inventory[product_id] = {'name': name, 'quantity': quantity, 'price': price}
    print("Product added successfully.")

def edit_product(product_id, name=None, quantity=None, price=None):
    if product_id not in inventory:
        print("Product not found.")
        return
    if name is not None:
        inventory[product_id]['name'] = name
    if quantity is not None:
        inventory[product_id]['quantity'] = quantity
    if price is not None:
        inventory[product_id]['price'] = price
    print("Product updated successfully.")

def delete_product(product_id):
    if product_id in inventory:
        del inventory[product_id]
        print("Product deleted successfully.")
    else:
        print("Product not found.")

def report_low_stock(threshold):
    low_stock = {pid: details for pid, details in inventory.items() if details['quantity'] < threshold}
    if low_stock:
        print("Low Stock Report:")
        for pid, details in low_stock.items():
            print(f"ID: {pid}, Name: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}")
    else:
        print("No products are below the stock threshold.")

# Main function for command-line interaction
def main():
    load_inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Edit Product")
        print("3. Delete Product")
        print("4. Low Stock Report")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            pid = input("Enter product ID: ")
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            add_product(pid, name, quantity, price)
        elif choice == '2':
            pid = input("Enter product ID: ")
            name = input("Enter new product name (leave blank to keep unchanged): ")
            quantity = input("Enter new quantity (leave blank to keep unchanged): ")
            price = input("Enter new price (leave blank to keep unchanged): ")
            quantity = int(quantity) if quantity else None
            price = float(price) if price else None
            edit_product(pid, name if name else None, quantity, price)
        elif choice == '3':
            pid = input("Enter product ID to delete: ")
            delete_product(pid)
        elif choice == '4':
            threshold = int(input("Enter stock threshold: "))
            report_low_stock(threshold)
        elif choice == '5':
            save_inventory()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
