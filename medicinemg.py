import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class MedicineStock:
    def __init__(self, root):
        self.root = root
        self.root.title("Medicine Stock Management System")
        self.root.geometry("1200x700+0+0")
        self.root.configure(background="#f0f0f0")

        # Database connection
        self.conn = sqlite3.connect("medicine_stock.db")
        self.cursor = self.conn.cursor()

        # Create table if it doesn't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS medicine (
                medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
                medicine_name TEXT NOT NULL,
                manufacturer TEXT,
                quantity INTEGER,
                expiry_date DATE,
                price REAL
            )
        """)

        # Title
        title = tk.Label(self.root, text="Medicine Stock Management System", font=("times new roman", 24, "bold"), bd=5, relief=tk.GROOVE, bg="#b7d8d6", fg="black")
        title.pack(side=tk.TOP, fill=tk.X)

        # Frames
        Manage_Frame = tk.Frame(self.root, width=1000, height=400, bd=5, relief=tk.RIDGE, bg="#789e9e")
        Manage_Frame.place(x=10, y=70)

        Buttons_Frame = tk.Frame(self.root, width=1000, height=55, bd=4, relief=tk.RIDGE, bg="#eef3db")
        Buttons_Frame.place(x=10, y=460)

        Data_Frame = tk.Frame(self.root, width=1000, height=270, bd=4, relief=tk.RIDGE, bg="#eef3db")
        Data_Frame.place(x=10, y=510)

        # Variables
        self.medicine_id = tk.StringVar()
        self.medicine_name = tk.StringVar()
        self.manufacturer = tk.StringVar()
        self.quantity = tk.StringVar()
        self.expiry_date = tk.StringVar()
        self.price = tk.StringVar()

        # Medicine Details
        MedFrame = tk.LabelFrame(Manage_Frame, text="Medicine Details", font=("times new roman", 16, "bold"), bd=5, relief=tk.RIDGE, bg="#eef3db", fg="black")
        MedFrame.place(x=5, y=5)

        # Medicine ID (Read-Only)
        lbl_MedID = tk.Label(MedFrame, text="Medicine ID:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_MedID.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        txt_MedID = tk.Entry(MedFrame, font=("times new roman", 12, "bold"), textvariable=self.medicine_id, state="readonly")
        txt_MedID.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Medicine Name
        lbl_MedName = tk.Label(MedFrame, text="Medicine Name:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_MedName.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        txt_MedName = tk.Entry(MedFrame, font=("times new roman", 12, "bold"), textvariable=self.medicine_name)
        txt_MedName.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Manufacturer
        lbl_Manufacturer = tk.Label(MedFrame, text="Manufacturer:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_Manufacturer.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        txt_Manufacturer = tk.Entry(MedFrame, font=("times new roman", 12, "bold"), textvariable=self.manufacturer)
        txt_Manufacturer.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        # Quantity
        lbl_Quantity = tk.Label(MedFrame, text="Quantity:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_Quantity.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        txt_Quantity = tk.Entry(MedFrame, font=("times new roman", 12, "bold"), textvariable=self.quantity)
        txt_Quantity.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        # Expiry Date
        lbl_ExpiryDate = tk.Label(MedFrame, text="Expiry Date (YYYY-MM-DD):", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_ExpiryDate.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        txt_ExpiryDate = tk.Entry(MedFrame, font=("times new roman", 12, "bold"), textvariable=self.expiry_date)
        txt_ExpiryDate.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

        # Price
        lbl_Price = tk.Label(MedFrame, text="Price:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_Price.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        txt_Price = tk.Entry(MedFrame, font=("times new roman", 12, "bold"), textvariable=self.price)
        txt_Price.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

        # Buttons Frame
        AddButton = tk.Button(Buttons_Frame, text="Add", font=("times new roman", 12, "bold"), bd=5, relief=tk.GROOVE, bg="white", fg="black", command=self.add_medicine)
        AddButton.grid(row=0, column=0, padx=10, pady=10)

        DisplayButton = tk.Button(Buttons_Frame, text="Display", font=("times new roman", 12, "bold"), bd=5, relief=tk.GROOVE, bg="white", fg="black", command=self.display_data)
        DisplayButton.grid(row=0, column=1, padx=10, pady=10)

        ClearButton = tk.Button(Buttons_Frame, text="Clear", font=("times new roman", 12, "bold"), bd=5, relief=tk.GROOVE, bg="white", fg="black", command=self.clear_data)
        ClearButton.grid(row=0, column=2, padx=10, pady=10)

        DeleteButton = tk.Button(Buttons_Frame, text="Delete", font=("times new roman", 12, "bold"), bd=5, relief=tk.GROOVE, bg="white", fg="black", command=self.delete_medicine)
        DeleteButton.grid(row=0, column=3, padx=10, pady=10)

        ExitButton = tk.Button(Buttons_Frame, text="Exit", font=("times new roman", 12, "bold"), bd=5, relief=tk.GROOVE, bg="white", fg="black", command=self.exit_app)
        ExitButton.grid(row=0, column=4, padx=10, pady=10)

        # Treeview for displaying data
        self.medicine_table = ttk.Treeview(Data_Frame, columns=("medid", "medname", "manufacturer", "quantity", "expiry_date", "price"))

        self.medicine_table.heading("medid", text="Medicine ID")
        self.medicine_table.heading("medname", text="Medicine Name")
        self.medicine_table.heading("manufacturer", text="Manufacturer")
        self.medicine_table.heading("quantity", text="Quantity")
        self.medicine_table.heading("expiry_date", text="Expiry Date")
        self.medicine_table.heading("price", text="Price")
        
        self.medicine_table['show'] = 'headings'

        self.medicine_table.column("medid", width=100)
        self.medicine_table.column("medname", width=150)
        self.medicine_table.column("manufacturer", width=150)
        self.medicine_table.column("quantity", width=100)
        self.medicine_table.column("expiry_date", width=100)
        self.medicine_table.column("price", width=100)

        self.medicine_table.pack(fill=tk.BOTH, expand=1)

    def add_medicine(self):
        # Function to add a new medicine to the database
        if self.medicine_name.get() == "" or self.manufacturer.get() == "" or self.quantity.get() == "" or self.expiry_date.get() == "" or self.price.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                # Convert quantity to integer and price to float
                quantity = int(self.quantity.get())
                price = float(self.price.get())

                # Insert data into the database
                self.cursor.execute("""
                    INSERT INTO medicine (medicine_name, manufacturer, quantity, expiry_date, price)
                    VALUES (?, ?, ?, ?, ?)
                """, (self.medicine_name.get(), self.manufacturer.get(), quantity, self.expiry_date.get(), price))
                self.conn.commit()

                messagebox.showinfo("Success", "Medicine added successfully")
                self.display_data()  # Refresh the table view
                self.clear_data()
            except ValueError:
                messagebox.showerror("Error", "Quantity must be an integer and Price must be a number")

    def display_data(self):
        # Function to display all medicines from the database
        for row in self.medicine_table.get_children():
            self.medicine_table.delete(row)

        self.cursor.execute("SELECT * FROM medicine")
        rows = self.cursor.fetchall()
        for row in rows:
            self.medicine_table.insert("", tk.END, values=row)

    def clear_data(self):
        # Function to clear all input fields
        self.medicine_id.set("")
        self.medicine_name.set("")
        self.manufacturer.set("")
        self.quantity.set("")
        self.expiry_date.set("")
        self.price.set("")

    def delete_medicine(self):
        # Function to delete a medicine from the database
        selected_item = self.medicine_table.selection()
        if selected_item:
            try:
                # Get the medicine ID from the selected row
                med_id = self.medicine_table.item(selected_item[0])['values'][0]
                self.cursor.execute("DELETE FROM medicine WHERE medicine_id = ?", (med_id,))
                self.conn.commit()
                self.medicine_table.delete(selected_item)
                messagebox.showinfo("Delete", "Medicine deleted successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting medicine: {e}")
        else:
            messagebox.showerror("Error", "Please select a medicine to delete")

    def exit_app(self):
        # Function to close the application
        self.conn.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicineStock(root)
    root.mainloop()