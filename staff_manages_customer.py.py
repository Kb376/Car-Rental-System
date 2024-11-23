import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class ManageCustomerAccount:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Customer Accounts")
        self.root.geometry("900x600")

        # Database setup
        self.conn = sqlite3.connect("car_rental.db")
        self.cursor = self.conn.cursor()
        self.setup_database()

        # Build the interface
        self.build_ui()

    def setup_database(self):
        """Create the customers table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE
            )
        """)
        self.conn.commit()

    def build_ui(self):
        """Build the user interface."""
        # Title
        tk.Label(self.root, text="Customer Account Management", font=("Arial", 16, "bold")).pack(pady=10)

        # Form Section
        form_frame = tk.Frame(self.root, bd=2, relief="ridge", padx=10, pady=10)
        form_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.phone_entry = tk.Entry(form_frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(form_frame, text="Add New Customer", command=self.add_customer, bg="#007BFF", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

        # Customer Table Section
        self.table_frame = tk.Frame(self.root, bd=2, relief="ridge", padx=10, pady=10)
        self.table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.customer_table = ttk.Treeview(self.table_frame, columns=("ID", "Name", "Phone", "Email"), show="headings")
        self.customer_table.heading("ID", text="ID")
        self.customer_table.heading("Name", text="Name")
        self.customer_table.heading("Phone", text="Phone")
        self.customer_table.heading("Email", text="Email")
        self.customer_table.column("ID", width=50)
        self.customer_table.column("Name", width=200)
        self.customer_table.column("Phone", width=150)
        self.customer_table.column("Email", width=200)
        self.customer_table.pack(fill="both", expand=True)

        self.customer_table.bind("<Double-1>", self.select_customer)

        # Action Buttons
        action_frame = tk.Frame(self.root, bd=2, relief="ridge", padx=10, pady=10)
        action_frame.pack(pady=10, padx=20, fill="x")

        tk.Button(action_frame, text="Modify Existing", command=self.update_customer, bg="#28A745", fg="white").pack(side="left", padx=10)
        tk.Button(action_frame, text="Delete Existing", command=self.delete_customer, bg="#DC3545", fg="white").pack(side="right", padx=10)

        self.load_customers()

    def load_customers(self):
        """Load customers from the database into the table."""
        for row in self.customer_table.get_children():
            self.customer_table.delete(row)

        self.cursor.execute("SELECT * FROM customers")
        for customer in self.cursor.fetchall():
            self.customer_table.insert("", "end", values=customer)

    def add_customer(self):
        """Add a new customer to the database."""
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if not name or not phone or not email:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            self.cursor.execute("INSERT INTO customers (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
            self.conn.commit()
            messagebox.showinfo("Success", "Customer added successfully!")
            self.clear_form()
            self.load_customers()
        except sqlite3.IntegrityError as e:
            messagebox.showerror("Error", f"Integrity Error: {e}")

    def update_customer(self):
        """Update the selected customer's information."""
        selected_item = self.customer_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a customer to update.")
            return

        customer_id = self.customer_table.item(selected_item)["values"][0]
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if not name or not phone or not email:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            self.cursor.execute("UPDATE customers SET name = ?, phone = ?, email = ? WHERE customer_id = ?", (name, phone, email, customer_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Customer updated successfully!")
            self.clear_form()
            self.load_customers()
        except sqlite3.IntegrityError as e:
            messagebox.showerror("Error", f"Integrity Error: {e}")

    def delete_customer(self):
        """Delete the selected customer."""
        selected_item = self.customer_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a customer to delete.")
            return

        customer_id = self.customer_table.item(selected_item)["values"][0]

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this customer?")
        if confirm:
            self.cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Customer deleted successfully!")
            self.load_customers()

    def select_customer(self, event):
        """Populate the form fields with the selected customer's information."""
        selected_item = self.customer_table.selection()
        if not selected_item:
            return

        customer = self.customer_table.item(selected_item)["values"]
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, customer[1])
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, customer[2])
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, customer[3])

    def clear_form(self):
        """Clear the form fields."""
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def __del__(self):
        """Close the database connection."""
        self.conn.close()


# Run the application independently
if __name__ == "__main__":
    root = tk.Tk()
    app = ManageCustomerAccount(root)
    root.mainloop()
