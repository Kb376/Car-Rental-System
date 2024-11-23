class CarRentalSystem:
    def __init__(self, system_id, system_name, working_hours):
        self.system_id = system_id
        self.system_name = system_name
        self.working_hours = working_hours

    def login(self, user_id):
        return f"User {user_id} has logged in to {self.system_name}."

    def logout(self, user_id):
        return f"User {user_id} has logged out of {self.system_name}."

# Example usage:
car_rental_system = CarRentalSystem("CRS123", "Car Renting Shop", "9:00 AM - 5:00 PM")

# Display system details
print(f"System ID: {car_rental_system.system_id}")
print(f"System Name: {car_rental_system.system_name}")
print(f"Working Hours: {car_rental_system.working_hours}")

# User login
print(car_rental_system.login("U123"))

# User logout
print(car_rental_system.logout("U123"))
