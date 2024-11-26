import tkinter as tk
from tkinter import ttk, messagebox
from car_data import car_data  # Import car data


class CarRentalAdminGUI:
    def __init__(self, root, logged_in=False, role=None):
        # Check access
        if not logged_in or role != "Staff":
            messagebox.showerror("Access Denied", "You must log in as a Staff member to access this feature.")
            root.destroy()  # Close the window immediately
            return

        self.root = root
        self.root.title("Car Rental Staff - Manage Cars")
        self.car_data = car_data  # Use imported car data

        # Title Label
        tk.Label(self.root, text="Car Rental - Manage Cars", font=("Arial", 16, "bold")).pack(pady=10)

        # Buttons
        tk.Button(self.root, text="Add New Car", command=self.add_car, width=30).pack(pady=5)
        tk.Button(self.root, text="Modify Existing Car", command=self.modify_car, width=30).pack(pady=5)
        tk.Button(self.root, text="Delete Car", command=self.delete_car, width=30).pack(pady=5)
        tk.Button(self.root, text="View All Cars", command=self.view_cars, width=30).pack(pady=5)

        # Back Button
        tk.Button(self.root, text="Back to Main Menu", command=self.go_back, width=30).pack(pady=10)

    def add_car(self):
        """Window to add a new car."""
        def save_car():
            make = make_entry.get().strip()
            model = model_entry.get().strip()
            available_from = from_entry.get().strip()
            available_to = to_entry.get().strip()

            if not make or not model or not available_from or not available_to:
                messagebox.showerror("Error", "All fields are required!")
                return

            self.car_data.append({
                "make": make,
                "model": model,
                "available_from": available_from,
                "available_to": available_to
            })
            messagebox.showinfo("Success", f"Car {make} {model} added successfully!")
            add_car_win.destroy()

        add_car_win = tk.Toplevel(self.root)
        add_car_win.title("Add Car")
        tk.Label(add_car_win, text="Make:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(add_car_win, text="Model:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(add_car_win, text="Available From (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(add_car_win, text="Available To (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)

        make_entry = tk.Entry(add_car_win)
        model_entry = tk.Entry(add_car_win)
        from_entry = tk.Entry(add_car_win)
        to_entry = tk.Entry(add_car_win)

        make_entry.grid(row=0, column=1, padx=10, pady=5)
        model_entry.grid(row=1, column=1, padx=10, pady=5)
        from_entry.grid(row=2, column=1, padx=10, pady=5)
        to_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(add_car_win, text="Save", command=save_car).grid(row=4, columnspan=2, pady=10)

    def modify_car(self):
        """Window to modify an existing car."""
        def save_modifications():
            selected_index = car_listbox.curselection()
            if not selected_index:
                messagebox.showerror("Error", "Please select a car to modify.")
                return

            selected_index = selected_index[0]
            new_make = make_entry.get().strip()
            new_model = model_entry.get().strip()
            new_from = from_entry.get().strip()
            new_to = to_entry.get().strip()

            if not new_make or not new_model or not new_from or not new_to:
                messagebox.showerror("Error", "All fields are required!")
                return

            self.car_data[selected_index] = {
                "make": new_make,
                "model": new_model,
                "available_from": new_from,
                "available_to": new_to
            }
            messagebox.showinfo("Success", "Car modified successfully!")
            modify_car_win.destroy()

        modify_car_win = tk.Toplevel(self.root)
        modify_car_win.title("Modify Car")

        car_listbox = tk.Listbox(modify_car_win, width=50)
        car_listbox.pack(pady=10)
        for car in self.car_data:
            car_listbox.insert(tk.END, f"{car['make']} {car['model']} ({car['available_from']} - {car['available_to']})")

        tk.Label(modify_car_win, text="New Make:").pack()
        make_entry = tk.Entry(modify_car_win)
        make_entry.pack(pady=5)

        tk.Label(modify_car_win, text="New Model:").pack()
        model_entry = tk.Entry(modify_car_win)
        model_entry.pack(pady=5)

        tk.Label(modify_car_win, text="New Available From (YYYY-MM-DD):").pack()
        from_entry = tk.Entry(modify_car_win)
        from_entry.pack(pady=5)

        tk.Label(modify_car_win, text="New Available To (YYYY-MM-DD):").pack()
        to_entry = tk.Entry(modify_car_win)
        to_entry.pack(pady=5)

        tk.Button(modify_car_win, text="Save", command=save_modifications).pack(pady=10)

    def delete_car(self):
        """Window to delete an existing car."""
        def confirm_delete():
            selected_index = car_listbox.curselection()
            if not selected_index:
                messagebox.showerror("Error", "Please select a car to delete.")
                return

            selected_index = selected_index[0]
            del self.car_data[selected_index]
            messagebox.showinfo("Success", "Car deleted successfully!")
            delete_car_win.destroy()

        delete_car_win = tk.Toplevel(self.root)
        delete_car_win.title("Delete Car")

        car_listbox = tk.Listbox(delete_car_win, width=50)
        car_listbox.pack(pady=10)
        for car in self.car_data:
            car_listbox.insert(tk.END, f"{car['make']} {car['model']} ({car['available_from']} - {car['available_to']})")

        tk.Button(delete_car_win, text="Delete", command=confirm_delete).pack(pady=10)

    def view_cars(self):
        """Display all cars."""
        view_win = tk.Toplevel(self.root)
        view_win.title("All Cars")
        for car in self.car_data:
            tk.Label(view_win, text=f"{car['make']} {car['model']} ({car['available_from']} - {car['available_to']})").pack()

    def go_back(self):
        """Return to the main menu."""
        self.root.destroy()


# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = CarRentalAdminGUI(root, logged_in=True, role="Staff")  # Test with access
    root.mainloop()
