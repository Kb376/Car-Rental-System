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

# Convert string date to datetime
def string_to_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

# Check car availability based on make, model, and date range
def check_availability(make, model, start_date, return_date):
    try:
        start_date = string_to_date(start_date)
        return_date = string_to_date(return_date)
    except ValueError as e:
        messagebox.showerror("Invalid Date", str(e))
        return None

    for car in car_data:
        if car['make'].lower() == make.lower() and car['model'].lower() == model.lower():
            available_from = string_to_date(car['available_from'])
            available_to = string_to_date(car['available_to'])

            if start_date >= available_from and return_date <= available_to:
                return car
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

# Handle new reservation
def handle_reservation(make, model, start_date, return_date, payment_option, reservations, result_label):
    car = check_availability(make, model, start_date, return_date)
    if car is None:
        messagebox.showerror("Unavailable", "Car is unavailable for the selected dates.")
        return

    # Create reservation ID
    reservation_id = str(len(reservations) + 1)

    # Add reservation details
    reservation = {
        "Car Make": make,
        "Car Model": model,
        "Start Date": start_date,
        "Return Date": return_date,
        "Payment Option": payment_option
    }
    reservations[reservation_id] = reservation
    save_reservations(reservations)

    # Confirmation
    confirmation_message = f"Reservation Confirmed!\n\nID: {reservation_id}\n"
    confirmation_message += "\n".join(f"{key}: {value}" for key, value in reservation.items())
    messagebox.showinfo("Reservation Confirmation", confirmation_message)

    # Update result label
    result_label.config(text=confirmation_message)

# Lookup a reservation by ID
def lookup_reservation(reservation_id, reservations, result_label):
    if reservation_id in reservations:
        reservation = reservations[reservation_id]
        result = f"Reservation Found:\nID: {reservation_id}\n" + "\n".join(f"{key}: {value}" for key, value in reservation.items())
    else:
        result = "Reservation ID not found."
    result_label.config(text=result)

# Main Reservation GUI
def reservation_gui():
    # Main window
    root = tk.Tk()
    root.title("Car Rental System")
    root.geometry("400x500")

    # Load reservations
    reservations = load_reservations()

    # Widgets for car reservation
    tk.Label(root, text="Car Make:").grid(row=0, column=0, pady=5, padx=10, sticky="w")
    make_entry = tk.Entry(root)
    make_entry.grid(row=0, column=1, pady=5, padx=10)

    tk.Label(root, text="Car Model:").grid(row=1, column=0, pady=5, padx=10, sticky="w")
    model_entry = tk.Entry(root)
    model_entry.grid(row=1, column=1, pady=5, padx=10)

    tk.Label(root, text="Start Date (YYYY-MM-DD):").grid(row=2, column=0, pady=5, padx=10, sticky="w")
    start_date_entry = tk.Entry(root)
    start_date_entry.grid(row=2, column=1, pady=5, padx=10)

    tk.Label(root, text="Return Date (YYYY-MM-DD):").grid(row=3, column=0, pady=5, padx=10, sticky="w")
    return_date_entry = tk.Entry(root)
    return_date_entry.grid(row=3, column=1, pady=5, padx=10)

    tk.Label(root, text="Payment Option:").grid(row=4, column=0, pady=5, padx=10, sticky="w")
    payment_option_var = tk.StringVar(value="Not Paid")
    tk.Radiobutton(root, text="Pay Now", variable=payment_option_var, value="Paid").grid(row=4, column=1, sticky="w")
    tk.Radiobutton(root, text="Pay Later", variable=payment_option_var, value="Not Paid").grid(row=5, column=1, sticky="w")

    # Result label for showing feedback
    result_label = tk.Label(root, text="", wraplength=300, justify="left")
    result_label.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

    # Reservation button
    reserve_button = tk.Button(root, text="Make Reservation", command=lambda: handle_reservation(
        make_entry.get(), model_entry.get(), start_date_entry.get(), return_date_entry.get(),
        payment_option_var.get(), reservations, result_label
    ))
    reserve_button.grid(row=6, column=0, columnspan=2, pady=10)

    # Widgets for reservation lookup
    tk.Label(root, text="Lookup Reservation ID:").grid(row=8, column=0, pady=5, padx=10, sticky="w")
    reservation_lookup_entry = tk.Entry(root)
    reservation_lookup_entry.grid(row=8, column=1, pady=5, padx=10)

    lookup_button = tk.Button(root, text="Lookup Reservation", command=lambda: lookup_reservation(
        reservation_lookup_entry.get(), reservations, result_label
    ))
    lookup_button.grid(row=9, column=0, columnspan=2, pady=10)

    # Run the GUI
    root.mainloop()
