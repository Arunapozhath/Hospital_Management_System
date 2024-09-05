import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def main():
    root = Tk()
    app = Windows1(root)
    root.mainloop()

class Windows1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


        self.Username = StringVar()
        self.Password = StringVar()


        self.LabelTitle = Label(self.frame, text="       Pharmacy Management System      ", font=("arial", 40, "bold"),
                                bd=10, relief="sunken")
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.Loginframe1 = Frame(self.frame, width=1000, height=300, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0, padx=10, pady=10)

        self.Loginframe2 = Frame(self.frame, width=1000, height=100, bd=10, relief="groove")
        self.Loginframe2.grid(row=2, column=0, pady=15)

        self.Loginframe3 = Frame(self.frame, width=1000, height=200, bd=10, relief="groove")
        self.Loginframe3.grid(row=3, column=0, pady=5)

        self.button_reg = Button(self.Loginframe3, text="Patient Registration Window", state="disabled" , font=("arial", 15, "bold"),
                                 command=self.Registration_window)
        self.button_reg.grid(row=0, column=0, padx=10, pady=10)

        self.button_Hosp = Button(self.Loginframe3, text="Hospital Management Window", state="disabled" , font=("arial", 15, "bold"),
                                  command=self.Hospital_Window)
        self.button_Hosp.grid(row=0, column=1, padx=10, pady=10)

        self.button_Dr_appt = Button(self.Loginframe3, text="Doctor Appoinment Window", state="disabled" , font=("arial", 15, "bold"),
                                     command=self.Dr_Apoint_window)
        self.button_Dr_appt.grid(row=1, column=0, padx=10, pady=10)

        self.button_med_stock = Button(self.Loginframe3, text="Medicine Stock Window", state="disabled" , font=("arial", 15, "bold"),
                                       command=self.Medicine_stock)
        self.button_med_stock.grid(row=1, column=1, padx=10, pady=10)

        #now we will make user name and password frame

        self.LabelUsername = Label(self.Loginframe1, text = "User Name", font = ("arial",20,"bold"),bd = 3)
        self.LabelUsername.grid(row = 0 , column = 0)

        self.textUsername = Entry(self.Loginframe1,font = ("arial",20,"bold"), bd = 3 ,textvariable = self.Username)
        self.textUsername.grid(row = 0 , column = 1 , padx = 40 , pady = 15 )


        self.LabelPassword = Label(self.Loginframe1, text = "Password", font = ("arial",20,"bold"),bd = 3)
        self.LabelPassword.grid(row = 1 , column = 0)

        self.textPassword = Entry(self.Loginframe1,font = ("arial",20,"bold"),show = "*" , bd = 3 ,textvariable = self.Password)
        self.textPassword.grid(row = 1 , column = 1 , padx = 40 , pady = 15 )


        self.button_login =  Button(self.Loginframe2, text = "Login" , width = 20 , font = ("arial",18,"bold"),
                                          command = self.login_system)
        self.button_login.grid(row = 0 , column = 0 , padx = 10 , pady = 10 )

        self.button_Reset =  Button(self.Loginframe2, text = "Reset" , width = 20 , font = ("arial",18,"bold"),
                                           command = self.reset_btn)
        self.button_Reset.grid(row = 0 , column = 3 , padx = 10 , pady = 10 )

        self.button_Exit =  Button(self.Loginframe2, text = "Exit" , width = 20 , font = ("arial",18,"bold"),
                                          command = self.Exit_btn )
        self.button_Exit.grid(row = 0 , column = 6 , padx = 10 , pady = 10 )


    def login_system(self):
        user = self.Username.get()
        pswd = self.Password.get()

        if (user == str("admin") and (pswd == str("admin"))):
            self.button_reg.config(state = "normal")
            self.button_Hosp.config(state = "normal")
            self.button_Dr_appt.config(state = "normal")
            self.button_med_stock.config(state = "normal")
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System","you have entered an invalid password or user name")
            self.button_reg.config(state = "disabled")
            self.button_Hosp.config(state = "disabled")
            self.button_Dr_appt.config(state = "disabled")
            self.button_med_stock.config(state = "disabled")

            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()

    def reset_btn(self):
        self.button_reg.config(state = "disabled")
        self.button_Hosp.config(state = "disabled")
        self.button_Dr_appt.config(state = "disabled")
        self.button_med_stock.config(state = "disabled")
    #bcoz as we reset we havent given thw correct username and password
        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def Exit_btn(self):
        self.Exit_btn = tkinter.messagebox.askyesno("Pharmacy Management System", "Are you sure you want to exit?")
        if self.Exit_btn > 0:
            self.master.destroy()
            return     





    # Methods for opening new windows
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)

    def Hospital_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Hospital(self.newWindow)

    def Dr_Apoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Doctor(self.newWindow)

    def Medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = MedicineStock(self.newWindow)

