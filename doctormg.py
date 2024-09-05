import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Doctor:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")

        # Variables
        self.Date_of_Registration = StringVar()
        self.Date_of_Registration.set(time.strftime("%d/%m/%y"))
        self.DrId = StringVar()
        self.Drname = StringVar()
        self.DateofBirth = StringVar()
        self.Spes = StringVar()
        self.GovtPri = StringVar()
        self.Surgeries = StringVar()
        self.Experiences = StringVar()
        self.Nurses = StringVar()
        self.DrMobile = StringVar()
        self.PtName = StringVar()
        self.Apptime = StringVar()
        self.PtAge = StringVar()
        self.PatientAddress = StringVar()
        self.PtMobile = StringVar()
        self.Disease = StringVar()
        self.Case = StringVar()
        self.BenefitCard = StringVar()

        # Title
        title = Label(self.root, text="Doctor Management System", font=("monotype corsiva", 42, "bold"), bd=5, relief=GROOVE, bg="#b7d8d6", fg="black")
        title.pack(side=TOP, fill=X)

        # Frames
        Manage_Frame = Frame(self.root, width=1510, height=400, bd=5, relief=RIDGE, bg="#789e9e")
        Manage_Frame.place(x=10, y=80)

        Buttons_Frame = Frame(self.root, width=1510, height=55, bd=4, relief=RIDGE, bg="#eef3db")
        Buttons_Frame.place(x=10, y=460)

        Data_Frame = Frame(self.root, width=1510, height=270, bd=4, relief=RIDGE, bg="#eef3db")
        Data_Frame.place(x=10, y=510)

        # Doctor's Details
        DFrame = LabelFrame(Manage_Frame, text="Doctor's Details", font=("times new roman", 16, "bold"), bd=5, relief=RIDGE, bg="#eef3db", fg="black")
        DFrame.place(x=5, y=5)

        # Doctor ID
        lbl_DrID = Label(DFrame, text="Doctor ID:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_DrID.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        txt_DrID = Entry(DFrame, font=("times new roman", 12, "bold"), textvariable=self.DrId)
        txt_DrID.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Doctor Name
        lbl_DrName = Label(DFrame, text="Doctor Name:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_DrName.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        txt_DrName = Entry(DFrame, font=("times new roman", 12, "bold"), textvariable=self.Drname)
        txt_DrName.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Date of Birth
        lbl_DoB = Label(DFrame, text="Date of Birth:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_DoB.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        txt_DoB = Entry(DFrame, font=("times new roman", 12, "bold"), textvariable=self.DateofBirth)
        txt_DoB.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Specialisation
        lbl_Spes = Label(DFrame, text="Specialisation:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_Spes.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        txt_Spes = Entry(DFrame, font=("times new roman", 12, "bold"), textvariable=self.Spes)
        txt_Spes.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Govt/Private
        lbl_GovPri = Label(DFrame, text="Govt/Private:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_GovPri.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        txt_GovPri = Entry(DFrame, font=("times new roman", 12, "bold"), textvariable=self.GovtPri)
        txt_GovPri.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Total Surgeries
        lbl_Surgeries = Label(DFrame, text="Total Surgeries:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_Surgeries.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        txt_Surgeries = Entry(DFrame, font=("times new roman", 12, "bold"), textvariable=self.Surgeries)
        txt_Surgeries.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # Experience in years
        lbl_Experiences = Label(DFrame, text="Experience in years:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_Experiences.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        txt_Experiences = Entry(DFrame, font=("times new roman", 12, "bold"), textvariable=self.Experiences)
        txt_Experiences.grid(row=6, column=1, padx=10, pady=5, sticky=W)

        # Nurses under Dr
        lbl_Nurses = Label(DFrame, text="Nurses under Dr:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_Nurses.grid(row=7, column=0, padx=10, pady=5, sticky=W)
        txt_Nurses = Entry(DFrame, font=("times new roman", 12, "bold"), textvariable=self.Nurses)
        txt_Nurses.grid(row=7, column=1, padx=10, pady=5, sticky=W)

        # Doctor Mobile No
        lbl_DrMobile = Label(DFrame, text="Doctor Mobile No:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_DrMobile.grid(row=8, column=0, padx=10, pady=5, sticky=W)
        txt_DrMobile = Entry(DFrame, font=("times new roman", 12, "bold"), textvariable=self.DrMobile)
        txt_DrMobile.grid(row=8, column=1, padx=10, pady=5, sticky=W)

        # Patient's Details
        PFrame = LabelFrame(Manage_Frame, text="Patient's Information", font=("times new roman", 16, "bold"), bd=5, relief=RIDGE, bg="#eef3db", fg="black")
        PFrame.place(x=550, y=5)

        # Patient Name
        lbl_PtName = Label(PFrame, text="Patient Name:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_PtName.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        txt_PtName = Entry(PFrame, font=("times new roman", 12, "bold"), textvariable=self.PtName)
        txt_PtName.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Appointment Time
        lbl_Apptime = Label(PFrame, text="Appointment Time:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_Apptime.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        txt_Apptime = Entry(PFrame, font=("times new roman", 12, "bold"), textvariable=self.Apptime)
        txt_Apptime.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Patient Age
        lbl_PtAge = Label(PFrame, text="Patient Age:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_PtAge.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        txt_PtAge = Entry(PFrame, font=("times new roman", 12, "bold"), textvariable=self.PtAge)
        txt_PtAge.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Patient Address
        lbl_PatientAddress = Label(PFrame, text="Patient Address:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_PatientAddress.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        txt_PatientAddress = Entry(PFrame, font=("times new roman", 12, "bold"), textvariable=self.PatientAddress)
        txt_PatientAddress.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Patient Mobile No
        lbl_PtMobile = Label(PFrame, text="Patient Mobile No:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_PtMobile.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        txt_PtMobile = Entry(PFrame, font=("times new roman", 12, "bold"), textvariable=self.PtMobile)
        txt_PtMobile.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Disease
        lbl_Disease = Label(PFrame, text="Disease:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_Disease.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        txt_Disease = Entry(PFrame, font=("times new roman", 12, "bold"), textvariable=self.Disease)
        txt_Disease.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # Case Type
        lbl_Case = Label(PFrame, text="Case Type:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_Case.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        txt_Case = Entry(PFrame, font=("times new roman", 12, "bold"), textvariable=self.Case)
        txt_Case.grid(row=6, column=1, padx=10, pady=5, sticky=W)

        # Benefit Card ID
        lbl_BenefitCard = Label(PFrame, text="Benefit Card ID:", font=("times new roman", 12, "bold"), bg="white", fg="black")
        lbl_BenefitCard.grid(row=7, column=0, padx=10, pady=5, sticky=W)
        txt_BenefitCard = Entry(PFrame, font=("times new roman", 12, "bold"), textvariable=self.BenefitCard)
        txt_BenefitCard.grid(row=7, column=1, padx=10, pady=5, sticky=W)

        # Buttons Frame
        AddButton = Button(Buttons_Frame, text="Add", font=("times new roman", 12, "bold"), bd=5, relief=GROOVE, bg="white", fg="black", command=self.add_doctor)
        AddButton.grid(row=0, column=0, padx=10, pady=10)

        DisplayButton = Button(Buttons_Frame, text="Display", font=("times new roman", 12, "bold"), bd=5, relief=GROOVE, bg="white", fg="black", command=self.Display_data)
        DisplayButton.grid(row=0, column=1, padx=10, pady=10)

        ClearButton = Button(Buttons_Frame, text="Clear", font=("times new roman", 12, "bold"), bd=5, relief=GROOVE, bg="white", fg="black", command=self.Clear_data)
        ClearButton.grid(row=0, column=2, padx=10, pady=10)

        DeleteButton = Button(Buttons_Frame, text="Delete", font=("times new roman", 12, "bold"), bd=5, relief=GROOVE, bg="white", fg="black", command=self.delete_data)
        DeleteButton.grid(row=0, column=3, padx=10, pady=10)

        ExitButton = Button(Buttons_Frame, text="Exit", font=("times new roman", 12, "bold"), bd=5, relief=GROOVE, bg="white", fg="black", command=self.exit_app)
        ExitButton.grid(row=0, column=4, padx=10, pady=10)

        # Treeview for displaying data
        self.hospital_table = ttk.Treeview(Data_Frame, columns=("drid", "drname", "dob", "specialisation", "govtpri", "surgeries", "experience", "nurses", "drmobile", "ptname", "apptime", "ptage", "patientaddress", "ptmobile", "disease", "case", "benefitcard"))

        self.hospital_table.heading("drid", text="Doctor ID")
        self.hospital_table.heading("drname", text="Doctor Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("specialisation", text="Specialisation")
        self.hospital_table.heading("govtpri", text="Govt/Private")
        self.hospital_table.heading("surgeries", text="Total Surgeries")
        self.hospital_table.heading("experience", text="Experience (years)")
        self.hospital_table.heading("nurses", text="Nurses under Dr")
        self.hospital_table.heading("drmobile", text="Doctor Mobile")
        self.hospital_table.heading("ptname", text="Patient Name")
        self.hospital_table.heading("apptime", text="Appointment Time")
        self.hospital_table.heading("ptage", text="Patient Age")
        self.hospital_table.heading("patientaddress", text="Patient Address")
        self.hospital_table.heading("ptmobile", text="Patient Mobile")
        self.hospital_table.heading("disease", text="Disease")
        self.hospital_table.heading("case", text="Case Type")
        self.hospital_table.heading("benefitcard", text="Benefit Card ID")
        
        self.hospital_table['show'] = 'headings'

        self.hospital_table.column("drid", width=100)
        self.hospital_table.column("drname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("specialisation", width=100)
        self.hospital_table.column("govtpri", width=100)
        self.hospital_table.column("surgeries", width=100)
        self.hospital_table.column("experience", width=100)
        self.hospital_table.column("nurses", width=100)
        self.hospital_table.column("drmobile", width=100)
        self.hospital_table.column("ptname", width=100)
        self.hospital_table.column("apptime", width=100)
        self.hospital_table.column("ptage", width=100)
        self.hospital_table.column("patientaddress", width=150)
        self.hospital_table.column("ptmobile", width=100)
        self.hospital_table.column("disease", width=100)
        self.hospital_table.column("case", width=100)
        self.hospital_table.column("benefitcard", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)

    def add_doctor(self):
        # Functionality for adding doctor details
        if self.DrId.get() == "" or self.Drname.get() == "":
            tkinter.messagebox.showerror("Error", "All fields are required")
        else:
            self.hospital_table.insert("", "end", values=(self.DrId.get(), self.Drname.get(), self.DateofBirth.get(), self.Spes.get(), self.GovtPri.get(), self.Surgeries.get(), self.Experiences.get(), self.Nurses.get(), self.DrMobile.get(), self.PtName.get(), self.Apptime.get(), self.PtAge.get(), self.PatientAddress.get(), self.PtMobile.get(), self.Disease.get(), self.Case.get(), self.BenefitCard.get()))
            tkinter.messagebox.showinfo("Success", "Record has been inserted successfully")
            self.Clear_data()

    def Display_data(self):
        # Functionality for displaying doctor and patient details
        for row in self.hospital_table.get_children():
            self.hospital_table.delete(row)
        tkinter.messagebox.showinfo("Info", "Data has been displayed")

    def Clear_data(self):
        # Functionality for clearing the form data
        self.DrId.set("")
        self.Drname.set("")
        self.DateofBirth.set("")
        self.Spes.set("")
        self.GovtPri.set("")
        self.Surgeries.set("")
        self.Experiences.set("")
        self.Nurses.set("")
        self.DrMobile.set("")
        self.PtName.set("")
        self.Apptime.set("")
        self.PtAge.set("")
        self.PatientAddress.set("")
        self.PtMobile.set("")
        self.Disease.set("")
        self.Case.set("")
        self.BenefitCard.set("")

    def delete_data(self):
        # Functionality for deleting data
        selected_item = self.hospital_table.selection()
        if selected_item:
            self.hospital_table.delete(selected_item)
            tkinter.messagebox.showinfo("Delete", "Record has been deleted successfully")
        else:
            tkinter.messagebox.showerror("Error", "Please select a record to delete")

    def exit_app(self):
        # Functionality for exiting the application
        self.root.destroy()

# Initialize the GUI application
if __name__ == "__main__":
    root = Tk()
    app = Doctor(root)
    root.mainloop()
