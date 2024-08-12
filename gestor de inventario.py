import tkinter as tk
from tkinter import messagebox

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity, price):
        if name in self.products:
            return f"El producto '{name}' ya existe."
        else:
            self.products[name] = {'quantity': quantity, 'price': price}
            return f"Producto '{name}' agregado con éxito."

    def update_product(self, name, quantity=None, price=None):
        if name in self.products:
            if quantity is not None:
                self.products[name]['quantity'] = quantity
            if price is not None:
                self.products[name]['price'] = price
            return f"Producto '{name}' actualizado con éxito."
        else:
            return f"El producto '{name}' no existe en el inventario."

    def delete_product(self, name):
        if name in self.products:
            del self.products[name]
            return f"Producto '{name}' eliminado con éxito."
        else:
            return f"El producto '{name}' no existe en el inventario."

    def display_inventory(self):
        if not self.products:
            return "El inventario está vacío."
        else:
            inventory_list = ["Inventario actual:"]
            for name, details in self.products.items():
                inventory_list.append(f"Producto: {name}, Cantidad: {details['quantity']}, Precio: {details['price']}")
            return "\n".join(inventory_list)

class InventoryApp:
    def __init__(self, root):
        self.inventory = Inventory()
        self.root = root
        self.root.title("Gestión de Inventario")

        # Crear widgets
        self.label_name = tk.Label(root, text="Nombre del producto:")
        self.label_quantity = tk.Label(root, text="Cantidad:")
        self.label_price = tk.Label(root, text="Precio:")
        
        self.entry_name = tk.Entry(root)
        self.entry_quantity = tk.Entry(root)
        self.entry_price = tk.Entry(root)

        self.button_add = tk.Button(root, text="Agregar", command=self.add_product)
        self.button_update = tk.Button(root, text="Actualizar", command=self.update_product)
        self.button_delete = tk.Button(root, text="Eliminar", command=self.delete_product)
        self.button_display = tk.Button(root, text="Mostrar Inventario", command=self.display_inventory)

        # Posicionar widgets en la ventana
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.label_quantity.grid(row=1, column=0, padx=5, pady=5)
        self.label_price.grid(row=2, column=0, padx=5, pady=5)

        self.entry_name.grid(row=0, column=1, padx=5, pady=5)
        self.entry_quantity.grid(row=1, column=1, padx=5, pady=5)
        self.entry_price.grid(row=2, column=1, padx=5, pady=5)

        self.button_add.grid(row=3, column=0, padx=5, pady=5)
        self.button_update.grid(row=3, column=1, padx=5, pady=5)
        self.button_delete.grid(row=4, column=0, padx=5, pady=5)
        self.button_display.grid(row=4, column=1, padx=5, pady=5)

    def add_product(self):
        name = self.entry_name.get()
        quantity = int(self.entry_quantity.get())
        price = float(self.entry_price.get())
        result = self.inventory.add_product(name, quantity, price)
        messagebox.showinfo("Resultado", result)

    def update_product(self):
        name = self.entry_name.get()
        quantity = int(self.entry_quantity.get())
        price = float(self.entry_price.get())
        result = self.inventory.update_product(name, quantity, price)
        messagebox.showinfo("Resultado", result)

    def delete_product(self):
        name = self.entry_name.get()
        result = self.inventory.delete_product(name)
        messagebox.showinfo("Resultado", result)

    def display_inventory(self):
        inventory = self.inventory.display_inventory()
        messagebox.showinfo("Inventario", inventory)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