class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background = "black")


        #we will take live time using time module

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        Mobile_no = StringVar()
        Pincode = StringVar()
        Address = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()


        #this is for combobox
        Var1 = StringVar()
        Var2 = StringVar()
        Var3 = StringVar()
        Var4 = StringVar()
        Var5 = IntVar()


        Membership = StringVar()
        Membership.set("0")


        ######################FUNCTIONS########################
        def exitbtt():
            exitbtt = tkinter.messagebox.askyesno(" Member Registration Form","Are you sure you want to exit ?")
            if exitbtt > 0:   
                root.destroy()
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Registration(self.newWindow)
                return

        def resetbtt():
            Firstname.set("")
            Ref.set("")
            Mobile_no.set("")
            Pincode.set("")
            Address.set("")
            Firstname.set("")
            Lastname.set("")
            Var1.set("")
            Var2.set("")
            Var3.set("")
            Var4.set("")
            Var5.set("")
            Membership.set("0")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt(state = "disabled")


        def reeesetbtt():
            reeesetbtt = tkinter.messagebox.askokcancel("Member Registration Form","You want to as New Record")
            if reeesetbtt > 0:
                resetbtt()
            elif reeesetbtt <= 0:
                 resetbtt()
                 detail_labeltxt.delete("1.0", END)
                 return
        
        def Reference_number():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)
        
        def membership_fees():

            if(Var5.get() == 1):#checkbox clicked
                member_membershiptxt.configure(state = "normal")
                item = float(15000) #membership plan can be changed according to you
                Membership.set(str(item)+ "Rs")
            elif( Var5.get() == 0):
                #when unchecked
                member_membershiptxt.configure(state = "disabled")
                Membership.set("0")
                   

        def Reciept():
                Reference_number()
                detail_labeltxt.insert(END, "\t" + Date_of_Registration.get() + "      \t" + Ref.get() + "     \t\t" +
                           Firstname.get() + '    \t\t' + Lastname.get() + "\t" + Mobile_no.get() + "\t" +
                           Address.get() + "\t\t" + Pincode.get() + "\t" + member_gendercmb.get() + 
                           "\t\t" + Membership.get() + "\n")




        #######################  TITLE  ####################
        title = Label(self.root, text = "Member Registration Form", font = ("monnotype corsiva",30,"bold"),bd = 5,
                      relief = GROOVE,bg = "#E6005C", fg = "#000000")
        title.pack(side=TOP, fill = X)

        ########################## MEMBER FRAME ################
        Manage_frame = Frame(self.root , bd = 4, relief = RIDGE , bg = "#001a66")
        Manage_frame.place(x=20,y=100,width=450,height = 630)

        ############ text ,label, combo boxesframe #################
        Cus_title = Label(Manage_frame,text = "Customer Details" , font =("arial",20,"bold"), bg = "#001a66",fg = "white")
        Cus_title.grid(row =0 , columnspan = 2 ,pady = 5) 

        member_date1b1 = Label(Manage_frame,text = "Date",font = ("arail",15,"bold"),bg = "#001a66" , fg = "white")
        member_date1b1.grid(row = 1  , column = 0 , pady = 5, padx = 10 , sticky = "w")

        member_datetxt = Entry(Manage_frame, font = ("arial",15,"bold"), textvariable = Date_of_Registration)
        member_datetxt.grid(row = 1, column = 1 , pady = 5 ,padx = 10 , sticky = "w")

        member_reflbl = Label(Manage_frame,text = "Reference ID" , font = ("arial",15,"bold"), bg = "#001a66" , fg = "white")
        member_reflbl.grid(row = 2 , column = 0 , pady = 5 , padx = 10 , sticky = "w")

        member_reftxt = Entry(Manage_frame, font = ("arial",15,"bold"),state = "disabled" , text = Ref)
        member_reftxt.grid(row = 2, column = 1 , pady = 5 ,padx = 10 , sticky = "w")

        member_fname1b1 = Label(Manage_frame,text = "First Name",font = ("arail",15,"bold"),bg = "#001a66" , fg = "white")
        member_fname1b1.grid(row = 3  , column = 0 , pady = 5, padx = 10 , sticky = "w")

        member_fnametxt = Entry(Manage_frame, font = ("arial",15,"bold"), textvariable = Firstname)
        member_fnametxt.grid(row = 3, column = 1 , pady = 5 ,padx = 10 , sticky = "w")

        member_1name1b1 = Label(Manage_frame,text = "Last Name",font = ("arail",15,"bold"),bg = "#001a66" , fg = "white")
        member_1name1b1.grid(row = 4  , column = 0 , pady = 5, padx = 10 , sticky = "w")

        member_1nametxt = Entry(Manage_frame, font = ("arial",15,"bold"), textvariable = Lastname)
        member_1nametxt.grid(row = 4, column = 1 , pady = 5 ,padx = 10 , sticky = "w")

        member_mobile1b1 = Label(Manage_frame,text = "Mobile No",font = ("arail",15,"bold"),bg = "#001a66" , fg = "white")
        member_mobile1b1.grid(row = 5  , column = 0 , pady = 5, padx = 10 , sticky = "w")

        member_mobiletxt = Entry(Manage_frame, font = ("arial",15,"bold"), textvariable = Mobile_no)
        member_mobiletxt.grid(row = 5, column = 1 , pady = 5 ,padx = 10 , sticky = "w")


        member_address1b1 = Label(Manage_frame,text = "Address",font = ("arail",15,"bold"),bg = "#001a66" , fg = "white")
        member_address1b1.grid(row = 6  , column = 0 , pady = 5, padx = 10 , sticky = "w")

        member_addresstxt = Entry(Manage_frame, font = ("arial",15,"bold"), textvariable = Address)
        member_addresstxt.grid(row = 6, column = 1 , pady = 5 ,padx = 10 , sticky = "w")

        member_pincode1b1 = Label(Manage_frame,text = "Pin code",font = ("arail",15,"bold"),bg = "#001a66" , fg = "white")
        member_pincode1b1.grid(row = 7  , column = 0 , pady = 5, padx = 10 , sticky = "w")

        member_pincodetxt = Entry(Manage_frame, font = ("arial",15,"bold"), textvariable = Pincode)
        member_pincodetxt.grid(row = 7, column = 1 , pady = 5 ,padx = 10 , sticky = "w")

        member_gender1b1 = Label(Manage_frame,text = "Gender",font = ("arail",15,"bold"),bg = "#001a66" , fg = "white")
        member_gender1b1.grid(row = 8  , column = 0 , pady = 5, padx = 10 , sticky = "w")

        member_gendercmb = ttk.Combobox(Manage_frame, text = Var4 , state = "readonly" ,font = ("arial",15,"bold"),
                                        width = 19 )
        member_gendercmb["values"] = ("","Male","Female","Other")
        member_gendercmb.current(0)
        member_gendercmb.grid(row = 8 , column = 1 , pady = 5 , padx = 10 , sticky = "w" )


        member_id_proof1b1 = Label(Manage_frame,text = "ID Proof",font = ("arail",15,"bold"),bg = "#001a66" , fg = "white")
        member_id_proof1b1.grid(row = 9  , column = 0 , pady = 5, padx = 10 , sticky = "w")

        member_id_proofcmb = ttk.Combobox(Manage_frame, text = Var3 , state = "readonly" ,font = ("arial",15,"bold"),
                                        width = 19 )
        member_id_proofcmb["values"] = ("","Aadhar Card","Passport","Driving License","Pan Card","Student ID")
        member_id_proofcmb.current(0)
        member_id_proofcmb.grid(row = 9 , column = 1 , pady = 5 , padx = 10 , sticky = "w" )


        member_memtype1b1 = Label(Manage_frame,text = "Member Type",font = ("arail",15,"bold"),bg = "#001a66" , fg = "white")
        member_memtype1b1.grid(row = 10  , column = 0 , pady = 5, padx = 10 , sticky = "w")

        member_memtypecmb = ttk.Combobox(Manage_frame, text = Var2 , state = "readonly" ,font = ("arial",15,"bold"),
                                        width = 19 )
        member_memtypecmb["values"] = ("","Insurance","Pay Immediately","Ayushman Card")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row = 10 , column = 1 , pady = 5 , padx = 10 , sticky = "w" )

        member_paymentwith1b1 = Label(Manage_frame,text = " payment method",font = ("arail",15,"bold"),bg = "#001a66" , fg = "white")
        member_paymentwith1b1.grid(row = 11  , column = 0 , pady = 5, padx = 10 , sticky = "w")

        member_paymentwithcmb = ttk.Combobox(Manage_frame, text = Var1, state = "readonly" ,font = ("arial",15,"bold"),
                                        width = 19 )
        member_paymentwithcmb["values"] = ("","Cash","Debit Card - RuPay","Debit Card - Visa","Debit Card - MasterCard","Credit Card","Google Pay","PayTm","Other")
        member_paymentwithcmb.current(0)
        member_paymentwithcmb.grid(row = 11 , column = 1 , pady = 5 , padx = 10 , sticky = "w" )

        member_membership = Checkbutton(Manage_frame , text = "Membership Fees" , variable = Var5 , onvalue = 1, offvalue = 0 , font = ("arial",15,"bold"),bg = "#001a66" , fg = "white" , command = membership_fees)
        member_membership.grid(row = 12 , column = 0 , sticky = "w")
        member_membershiptxt = Entry(Manage_frame,font = ("arial",15,"bold"),state = "disabled",justify = "right" ,textvariable = Membership)
        member_membershiptxt.grid(row = 12 , column = 1 ,pady = 5 ,padx = 10 ,sticky = "w")





        ###################### DETAIL FRAME####################
        detail_frame = Frame(self.root , relief = RIDGE , bg = "#001a66")
        detail_frame.place(x=500,y=100,width=820,height = 630)
        
        detail_label = Label(detail_frame ,font  =("arial",11,"bold "),padx = 2 ,pady = 10 ,width = 95 , text = "Date\t  Ref Id\t    Firstname  Lastname  Mobile No  Address  Pincode  Gender  Membership")
        detail_label.grid(row = 0 , column = 0 , columnspan = 4 , sticky = "w")
        detail_labeltxt = Text(detail_frame , width = 123 , height = 34 , font = ("arial", 10))
        detail_labeltxt.grid(row = 1 ,column = 0 ,columnspan = 4)

        #################button detail frame################
        receipttbtn = Button(detail_frame , padx = 15 ,bd = 5 , font = ("arial",12,"bold"),bg = "#ff9966",width = 20 ,text = "Reciept" , command = Reciept )
        receipttbtn.grid(row = 2 ,column = 0 )


        resettbtn = Button(detail_frame , padx = 15 ,bd = 5 , font = ("arial",12,"bold"),bg = "#ff9966",width = 20 ,text = "Reset" , command = reeesetbtt)
        resettbtn.grid(row = 2 ,column = 1 )

        exittbtn = Button(detail_frame , padx = 15 ,bd = 5 , font = ("arial",12,"bold"),bg = "#ff9966",width = 20 ,text = "Exit", command = exitbtt )
                          
        exittbtn.grid(row = 2 ,column = 2 )





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
    main()
