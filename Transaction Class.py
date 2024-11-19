class Transaction:
    def __init__(self, transaction_id, invoice_id, payment_status, transaction_date):
        self.transaction_id = transaction_id
        self.invoice_id = invoice_id
        self.payment_status = payment_status
        self.transaction_date = transaction_date  # Use string like "2024-11-19"

    def process_transaction(self, amount_paid):
        if self.payment_status.lower() != "completed":
            self.payment_status = "Completed"
            return (f"Transaction {self.transaction_id} for Invoice {self.invoice_id} "
                    f"has been processed on {self.transaction_date}. Amount Paid: ${amount_paid:.2f}")
        else:
            return f"Transaction {self.transaction_id} has already been completed."

# Example usage:
transaction = Transaction("T001", "INV123", "Pending", "2024-11-19")

# Process the transaction
print(transaction.process_transaction(250.75))

# Attempt to process it again
print(transaction.process_transaction(250.75))