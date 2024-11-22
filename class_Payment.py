class Payment:
    def __init__(self, payment_id, client_id, amount, method_of_payment):
        self.payment_id = payment_id
        self.client_id = client_id
        self.amount = amount
        self.method_of_payment = method_of_payment
        self.status = "Pending"  # Default status for payments

    def payment_processing(self):
        if self.status == "Pending":
            return (f"Processing payment of ${self.amount:.2f} for Client ID {self.client_id} "
                    f"using {self.method_of_payment}.")
        else:
            return f"Payment {self.payment_id} has already been processed."

    def confirm_payment(self):
        if self.status == "Pending":
            self.status = "Confirmed"
            return f"Payment {self.payment_id} has been confirmed."
        else:
            return f"Payment {self.payment_id} is already confirmed."

# Example usage:
payment = Payment(1001, 201, 150.50, "Credit Card")

# Process the payment
print(payment.payment_processing())

# Confirm the payment
print(payment.confirm_payment())

# Attempt to confirm again
print(payment.confirm_payment())