class Invoice:
    def __init__(self, invoice_id, client_id, amount_due, status):
        self.invoice_id = invoice_id
        self.client_id = client_id
        self.amount_due = amount_due
        self.status = status

    def generate_invoice(self):
        return (f"Invoice ID: {self.invoice_id}\n"
                f"Client ID: {self.client_id}\n"
                f"Amount Due: ${self.amount_due:.2f}\n"
                f"Status: {self.status}")

    def send_invoice(self):
        return f"Invoice {self.invoice_id} has been sent to client {self.client_id}."

    def settle_invoice(self):
        if self.status.lower() != "paid":
            self.status = "Paid"
            self.amount_due = 0.0
            return f"Invoice {self.invoice_id} has been settled. Status updated to 'Paid'."
        else:
            return f"Invoice {self.invoice_id} is already settled."

# Example usage:
invoice = Invoice("INV123", 101, 250.75, "Pending")

# Generate and display the invoice
print(invoice.generate_invoice())

# Send the invoice
print(invoice.send_invoice())

# Settle the invoice
print(invoice.settle_invoice())

# Attempt to settle again
print(invoice.settle_invoice())
