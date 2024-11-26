import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import car_data  # Assuming car_data is imported as a list of dictionaries

# Reservation dictionary to store reservations
reservations = {}

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

    for car in car_data.car_data:
        if car['make'].lower() == make.lower() and car['model'].lower() == model.lower():
            available_from = string_to_date(car['available_from'])
            available_to = string_to_date(car['available_to'])

            if start_date >= available_from and return_date <= available_to:
                return car
    return None

# Main Reservation GUI
def reservation_gui():
    def make_reservation():
        make = make_entry.get().strip()
        model = model_entry.get().strip()
        start_date = start_date_entry.get().strip()
        return_date = return_date_entry.get().strip()

        if not make or not model or not start_date or not return_date:
            messagebox.showerror("Error", "All fields are required.")
            return

        car = check_availability(make, model, start_date, return_date)
        if car is None:
            messagebox.showerror("Unavailable", "Car is unavailable for the selected dates.")
            return

        # Create reservation ID
        reservation_id = str(len(reservations) + 1)

        # Save reservation
        reservations[reservation_id] = {
            "Car Make": make,
            "Car Model": model,
            "Start Date": start_date,
            "Return Date": return_date,
            "Picked Up": False,
            "Payment Status": "Not Paid",
        }

        # Confirmation
        confirmation_message = f"Reservation Confirmed!\n\nReservation ID: {reservation_id}\n"
        confirmation_message += "\n".join(f"{key}: {value}" for key, value in reservations[reservation_id].items())
        messagebox.showinfo("Reservation Confirmation", confirmation_message)

    def lookup_reservation():
        reservation_id = reservation_lookup_entry.get().strip()
        if not reservation_id:
            messagebox.showerror("Error", "Reservation ID is required.")
            return

        reservation = reservations.get(reservation_id)
        if reservation:
            result_label.config(
                text=f"Reservation Found:\nID: {reservation_id}\n" +
                     "\n".join(f"{key}: {value}" for key, value in reservation.items())
            )
        else:
            result_label.config(text="Reservation ID not found.")

    def pick_up_rental():
        reservation_id = pickup_reservation_entry.get().strip()
        if not reservation_id:
            messagebox.showerror("Error", "Reservation ID is required.")
            return

        reservation = reservations.get(reservation_id)
        if reservation:
            if reservation["Picked Up"]:
                messagebox.showinfo("Info", "Car has already been picked up.")
                return

            # Mark the car as picked up and update payment status
            reservation["Picked Up"] = True
            reservation["Payment Status"] = "Paid"
            result_label.config(
                text=f"Car Picked Up Successfully!\nID: {reservation_id}\n" +
                     "\n".join(f"{key}: {value}" for key, value in reservation.items())
            )
        else:
            messagebox.showerror("Error", "Reservation ID not found.")

    # Main window
    root = tk.Tk()
    root.title("Car Rental Reservation")
    root.geometry("600x600")

    # Widgets for reservation input
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

    # Reservation button
    reserve_button = tk.Button(root, text="Make Reservation", command=make_reservation)
    reserve_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Widgets for reservation lookup
    tk.Label(root, text="Lookup Reservation ID:").grid(row=5, column=0, pady=5, padx=10, sticky="w")
    reservation_lookup_entry = tk.Entry(root)
    reservation_lookup_entry.grid(row=5, column=1, pady=5, padx=10)

    lookup_button = tk.Button(root, text="Lookup Reservation", command=lookup_reservation)
    lookup_button.grid(row=6, column=0, columnspan=2, pady=10)

    # Widgets for picking up rental
    tk.Label(root, text="Pick Up Reservation ID:").grid(row=7, column=0, pady=5, padx=10, sticky="w")
    pickup_reservation_entry = tk.Entry(root)
    pickup_reservation_entry.grid(row=7, column=1, pady=5, padx=10)

    pickup_button = tk.Button(root, text="Pick Up Rental", command=pick_up_rental)
    pickup_button.grid(row=8, column=0, columnspan=2, pady=10)

    # Result display
    result_label = tk.Label(root, text="", wraplength=500, justify="left")
    result_label.grid(row=9, column=0, columnspan=2, pady=10)

    root.mainloop()


# Run the GUI
if __name__ == "__main__":
    reservation_gui()
