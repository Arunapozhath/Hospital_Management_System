import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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
                           Firstname.get() + '    \t' + Lastname.get() + "\t\t" + Mobile_no.get() + "\t\t" +
                           Address.get() + "\t" + Pincode.get() + "\t" + member_gendercmb.get() + 
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
        member_paymentwithcmb["values"] = ("","Cash","Debit Card - RuPay","Debit Card - Visa","Debit Card = MasterCard","Credit Card","Google Pay","PayTm","Other")
        member_paymentwithcmb.current(0)
        member_paymentwithcmb.grid(row = 11 , column = 1 , pady = 5 , padx = 10 , sticky = "w" )

        member_membership = Checkbutton(Manage_frame , text = "Membership Fees" , variable = Var5 , onvalue = 1, offvalue = 0 , font = ("arial",15,"bold"),bg = "#001a66" , fg = "white" , command = membership_fees)
        member_membership.grid(row = 12 , column = 0 , sticky = "w")
        member_membershiptxt = Entry(Manage_frame,font = ("arial",15,"bold"),state = "disabled",justify = "right" ,textvariable = Membership)
        member_membershiptxt.grid(row = 12 , column = 1 ,pady = 5 ,padx = 10 ,sticky = "w")





        ###################### DETAIL FRAME####################
        detail_frame = Frame(self.root , relief = RIDGE , bg = "#001a66")
        detail_frame.place(x=500,y=100,width=820,height = 630)
        
        detail_label = Label(detail_frame ,font  =("arial",11,"bold "),padx = 2 ,pady = 10 ,width = 95 , text = "Date\t  Ref Id\t  Firstname  Lastname  Mobile No  Address  Pincode  Gender  Membership")
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








if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()

