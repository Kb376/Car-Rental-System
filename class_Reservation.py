import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime
import json
import os

# File to store reservation data
RESERVATION_FILE = "reservations.json"

# Sample car data - this can be used for availability checking
car_data = [
    {"car_id": 1, "make": "Toyota", "model": "Camry", "available_from": "2023-12-01", "available_to": "2023-12-31"},
    {"car_id": 2, "make": "Toyota", "model": "Corolla", "available_from": "2023-12-15", "available_to": "2024-01-15"},
    {"car_id": 3, "make": "Honda", "model": "Civic", "available_from": "2023-12-10", "available_to": "2023-12-20"},
    {"car_id": 4, "make": "Honda", "model": "Accord", "available_from": "2023-12-05", "available_to": "2023-12-25"},
    {"car_id": 5, "make": "Ford", "model": "Focus", "available_from": "2023-12-01", "available_to": "2023-12-15"},
    {"car_id": 6, "make": "Ford", "model": "Escape", "available_from": "2023-12-10", "available_to": "2023-12-30"},
    {"car_id": 7, "make": "Chevrolet", "model": "Malibu", "available_from": "2023-12-01", "available_to": "2023-12-31"},
    {"car_id": 8, "make": "Chevrolet", "model": "Cruze", "available_from": "2023-12-05", "available_to": "2023-12-25"},
    {"car_id": 9, "make": "Nissan", "model": "Altima", "available_from": "2023-12-15", "available_to": "2024-01-05"},
    {"car_id": 10, "make": "Nissan", "model": "Sentra", "available_from": "2023-12-10", "available_to": "2024-01-10"},
    {"car_id": 11, "make": "Hyundai", "model": "Elantra", "available_from": "2023-12-01", "available_to": "2023-12-20"},
    {"car_id": 12, "make": "Hyundai", "model": "Sonata", "available_from": "2023-12-10", "available_to": "2024-01-01"},
    {"car_id": 13, "make": "Kia", "model": "Optima", "available_from": "2023-12-15", "available_to": "2024-01-15"},
    {"car_id": 14, "make": "Kia", "model": "Forte", "available_from": "2023-12-10", "available_to": "2024-01-10"},
    {"car_id": 15, "make": "Mazda", "model": "Mazda3", "available_from": "2023-12-01", "available_to": "2023-12-20"},
    {"car_id": 16, "make": "Mazda", "model": "Mazda6", "available_from": "2023-12-10", "available_to": "2024-01-05"},
    {"car_id": 17, "make": "Volkswagen", "model": "Passat", "available_from": "2023-12-15", "available_to": "2024-01-10"},
    {"car_id": 18, "make": "Volkswagen", "model": "Jetta", "available_from": "2023-12-01", "available_to": "2023-12-25"},
    {"car_id": 19, "make": "Subaru", "model": "Impreza", "available_from": "2023-12-05", "available_to": "2023-12-30"},
    {"car_id": 20, "make": "Subaru", "model": "Legacy", "available_from": "2023-12-10", "available_to": "2024-01-15"},
]

# Convert string date to datetime for comparison
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")

# Check car availability based on the dates
def check_availability(make, model, start_date, return_date):
    try:
        start_date = string_to_date(start_date)
        return_date = string_to_date(return_date)
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter dates in YYYY-MM-DD format.")
        return None

    for car in car_data:
        if car['make'].lower() == make.lower() and car['model'].lower() == model.lower():
            available_from = string_to_date(car['available_from'])
            available_to = string_to_date(car['available_to'])

            if start_date >= available_from and return_date <= available_to:
                return car  # Return the car data if available
    return None

# Load existing reservations from file
def load_reservations():
    if os.path.exists(RESERVATION_FILE):
        with open(RESERVATION_FILE, "r") as file:
            return json.load(file)
    return {}

# Save reservations to file
def save_reservations(reservations):
    with open(RESERVATION_FILE, "w") as file:
        json.dump(reservations, file, indent=4)

