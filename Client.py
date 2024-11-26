class Client:
    def __init__(self, client_id, name, contact_info, preferences, rental_history):
        """
        Initialize the Client object with basic details.
        """
        self.client_id = client_id
        self.name = name
        self.contact_info = contact_info
        self.preferences = preferences
        self.rental_history = rental_history

    def provide_personal_information(self):
        """
        Display the client's personal information.
        """
        return f"Client ID: {self.client_id}, Name: {self.name}, Contact Info: {self.contact_info}, Preferences: {self.preferences}, Rental History: {self.rental_history}"

    def review_reservation(self, reservation_id, reservation_details):
        """
        Review details of a reservation.
        """
        return f"Reservation ID: {reservation_id}, Details: {reservation_details}"

