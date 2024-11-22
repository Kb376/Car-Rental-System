class Reservation:
    def __init__(self, reservation_id, car_id, client_id, date, time, status, number_of_guests):
        self.reservation_id = reservation_id
        self.car_id = car_id
        self.client_id = client_id
        self.date = date
        self.time = time
        self.status = status
        self.number_of_guests = number_of_guests

    def reservation_details(self):
        return (f"Reservation ID: {self.reservation_id}, Car ID: {self.car_id}, Client ID: {self.client_id}, "
                f"Date: {self.date}, Time: {self.time}, Status: {self.status}, Guests: {self.number_of_guests}")

    def modify_reservation(self, car_id=None, date=None, time=None, status=None, number_of_guests=None):
        if car_id:
            self.car_id = car_id
        if date:
            self.date = date
        if time:
            self.time = time
        if status:
            self.status = status
        if number_of_guests:
            self.number_of_guests = number_of_guests
        return "Reservation updated."

    def cancel_reservation(self):
        self.status = "Cancelled"
        return "Reservation cancelled."

# Example usage:
reservation = Reservation(101, 202, 303, '2024-11-25', 1400, "Confirmed", 4)

# Display details
print(reservation.reservation_details())

# Modify reservation
print(reservation.modify_reservation(date=20241125, time=1500))

# Cancel reservation
print(reservation.cancel_reservation())