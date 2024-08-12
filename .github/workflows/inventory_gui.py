import tkinter as tk
from tkinter import messagebox
import json

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")

        self.inventory = {}
        self.load_inventory()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Product ID").grid(row=0, column=0)
        self.product_id_entry = tk.Entry(self.root)
        self.product_id_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Product Name").grid(row=1, column=0)
        self.product_name_entry = tk.Entry(self.root)
        self.product_name_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Quantity").grid(row=2, column=0)
        self.product_quantity_entry = tk.Entry(self.root)
        self.product_quantity_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Price").grid(row=3, column=0)
        self.product_price_entry = tk.Entry(self.root)
        self.product_price_entry.grid(row=3, column=1)

        tk.Button(self.root, text="Add Product", command=self.add_product).grid(row=4, column=0, columnspan=2)

    def load_inventory(self):
        try:
            with open('inventory.json', 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            self.inventory = {}

    def save_inventory(self):
        with open('inventory.json', 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_product(self):
        product_id = self.product_id_entry.get()
        name = self.product_name_entry.get()
        quantity = self.product_quantity_entry.get()
        price = self.product_price_entry.get()

        if not product_id or not name or not quantity or not price:
            messagebox.showerror("Input Error", "All fields must be filled")
            return

        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            messagebox.showerror("Input Error", "Quantity and Price must be valid numbers")
            return

        if product_id in self.inventory:
            messagebox.showerror("Duplicate Error", "Product ID already exists")
            return

        self.inventory[product_id] = {'name': name, 'quantity': quantity, 'price': price}
        self.save_inventory()
        messagebox.showinfo("Success", "Product added successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()
