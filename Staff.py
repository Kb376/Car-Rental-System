class Staff:
    def __init__(self, staff_id, name, role, contact_info):
        """
        Initialize the Staff object with attributes.
        :param staff_id: (int) Unique identifier for the staff.
        :param name: (str) Name of the staff member.
        :param role: (str) Role or position of the staff member.
        :param contact_info: (str) Contact information of the staff member.
        """
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.contact_info = contact_info

    def make_reservation(self, reservation_details):
        """
        Creates a new reservation.
        :param reservation_details: (dict) Details of the reservation to be made.
        :return: Confirmation or status of the reservation.
        """
        return f"Reservation made successfully: {reservation_details}"

    def update_reservation(self, reservation_id, updated_details):
        """
        Updates an existing reservation.
        :param reservation_id: (int) ID of the reservation to update.
        :param updated_details: (dict) Updated reservation details.
        :return: Confirmation or status of the update.
        """
        return f"Reservation {reservation_id} updated successfully with details: {updated_details}"

    def cancel_reservation(self, reservation_id):
        """
        Cancels an existing reservation.
        :param reservation_id: (int) ID of the reservation to cancel.
        :return: Confirmation or status of the cancellation.
        """
        return f"Reservation {reservation_id} cancelled successfully."

# Example usage:
staff_member = Staff(101, "John Doe", "Manager", "john.doe@example.com")
print(staff_member.make_reservation({"date": "2024-11-20", "time": "10:00 AM", "customer": "Jane Smith"}))
print(staff_member.update_reservation(1, {"time": "11:00 AM"}))
print(staff_member.cancel_reservation(1))
