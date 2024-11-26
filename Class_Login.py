import tkinter as tk
from tkinter import messagebox
import time


class CarRentalSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Rental System - Login")
        self.root.geometry("400x400")
        self.logged_in = False
        self.username = None
        self.last_active_time = None  # To track session timeout

        # In-memory user credentials with roles
        self.users = {
            "admin": {"password": "admin123", "role": "Admin"},
            "user1": {"password": "mypassword", "role": "Staff"}
        }

        # Show the login screen
        self.show_login_screen()

    def show_login_screen(self):
        """Displays the login screen."""
        self.clear_screen()

        tk.Label(self.root, text="Car Rental System", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text="Login", font=("Arial", 14)).pack(pady=10)

        # Role Selection Dropdown
        tk.Label(self.root, text="Select Role:").pack()
        self.role_var = tk.StringVar(value="Select Role")  # Default value
        role_dropdown = tk.OptionMenu(self.root, self.role_var, "Admin", "Staff")
        role_dropdown.pack(pady=10)

        # Username and Password Entry
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        # Error Message Label
        self.error_label = tk.Label(self.root, text="", fg="red", font=("Arial", 10))
        self.error_label.pack(pady=10)

        # Buttons
        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Quit", command=self.root.quit).pack()

    def login(self):
        """Handles user login."""
        role = self.role_var.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Clear any previous error message
        self.error_label.config(text="")

        if role == "Select Role":
            self.error_label.config(text="Please select a role.")
            return

        if not username or not password:
            self.error_label.config(text="Username and password cannot be empty.")
            return

        # Validate credentials and role
        if username in self.users:
            user = self.users[username]
            if user["password"] == password and user["role"] == role:
                self.logged_in = True
                self.username = username
                self.last_active_time = time.time()
                self.show_home_screen()
            else:
                self.error_label.config(text="Invalid username and/or password. Try again.")
        else:
            self.error_label.config(text="Invalid username and/or password. Try again.")

    def show_home_screen(self):
        """Displays the home screen after successful login."""
        self.clear_screen()

        tk.Label(self.root, text="Car Rental System", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text=f"Welcome, {self.username}!", font=("Arial", 12)).pack(pady=5)

        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=10)
        tk.Button(self.root, text="Quit", command=self.root.quit).pack()

    def logout(self):
        """Handles user logout."""
        self.logged_in = False
        self.username = None
        self.last_active_time = None
        self.show_login_screen()

    def clear_screen(self):
        """Clears the current screen."""
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the app if this file is executed directly
if __name__ == "__main__":
    root = tk.Tk()
    app = CarRentalSystem(root)
    root.mainloop()
