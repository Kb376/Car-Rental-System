class Car:
    def __init__(self, car_id, model, year, rental_status="Available"):
        self.car_id = car_id
        self.model = model
        self.year = year
        self.rental_status = rental_status

    def check_availability(self):
        """
        Check if the car is available for rental.
        """
        return f"Car ID: {self.car_id}, Model: {self.model}, Year: {self.year}, Status: {self.rental_status}"

    def update_status(self, new_status):
        """
        Update the rental status of the car.
        """
        self.rental_status = new_status
        return f"Car ID {self.car_id} status updated to {self.rental_status}."

# Example usage:
car1 = Car("CAR001", "Toyota Camry", 2020)
car2 = Car("CAR002", "Honda Accord", 2021, rental_status="Rented")

# Check availability of cars
print(car1.check_availability())
print(car2.check_availability())

# Update car status
print(car1.update_status("Rented"))
print(car1.check_availability())
