import tkinter as tk
from tkinter import messagebox

#function to get receipt information
def print_receipt():
    name=name_entered.get()
    item_name=item_entered.get()
    quantity=int(quantity_entered.get())
    price =float(price_entered.get())

    total_price=quantity*price

    receipt = f"Name: {name}\n"
    receipt += f"Item: {item_name}\n"
    receipt += f"Quantity: {quantity}\n"
    receipt += f"Price: {price}\n"
    receipt +=f"Total Price: {total_price}\n"

    #printing receipt
    print(receipt)
    messagebox.showinfo("Receipt has been printed successfully")

#creating main window
window =tk.Tk()
window.title("mariam_nabukenya_receipt_printer")
window.geometry("400x250")

#creating labels
name_label =tk.Label(window,text="Name:",anchor="w")
name_label.pack(fill="x",padx=10,pady=5)

item_label = tk.Label(window,text="Item:",anchor="w")
item_label.pack(fill="x",padx=10,pady=5)

quantity_label = tk.Label(window,text="Quantity:",anchor="w")
quantity_label.pack(fill="x",padx=10,pady=5)

price_label =tk.Label(window,text="Price:",anchor="w")
price_label.pack(fill="x",padx=10,pady=5)

#creating entry feilds
name_entered=tk.Entry(window)
name_entered.pack(fill="x",padx=10)

item_entered=tk.Entry(window)
item_entered.pack(fill="x",padx=10)

quantity_entered=tk.Entry(window)
quantity_entered.pack(fill="x",padx=10)

price_entered=tk.Entry(window)
price_entered.pack(fill="x",padx=10)

#creating print button
print_button=tk.Button(window,text="Print Receipt",command=print_receipt)
print_button.pack()

window.mainloop()