import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CarRentalAdminGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Rental Admin")
        self.cars = {}  # {car_id: {"model": str, "available": bool}}

        # Title Label
        tk.Label(self.root, text="Car Rental Admin Panel", font=("Arial", 16)).pack(pady=10)

        # Buttons
        tk.Button(self.root, text="Add New Car as Available", command=self.add_car_available, width=30).pack(pady=5)
        tk.Button(self.root, text="Add New Car as Unavailable", command=self.add_car_unavailable, width=30).pack(pady=5)
        tk.Button(self.root, text="Modify Existing Account", command=self.modify_car, width=30).pack(pady=5)
        tk.Button(self.root, text="Delete Account", command=self.delete_car, width=30).pack(pady=5)

        # Exit Button
        tk.Button(self.root, text="Exit", command=self.root.quit, width=30).pack(pady=10)

    def add_car_available(self):
        """Add a new car as available."""
        self.add_car_window(available=True)

    def add_car_unavailable(self):
        """Add a new car as unavailable."""
        self.add_car_window(available=False)

    def add_car_window(self, available):
        """Window to add a new car."""
        def save_car():
            car_id = car_id_entry.get()
            model = model_entry.get()

            if not car_id or not model:
                messagebox.showerror("Error", "All fields are required!")
                return

            if car_id in self.cars:
                messagebox.showerror("Error", "Car ID already exists!")
            else:
                self.cars[car_id] = {"model": model, "available": available}
                status = "AVAILABLE for rent" if available else "UNAVAILABLE for rent"
                messagebox.showinfo("Success", f"Car {car_id} ({model}) added successfully as {status}!")
                add_car_win.destroy()

        add_car_win = tk.Toplevel(self.root)
        add_car_win.title("Add Car")
        tk.Label(add_car_win, text="Car ID:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(add_car_win, text="Model:").grid(row=1, column=0, padx=10, pady=5)

        car_id_entry = tk.Entry(add_car_win)
        model_entry = tk.Entry(add_car_win)

        car_id_entry.grid(row=0, column=1, padx=10, pady=5)
        model_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(add_car_win, text="Save", command=save_car).grid(row=2, columnspan=2, pady=10)

    def modify_car(self):
        """Window to modify an existing car."""
        def save_modifications():
            car_id = car_id_entry.get()
            new_model = model_entry.get()
            new_available = available_dropdown.get()

            if car_id not in self.cars:
                messagebox.showerror("Error", "Car not found!")
            else:
                if new_model:
                    self.cars[car_id]["model"] = new_model
                self.cars[car_id]["available"] = new_available == "Yes"
                status = "AVAILABLE for rent" if self.cars[car_id]["available"] else "UNAVAILABLE for rent"
                messagebox.showinfo("Success", f"Car modified successfully! New status: {status}.")
                modify_car_win.destroy()

        modify_car_win = tk.Toplevel(self.root)
        modify_car_win.title("Modify Car")
        tk.Label(modify_car_win, text="Car ID:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(modify_car_win, text="New Model:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(modify_car_win, text="Available (Yes/No):").grid(row=2, column=0, padx=10, pady=5)

        car_id_entry = tk.Entry(modify_car_win)
        model_entry = tk.Entry(modify_car_win)
        available_dropdown = ttk.Combobox(modify_car_win, values=["Yes", "No"], state="readonly")
        available_dropdown.set("Yes")

        car_id_entry.grid(row=0, column=1, padx=10, pady=5)
        model_entry.grid(row=1, column=1, padx=10, pady=5)
        available_dropdown.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(modify_car_win, text="Save", command=save_modifications).grid(row=3, columnspan=2, pady=10)

    def delete_car(self):
        """Window to delete an existing car."""
        def confirm_delete():
            car_id = car_id_entry.get()

            if car_id not in self.cars:
                messagebox.showerror("Error", "Car not found!")
            else:
                del self.cars[car_id]
                messagebox.showinfo("Success", f"Car {car_id} deleted successfully!")
                delete_car_win.destroy()

        delete_car_win = tk.Toplevel(self.root)
        delete_car_win.title("Delete Car")
        tk.Label(delete_car_win, text="Car ID:").grid(row=0, column=0, padx=10, pady=5)
        car_id_entry = tk.Entry(delete_car_win)
        car_id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(delete_car_win, text="Delete", command=confirm_delete).grid(row=1, columnspan=2, pady=10)

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = CarRentalAdminGUI(root)
    root.mainloop()
