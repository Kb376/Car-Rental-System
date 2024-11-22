import tkinter as tk
from tkinter import messagebox
from LoginTest1 import CarRentalSystem  # Import the login system

# Navigation Functions
def open_login():
    """Open the Login Window."""
    login_root = tk.Toplevel(root)
    CarRentalSystem(login_root)

def open_reservation():
    """Placeholder for Reservation Page."""
    messagebox.showinfo("Navigation", "Navigating to Reservations page...")

def open_return():
    """Placeholder for Returns Page."""
    messagebox.showinfo("Navigation", "Navigating to Returns page...")

def open_inventory():
    """Placeholder for Inventory Management Page."""
    messagebox.showinfo("Navigation", "Navigating to Inventory Management page...")

def open_customer_portal():
    """Placeholder for Customer Portal."""
    messagebox.showinfo("Navigation", "Navigating to Customer Portal page...")

# Main Window
root = tk.Tk()
root.title("Rental Car System - Home")
root.geometry("900x600")  # Increased size for better layout
root.resizable(False, False)

# Header
header_frame = tk.Frame(root)
header_frame.pack(pady=20)

header_label = tk.Label(header_frame, text="Welcome to the Rental Car System", font=("Helvetica", 16, "bold"))
header_label.pack()

subheader_label = tk.Label(header_frame, text="Select an option below to get started", font=("Helvetica", 12))
subheader_label.pack()

# Card Container
card_container = tk.Frame(root)
card_container.pack(pady=20)

# Card Function
def create_card(parent, row, col, title, description, command):
    """Helper function to create navigation cards."""
    card = tk.Frame(parent, relief="raised", borderwidth=2, padx=20, pady=20, width=200, height=150)
    card.grid(row=row, column=col, padx=20, pady=20)  # Add spacing between cards

    title_label = tk.Label(card, text=title, font=("Helvetica", 14, "bold"))
    title_label.pack(pady=5)

    description_label = tk.Label(card, text=description, wraplength=180, justify="center")
    description_label.pack(pady=10)

    button = tk.Button(card, text="Go", command=command, bg="#007BFF", fg="white", font=("Helvetica", 10))
    button.pack(pady=5)

# Cards (Arranged in Grid)
create_card(card_container, 0, 0, "Login", "Click here to login", open_login)
create_card(card_container, 0, 1, "Make a Reservation", "Create new reservations for clients.", open_reservation)
create_card(card_container, 0, 2, "Return a Car", "Process vehicle returns efficiently.", open_return)
create_card(card_container, 1, 0, "Inventory Management", "Track and update vehicle inventory.", open_inventory)
create_card(card_container, 1, 1, "Customer Portal", "Access client information and rental history.", open_customer_portal)

# Footer
footer_frame = tk.Frame(root)
footer_frame.pack(pady=20)

footer_label = tk.Label(footer_frame, text="© 2024 Car Rental System", font=("Helvetica", 10))
footer_label.pack()

footer_link = tk.Button(footer_frame, text="Back to Homepage", command=root.quit, fg="blue", font=("Helvetica", 10))
footer_link.pack()

# Run the App
root.mainloop()

