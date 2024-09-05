import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0")  # Corrected geometry format
        self.root.configure(background="black")  # Fixed 'comfigure' to 'configure'

        ####################VARIABLE DECLARATION################
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        cmbTabletNames = StringVar()
        HospitalCode = StringVar()
        Number_of_Tablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInformation = StringVar()
        StorageAdvice = StringVar()
        Medication = StringVar()
        PatientId = StringVar()
        PatientNumber = StringVar()
        PatientName = StringVar()
        DateOfBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        NHSNumber = StringVar()


        def Reference_numfunc():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def prescriptionfunc():
            Reference_numfunc()  # Likely a function call to generate a reference number

    # Inserting data into a text widget named TextPrescription
            TextPrescription.insert(END, "Patient ID: \t\t" + PatientId.get() + "\n")
            TextPrescription.insert(END, "Patient Name: \t\t" + Patientname.get() + "\n")
            TextPrescription.insert(END, "Tablet: \t\t" + cmbTabletNames.get() + "\n")
            TextPrescription.insert(END, "Number of tablet: \t\t" + Number_of_tablets.get() + "\n")
            TextPrescription.insert(END, "Daily Dose: \t\t" + DailyDose.get() + "\n")
            TextPrescription.insert(END, "Issued Date: \t\t" + IssuedDate.get() + "\n")
            TextPrescription.insert(END, "Expiry Date: \t\t" + ExpiryDate.get() + "\n")
            TextPrescription.insert(END, "Storage: \t\t" + StorageAdvice.get() + "\n")
            TextPrescription.insert(END, "More Information: \t\t" + MoreInformation.get() + "\n")

            return  # Returning from the function


            








      
        def prescriptiondatafunc():
            Reference_numfunc()  # Likely a function call to generate a reference number

    # Inserting data into a text widget named TextPrescriptionData
            TextPrescriptionData.insert(END, Date_of_Registration.get() + "\t" + Ref.get() + "\t\t" + PatientId.get() + "\t" +
            PatientName.get() + "\t" + DateOfBirth.get() + "\t\t" + NHSNumber.get() + "\t\t" +
            cmbTabletNames.get() + "\t" + Number_of_Tablets.get() + "\t\t" + IssuedDate.get() + "\t\t" +
            ExpiryDate.get() + "\t\t" + DailyDose.get() + "\t\t" + StorageAdvice.get() + "\t" + 
            PatientId.get() + "\n"
    )

            return  # Returning from the function




        def exitbtn():


        
            exitbtn = tkinter.messagebox.askyesno("Hospital Management system" ,"Are you sure you want to exit")
            if exitbtn > 0:
                root.destroy()
                return

        def deletefunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNumber.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSNumber.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return
            
        def resetfunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNumber.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSNumber.set("")
            TextPrescription.delete("1.0",END)




        # title
        title = Label(self.root, text="Hospital Management System", font=("monotype corsiva", 42, "bold"), bd=5, relief=GROOVE, bg="#2eb8b8", fg="black")
        title.pack(side=TOP, fill=X)

        # FRAMES
        Manage_Frame = Frame(self.root, width=1510, height=400, bd=5, relief=RIDGE, bg="#0099cc")
        Manage_Frame.place(x=10, y=80)

        Button_Frame = Frame(self.root, width=1510, height=50, bd=5, relief=RIDGE, bg="#328695")
        Button_Frame.place(x=10, y=460)

        Data_Frame = LabelFrame(self.root, width=1510, height=270, bd=4, relief=RIDGE, bg="#266e73")
        Data_Frame.place(x=10, y=510)

        # inner frames
        Data_FrameLeft = LabelFrame(Manage_Frame, width=1050, text="General Information", font=("arial", 20, "italic bold"), height=390, bd=7, relief=RIDGE, bg="#0099cc")
        Data_FrameLeft.pack(side="left")

        Data_FrameRight = LabelFrame(Manage_Frame, width=1050, text="Prescription", font=("arial", 15, "italic bold"), height=390, bd=7, relief=RIDGE, bg="#0099cc")
        Data_FrameRight.pack(side="right")

        Data_Framedata = LabelFrame(Data_Frame, width=1050, text="Prescription Data", font=("arial", 12, "italic bold"), height=390, bd=4, relief=RIDGE, bg="#3eb7bb")
        Data_Framedata.pack(side="left")

        ###################### LABELS ####################
        Date1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date", padx=2, bg="#0099cc")
        Date1b1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Datetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Date_of_Registration)
        Datetxt.grid(row=0, column=1, padx=10, pady=5, sticky=E)

        ############################## REF ###################
        Ref1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Reference Number", padx=2, bg="#0099cc")
        Ref1b1.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        Reftxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27,state= "disabled" ,textvariable=Ref)
        Reftxt.grid(row=1, column=1, padx=10, pady=5, sticky=E)

        ###################### PATIENT ID #######################################
        PatientId1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Id", padx=2, bg="#0099cc")
        PatientId1b1.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        PatientIdtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PatientId)
        PatientIdtxt.grid(row=2, column=1, padx=10, pady=5, sticky=E)

        ################################## PATIENT NAME ######################
        PatientName1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Name", padx=2, bg="#0099cc")
        PatientName1b1.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        PatientNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PatientName)
        PatientNametxt.grid(row=3, column=1, padx=10, pady=5, sticky=E)

        ############################### DOB ##############################
        DateofBirth1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date of Birth", padx=2, bg="#0099cc")
        DateofBirth1b1.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        DateofBirthtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=DateOfBirth)
        DateofBirthtxt.grid(row=4, column=1, padx=10, pady=5, sticky=E)

        ######################### ADDRESS #############################
        Address1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Address", padx=2, bg="#0099cc")
        Address1b1.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        Addresstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PatientAddress)
        Addresstxt.grid(row=5, column=1, padx=10, pady=5, sticky=E)

        ########################## NHS NUMBER ############################
        NHSNumber1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="NHS Number", padx=2, bg="#0099cc")
        NHSNumber1b1.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        NHSNumbertxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=NHSNumber)
        NHSNumbertxt.grid(row=6, column=1, padx=10, pady=5, sticky=E)

        ################################ TABLET NAME ##########################
        Tablet1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Tablets", padx=2, bg="#0099cc")
        Tablet1b1.grid(row=7, column=0, padx=10, pady=5, sticky=W)

        Tabletcmb = ttk.Combobox(Data_FrameLeft, textvariable=cmbTabletNames, width=25, state="readonly", font=("arial", 12, "bold"))
        Tabletcmb['values'] = ("", "Paracetamol", "Ibuprofen", "Amoxicillin", "Cetirizine", "Metformin", "Lisinopril", "Omeprazole", "Atorvastatin", "Aspirin", "Doxycycline", "Clopidogrel", "Azithromycin", "Alprazolam", "Simvastatin", "Levothyroxine")

        Tabletcmb.current(0)
        Tabletcmb.grid(row=7, column=1, padx=10, pady=5)

        ########################## NO OF TABLETS TO TAKE #######################
        No_of_Tablets1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Number of Tablets", padx=2, bg="#0099cc")
        No_of_Tablets1b1.grid(row=8, column=0, padx=10, pady=5, sticky=W)
        No_of_Tabletstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Number_of_Tablets)
        No_of_Tabletstxt.grid(row=8, column=1, padx=10, pady=5, sticky=E)

    

        ########################## hospital code #######################
        HospitalCode1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Hospital Code ", padx=2, bg="#0099cc")
        HospitalCode1b1.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        HospitalCodetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=HospitalCode)
        HospitalCodetxt.grid(row=0, column=3, padx=10, pady=5, sticky=E)
   
        ###############store instructios###################
        StorageAdvice1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Storage Advice", padx=2, bg="#0099cc")
        StorageAdvice1b1.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft, textvariable=StorageAdvice, width=25, state="readonly", font=("arial", 12, "bold"))
        StorageAdvicecmb['values'] = ("","under room temp","below 5*C","below 0*C","Refrigaration")
        StorageAdvicecmb.current(0)
        StorageAdvicecmb.grid(row=1, column=3, padx=10, pady=5, sticky=E)
   
         ########################## lot number #######################
        Lot_no1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Lot Number", padx=2, bg="#0099cc")
        Lot_no1b1.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        Lot_notxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=Lot)
        Lot_notxt.grid(row=2, column=3, padx=10, pady=5, sticky=E)
   

        IssuedDate1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date of Issue", padx=2, bg="#0099cc")
        IssuedDate1b1.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        IssuedDatetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=IssuedDate)
        IssuedDatetxt.grid(row=3, column=3, padx=10, pady=5, sticky=E)
   


        ExpiryDate1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Expiry Date", padx=2, bg="#0099cc")
        ExpiryDate1b1.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        ExpiryDatetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=ExpiryDate)
        ExpiryDatetxt.grid(row=4, column=3, padx=10, pady=5, sticky=E)
   

        SideEffects1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Side Effects", padx=2, bg="#0099cc")
        SideEffects1b1.grid(row=5, column=2, padx=10, pady=5, sticky=W)
        SideEffectstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=SideEffects)
        SideEffectstxt.grid(row=5, column=3, padx=10, pady=5, sticky=E)
   


        DailyDose1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Daily Dose", padx=2, bg="#0099cc")
        DailyDose1b1.grid(row=6, column=2, padx=10, pady=5, sticky=W)
        DailyDosetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=DailyDose)
        DailyDosetxt.grid(row=6, column=3, padx=10, pady=5, sticky=E)
   

        
        MoreInformation1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text=" More Information", padx=2, bg="#0099cc")
        MoreInformation1b1.grid(row=7, column=2, padx=10, pady=5, sticky=W)
        MoreInformationtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=MoreInformation)
        MoreInformationtxt.grid(row=7, column=3, padx=10, pady=5, sticky=E)
   
        Medication1b1 = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text=" Medication", padx=2, bg="#0099cc")
        Medication1b1.grid(row=8, column=2, padx=10, pady=5, sticky=W)
        Medicationtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=Medication)
        Medicationtxt.grid(row=8, column=3, padx=10, pady=5, sticky=E)
   
       ######################TEXT FIELD FOR PRESCRIPTION######################

        TextPrescription = Text(Data_FrameRight , font = ("arial",12,"bold") , width = 35 , height = 17 ,padx = 3,pady = 5)
        TextPrescription.grid(row = 0 ,column=0)

        #exit for prescription########################################
        TextPrescriptionData = Text(Data_Framedata , font = ("arial",12,"bold") , width = 203 , height = 12)
        TextPrescriptionData.grid(row = 1 ,column=0)


        ###############button############

        Prescriptionbtn = Button(Button_Frame, text="Prescription", bg="#ffaab0", activebackground="#fcceb2", font=("arial", 15, "bold"), width=22,command = prescriptionfunc)
        Prescriptionbtn.grid(row=0, column=0, padx=15)

        Receptionbtn = Button(Button_Frame, text="Prescription Data", bg="#ffaab0", activebackground="#fcceb2", font=("arial", 15, "bold"), width=22, command = prescriptiondatafunc)
        Receptionbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Button_Frame, text="Reset", bg="#ffaab0", activebackground="#fcceb2", font=("arial", 15, "bold"), width=22 , command = resetfunc)
        Resetbtn.grid(row=0, column=2, padx=15)


        Deletebtn = Button(Button_Frame, text="Delete", bg="#ffaab0", activebackground="#fcceb2", font=("arial", 15, "bold"), width=22 , command = deletefunc)
        Deletebtn.grid(row=0, column=3, padx=15)

        Exitbtn = Button(Button_Frame, text="Exit", bg="#ffaab0", activebackground="#fcceb2", font=("arial", 15, "bold"), width=22 , command = exitbtn )
        Exitbtn.grid(row=0, column=4, padx=15)


        Prescriptiondatarow = Label(Data_Framedata, bg = "white",font = ("arial", 12 ,"bold"),
                                    text = "Date\tReference Id\tPatient Name\tDate of  Birth\tNHS Number\tTablet\tNo of Tablet\tIssued Date\tExpiry Date\tDaily Dose\tStorag Advice\tPatient ID")
        Prescriptiondatarow.grid(row = 0 , column = 0 , sticky = W)

if __name__ == "__main__":
    root = Tk()
    application = Hospital(root)
    root.mainloop()
