import tkinter as tk
from tkinter import ttk,messagebox

class restaurantordermanagement:
    def __init__(self,root):
        self.root = root
        self.root.title("Restaurant Order Management")
        self.root.geometry("800x600")
        
        self.menu_items = {
            "Pizza": 10.99,
            "Burger": 7.99,
            "Pasta": 8.99,
            "Salad": 5.99,
            "Soda": 1.99
        }
        
        self.exchange_rate = 82.0
        self.setup_background(root)
        
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        ttk.Label(frame, text="Restaurant Order Management:").grid(row=0, column=0, padx=10, pady=10)
        
        self.menu_labels = {}
        self.menu_quantities = {}
        
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            self.menu_labels[item] = ttk.Label(frame, text=f"{item} (${price})")
            self.menu_labels[item].grid(row=i, column=0, padx=10, pady=5)
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry
        
        self.currency_var = tk.StringVar()
        ttk.Label(frame, text="Select Currency:").grid(row=len(self.menu_items)+1, column=0, padx=10, pady=10)
        
        currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, values=["USD", "INR"], state="readonly")
        currency_dropdown.grid(row=len(self.menu_items)+1, column=1, padx=10, pady=10)
        currency_dropdown.current(0)
        self.currency_var.trace("w", self.update_menu_prices)
        
        order_btn = ttk.Button(frame, text="Place Order", command=self.place_order)
        order_btn.grid(row=len(self.menu_items)+2, column=0, columnspan=2, pady=20)
        

        
    
    
    
            
            