# Function to handle reservation
def handle_reservation():
    # Get data from entries
    car_make = make_entry.get()
    car_model = model_entry.get()
    start_date = start_date_entry.get()
    return_date = return_date_entry.get()
    payment_option = payment_option_var.get()

    # Check if car make, model and dates are valid
    car = check_availability(car_make, car_model, start_date, return_date)
    if car is None:
        messagebox.showerror("Invalid Input", "Invalid car make/model or dates. Please try again.")
        return

    # Generate a new reservation ID
    reservation_id = str(len(reservations) + 1)

    # Create a reservation entry
    reservation = {
        "Car Make": car_make,
        "Car Model": car_model,
        "Start Date": start_date,
        "Return Date": return_date,
        "Payment Option": payment_option
    }

    # Save reservation to the dictionary
    reservations[reservation_id] = reservation

    # Save to file
    save_reservations(reservations)

    # Show confirmation popup with reservation details
    confirmation_message = f"Reservation Confirmed!\nID: {reservation_id}\n\n"
    confirmation_message += "\n".join(f"{key}: {value}" for key, value in reservation.items())
    messagebox.showinfo("Reservation Confirmation", confirmation_message)

# Function to lookup reservation by ID
def lookup_reservation():
    reservation_id = reservation_lookup_entry.get()

    if reservation_id in reservations:
        reservation = reservations[reservation_id]
        result = f"ID: {reservation_id}\n" + "\n".join(f"{key}: {value}" for key, value in reservation.items())
    else:
        result = "Reservation ID not found."

    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Car Rental System")
root.geometry("400x500")

# Load existing reservations from the file
reservations = load_reservations()

# Car Make input
tk.Label(root, text="Car Make:").grid(row=0, column=0, pady=5, padx=10, sticky="w")
make_entry = tk.Entry(root)
make_entry.grid(row=0, column=1, pady=5, padx=10, sticky="w")

# Car Model input
tk.Label(root, text="Car Model:").grid(row=1, column=0, pady=5, padx=10, sticky="w")
model_entry = tk.Entry(root)
model_entry.grid(row=1, column=1, pady=5, padx=10, sticky="w")

# Start Date input
tk.Label(root, text="Start Date (YYYY-MM-DD):").grid(row=2, column=0, pady=5, padx=10, sticky="w")
start_date_entry = tk.Entry(root)
start_date_entry.grid(row=2, column=1, pady=5, padx=10, sticky="w")

# Return Date input
tk.Label(root, text="Return Date (YYYY-MM-DD):").grid(row=3, column=0, pady=5, padx=10, sticky="w")
return_date_entry = tk.Entry(root)
return_date_entry.grid(row=3, column=1, pady=5, padx=10, sticky="w")

# Payment Option
tk.Label(root, text="Payment Option:").grid(row=4, column=0, pady=5, padx=10, sticky="w")
payment_option_var = tk.StringVar(value="")
tk.Radiobutton(root, text="Pay Now", variable=payment_option_var, value="Paid").grid(row=4, column=1, pady=5, padx=10, sticky="w")
tk.Radiobutton(root, text="Pay Later", variable=payment_option_var, value="Not Paid").grid(row=5, column=1, pady=5, padx=10, sticky="w")

# Reservation Button
reserve_button = tk.Button(root, text="Make Reservation", command=handle_reservation)
reserve_button.grid(row=6, column=0, columnspan=2, pady=10)

# Reservation ID lookup section
tk.Label(root, text="Reservation ID Lookup:").grid(row=7, column=0, pady=5, padx=10, sticky="w")
reservation_lookup_entry = tk.Entry(root)
reservation_lookup_entry.grid(row=8, column=1, pady=5, padx=10, sticky="w")
lookup_button = tk.Button(root, text="Lookup Reservation", command=lookup_reservation)
lookup_button.grid(row=9, column=0, columnspan=2, pady=10)

# Result display label
result_label = tk.Label(root, text="")
result_label.grid(row=10, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
