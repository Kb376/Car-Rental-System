import tkinter as tk
from tkinter import messagebox

class ReturnCarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Return Car")

        self.return_label = tk.Label(self.root, text="Enter Rental ID to Return Car")
        self.return_label.pack(pady=10)

        self.rental_id_entry = tk.Entry(self.root)
        self.rental_id_entry.pack(pady=10)

        self.return_button = tk.Button(self.root, text="Return Car", command=self.return_car)
        self.return_button.pack(pady=10)

    def return_car(self):
        rental_id = self.rental_id_entry.get()
        if rental_id:
            car_info = self.get_car_info(rental_id)
            bill_info = self.get_bill_info(rental_id)

            if car_info and bill_info:
                messagebox.showinfo("Return Car", f"Car Information:\n{car_info}\n\nBill Information:\n{bill_info}")
            else:
                messagebox.showerror("Return Car", "Invalid Rental ID. Please check and try again.")
        else:
            messagebox.showerror("Return Car", "Please enter a Rental ID.")

    def get_car_info(self, rental_id):
        with open('cars.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == rental_id:
                    return f"Car ID: {data[1]}\nModel: {data[2]}\nYear: {data[3]}\nColor: {data[4]}"
        return None

    def get_bill_info(self, rental_id):
        with open('bills.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == rental_id:
                    return f"Rental ID: {data[0]}\nTotal Amount: ${data[1]}\nDue Date: {data[2]}"
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ReturnCarApp(root)
    root.mainloop()
