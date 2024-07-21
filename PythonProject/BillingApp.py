from tkinter import *
import random
import os
from tkinter import messagebox

# ============main============================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        
        bg_color = "#e6f0ff"
        self.root.configure(bg=bg_color)  # Setting the background color here
        
        title = Label(self.root, text="Invoice Manager", font=('times new roman', 27, 'bold'), pady=2, bd=12, bg="#cce0e0", fg="Black", relief=GROOVE)
        title.pack(fill=X)

    # ================E-BOOKS   variables=======================
        self.Dune = IntVar()
        self.Sapiens = IntVar()
        self.Fahrenheit = IntVar()
        self.Grit = IntVar()
        self.Beloved = IntVar()
        self.Shantaram = IntVar()
        
    # =================  BEVERAGES   ========================================     
        self.Elixirs = IntVar()
        self.Infusions = IntVar()
        self.Kombucha = IntVar()
        self.Seltzers = IntVar()
        self.Matcha = IntVar()
        self.Smoothies = IntVar()
        
    # ================= Confection    ========================================     
        self.Macaron = IntVar()
        self.Truffle = IntVar()
        self.Nougat = IntVar()
        self.Taffy = IntVar()
        self.Bonbon = IntVar()
        self.Fudge = IntVar()
        
        self.E_Books_price = StringVar()
        self.Beverages_price = StringVar()
        self.Confection_price = StringVar()
        
        # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        
         # ===============Tax================================
        self.E_Books_tax = StringVar()
        self.Beverages_tax = StringVar()
        self.Confection_tax = StringVar()

 # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'),
                        bd=6, fg="Black", bg="#e6f0ff")
        F1.place(x=0, y=80, relheight=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=10, pady=0)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15' , bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)
        
        cphn_lbl = Label(F1, text="Costumer Phone:", bg="#e6f0ff", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)
        
        c_bill_lbl = Label(F1, text="Bill Number:", bg="#e6f0ff", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)
        
        bill_btn = Button(F1, text="Search", command=self.search_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bill_btn.grid(row=0, column=6, pady=5, padx=10)
        
#billing software

#===================E BOOKS=================================

        F2 = LabelFrame(self.root, text="E Books", font=('times new roman', 15, 'bold'), 
                        bd=10, fg="Black", bg = "#e6f0ff")
        F2.place(x=5, y=170, width=310, height=340)
        
        dune_lbl = Label(F2, text="Dune", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")


        dune_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        dune_txt = Entry(F2, width=10, textvariable=self.Dune, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        dune_txt.grid(row=0, column=1, padx=10, pady=10)
        
        sapiens_lbl = Label(F2, text="Sapiens", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        sapiens_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        sapiens_txt = Entry(F2, width=10, textvariable=self.Sapiens, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        sapiens_txt.grid(row=1, column=1, padx=10, pady=10)
        
        fahrenheit_lbl = Label(F2, text="Fahrenheit", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        fahrenheit_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        fahrenheit_txt = Entry(F2, width=10, textvariable=self.Fahrenheit, font=('times new roman', 16, 'bold'), bd=3, relief =GROOVE)
        fahrenheit_txt.grid(row=2, column=1, padx=10, pady=10)
        
        grit_lbl = Label(F2, text="Grit", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        grit_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        grit_txt = Entry(F2, width=10, textvariable=self.Grit, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        grit_txt.grid(row=3, column=1, padx=10, pady=10)
        
        beloved_lbl = Label(F2, text="Beloved", font =('times new roman', 16, 'bold'), bg = "#e6f0ff", fg = "black")
        beloved_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        beloved_txt = Entry(F2, width=10, textvariable=self.Beloved, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        beloved_txt.grid(row=4, column=1, padx=10, pady=10)
        
        shantaram_lbl = Label(F2, text="Shantaram", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        shantaram_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        shantaram_txt = Entry(F2, width=10, textvariable=self.Shantaram, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        shantaram_txt.grid(row=5, column=1, padx=10, pady=10)

# ==========BEVERAGES=========================
        
        F3 = LabelFrame(self.root, text="Beverages", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#e6f0ff")
        F3.place(x=340, y=170, width=310, height=340)
        
        elixir_lbl = Label(F3, text="Elixirs", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        elixir_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        elixir_txt = Entry(F3, width=10, textvariable=self.Elixirs, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        elixir_txt.grid(row=0, column=1, padx=10, pady=10)
        
        infusion_lbl = Label(F3, text=" Infusions", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        infusion_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        infusion_txt = Entry(F3, width=10, textvariable=self.Infusions, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        infusion_txt.grid(row=1, column=1, padx=10, pady=10)
        
        kombucha_lbl = Label(F3, text="Kombucha", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        kombucha_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        kombucha_txt = Entry(F3, width=10, textvariable=self.Kombucha, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        kombucha_txt.grid(row=2, column=1, padx=10, pady=10)
        
        seltzer_lbl = Label(F3, text="Seltzers", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        seltzer_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        seltzer_txt = Entry(F3, width=10, textvariable=self.Seltzers, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        seltzer_txt.grid(row=3, column=1, padx=10, pady=10)
        
        matcha_lbl = Label(F3, text="Matcha", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        matcha_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        matcha_txt = Entry(F3, width=10, textvariable=self.Matcha, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        matcha_txt.grid(row=4, column=1, padx=10, pady=10)
        
        smoothie_lbl = Label(F3, text="Smoothies", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        smoothie_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        smoothie_txt = Entry(F3, width=10, textvariable=self.Smoothies, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        smoothie_txt.grid(row=5, column=1, padx=10, pady=10)
        
# ===========CONFECTION================================
        F4 = LabelFrame(self.root, text="Confection", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#e6f0ff")
        F4.place(x=670, y=170, width=310, height=340)
        
        macaron_lbl = Label(F4, text="Macaron", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        macaron_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        macaron_txt = Entry(F4, width=10, textvariable=self.Macaron, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        macaron_txt.grid(row=0, column=1, padx=10, pady=10)
        
        truffle_lbl = Label(F4, text="Truffle", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        truffle_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        truffle_txt = Entry(F4, width=10, textvariable=self.Truffle, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        truffle_txt.grid(row=1, column=1, padx=10, pady=10)
        
        nougat_lbl = Label(F4, text="Nougat", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        nougat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        nougat_txt = Entry(F4, width=10, textvariable=self.Nougat, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        nougat_txt.grid(row=2, column=1, padx=10, pady=10)
        
        taffy_lbl = Label(F4, text="Taffy", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        taffy_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        taffy_txt = Entry(F4, width=10, textvariable=self.Taffy, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        taffy_txt.grid(row=3, column=1, padx=10, pady=10)
        
        bonbon_lbl = Label(F4, text="Bonbon", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        bonbon_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        bonbon_txt = Entry(F4, width=10, textvariable=self.Bonbon, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        bonbon_txt.grid(row=4, column=1, padx=10, pady=10)
        
        fudge_lbl = Label(F4, text="Fudge", font=('times new roman', 16, 'bold'), bg="#e6f0ff", fg="black")
        fudge_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        fudge_txt = Entry(F4, width=10, textvariable=self.Fudge, font=('times new roman', 16, 'bold'), bd=3, relief=GROOVE)
        fudge_txt.grid(row=5, column=1, padx=10, pady=10)     

#  BILL AREA

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=954, y=170, width=330, height=340)
        
        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        
       
 #   Create a Button Frame and Button for Billing Software
 
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="black", bg="#e6f0ff")
        F6.place(x=0, y=520, relwidth=1, height=126)
        
        m1_lbl = Label(F6, text="Total E-Book Price", font=('times new roman', 14, 'bold'), bg="#e6f0ff", fg="black")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.E_Books_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1) 

      
        m2_lbl= Label(F6, text="Total Beverage Price", font=('times new roman', 14, 'bold'), bg="#e6f0ff", fg="black")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.Beverages_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)
        
        
        m3_lbl= Label(F6, text="Total Confection Price", font=('times new roman', 14, 'bold'), bg="#e6f0ff", fg="black")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.Confection_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)


        m4_lbl = Label(F6, text="E-Book Tax", font=('times new roman', 14, 'bold'), bg="#e6f0ff", fg="black")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.E_Books_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)


        m5_lbl = Label(F6, text="Beverages Tax", font=('times new roman', 14, 'bold'), bg="#e6f0ff", fg="black")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.Beverages_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)


        m6_lbl = Label(F6, text="Confection Tax", font=('times new roman', 14, 'bold'), bg="#e6f0ff", fg="black")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.Confection_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)


#   BUTTONS 

        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)
        
        total_btn = Button(btn_f, command=self.total, text="Total", bg="#e6f0ff", bd=2, fg="black", pady=15, width=10, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f , command=self.bill_area, text="Generate Bill", bd=2, bg="#e6f0ff", fg="black", pady=15, width=10, font='arial 13 bold' )
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)
        
        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#e6f0ff", bd=2, fg="black", pady=15, width=10, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)
        
        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#e6f0ff", fg="black", pady=15, width=10, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()
        
        
        
    def total(self):
            self.m_h_g_p = self.Dune.get()*12
            self.m_s_p = self.Sapiens.get()*2
            self.m_m_p = self.Fahrenheit.get()*5
            self.m_d_p = self.Grit.get()*30
            self.m_n_p = self.Beloved.get()*5
            self.m_t_g_p = self.Shantaram.get()*15
            self.total_ebook_price = float(self.m_m_p+self.m_h_g_p+self.m_d_p+self.m_n_p+self.m_t_g_p+self.m_s_p)
            
            
            self.Beverages_price.set("Rs. "+str(self.total_ebook_price))
            self.c_tax = round((self.total_ebook_price*0.05), 2)
            self.E_Books_tax.set("Rs. "+str(self.c_tax))
            
            
         
            self.g_r_p = self.Elixirs.get()*10
            self.g_f_o_p = self.Infusions.get()*10
            self.g_w_p = self.Kombucha.get()*10
            self.g_d_p = self.Seltzers.get()*6
            self.g_f_p = self.Matcha.get()*8
            self.g_m_p = self.Smoothies.get()*5 
            self.total_beverage_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_d_p+self.g_f_p+self.g_m_p)
            
            
            self.Beverages_price.set("Rs. "+str(self.total_beverage_price))
            self.b_tax = round((self.total_beverage_price*5), 2)
            self.Beverages_tax.set("Rs. "+str(self.b_tax))
            
            
            self.c_d_s_p = self.Macaron.get()*10
            self.c_d_l_p = self.Truffle.get()*10
            self.c_d_m_p = self.Nougat.get()*10
            self.c_d_c_p = self.Taffy.get()*10
            self.c_d_f_p = self.Bonbon.get()*10
            self.c_m_d = self.Fudge.get()*10
            self.total_confection_price = float(self.c_d_s_p+self.c_d_l_p+self.c_d_m_p+self.c_d_c_p+self.c_d_f_p+self.c_m_d)
            
            
            self.Confection_price.set("Rs. "+str(self.total_confection_price))
            self.c_d_tax = round((self.total_confection_price * 0.1), 2)
            self.Confection_tax.set("Rs. "+str(self.c_d_tax))
            
            self.total_bill = float(self.total_ebook_price+self.total_beverage_price+self.total_confection_price)
            
#  WELCOME BILL

     
    def welcome_bill(self):
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, "\tWelcome Webcode Retail")   
            self.txtarea.insert(END, f"\n Bill Number:{self.bill_no.get() }")
            self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
            self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
            self.txtarea.insert(END, f"\n====================================")
            self.txtarea.insert(END, f"\nProducts\t\tQTY\tPrice")

    
#  BILL AREA     
                     
            
    def bill_area(self):
         if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")     
         elif self.E_Books_price.get() == "Rs. 0.0" and self.Beverages_price.get() == "Rs. 0.0" and self.Confection_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
         else:
            self.welcome_bill()     
            
            
        #     E-BOOK
            
            if self.Dune.get() != 0:
                    self.txtarea.insert(END, f"\nDune\t\t{self.Dune.get()}\t\t{self.m_s_p}")
            if self.Sapiens.get() != 0:
                    self.txtarea.insert(END, f"\nSapiens\t\t{self.Sapiens.get()}\t\t{self.m_m_p}")
            if self.Fahrenheit.get() != 0:
                    self.txtarea.insert(END, f"\n Fahrenheit\t\t{self.Fahrenheit.get()}\t\t{self.m_h_g_p}")
            if self.Grit.get() != 0:
                    self.txtarea.insert(END, f"\nGrit\t\t{self.Grit.get()}\t\t{self.m_d_p}")
            if self.Beloved.get() != 0:
                    self.txtarea.insert(END, f"\nBeloved\t\t{self.Beloved.get()}\t\t{self.m_n_p}")
            if self.Shantaram.get() != 0:
                    self.txtarea.insert(END, f"\n Shantaram\t\t{self.Shantaram.get()}\t\t{self.m_t_g_p}")
            
      #   BEVERAGES
        
            if self.Elixirs.get() != 0:
                    self.txtarea.insert(END, f"\n Elixirs\t\t{self.Elixirs.get()}\t\t{self.g_r_p}")
            if self.Infusions.get() != 0:
                    self.txtarea.insert(END, f"\n Infusions\t\t{self.Infusions.get()}\t\t{self.g_f_o_p}")
            if self.Kombucha.get() != 0:
                    self.txtarea.insert(END, f"\n Kombucha\t\t{self.Kombucha.get()}\t\t{self.g_w_p}")
            if self.Seltzers.get() != 0:
                    self.txtarea.insert(END, f"\n Seltzers\t\t{self.Seltzers.get()}\t\t{self.g_d_p}")
            if self.Matcha.get() != 0 :
                    self.txtarea.insert(END, f"\n Matcha\t\t{self.Matcha.get()}\t\t{self.g_f_p}")
            if self.Smoothies.get() != 0:
                    self.txtarea.insert(END, f"\n Smoothies\t\t{self.Smoothies.get()}\t\t{self.g_m_p}") 
                    
                    
   #     CONFECTION
       
            if  self.Macaron.get() != 0:
                    self.txtarea.insert(END, f"\n Macaron\t\t{self.Macaron.get()}\t\t{self.c_d_s_p}")
            if self.Truffle.get() != 0:
                    self.txtarea.insert(END, f"\n Truffle\t\t{self.Truffle.get()}\t\t{self.c_d_l_p}")
            if self.Nougat.get() != 0 :
                    self.txtarea.insert(END, f"\n Nougat\t\t{self.Nougat.get()}\t\t{self.c_d_m_p}")
            if self.Taffy.get() != 0:
                    self.txtarea.insert(END, f"\n Taffy\t\t{self.Taffy.get()}\t\t{self.c_d_c_p}")
            if self.Bonbon.get() != 0:
                    self.txtarea.insert(END, f"\n Bonbon\t\t{self.Bonbon.get()}\t\t{self.c_d_f_p}")
            if self.Fudge.get() != 0:
                    self.txtarea.insert(END, f"\n Fudge\t\t{self.Fudge.get()}\t\t{self.c_m_d}")
                    self.txtarea.insert(END, f"\n--------------------------------------------------")                                                                                                   
                                                            
        #   Taxes
            if self.E_Books_tax.get() != '0.0':
                    self.txtarea.insert(END, f"\n E-Book Tax\t\t{self.E_Books_tax.get()}")
            if self.Beverages_tax.get() != '0.0':
                    self.txtarea.insert(END, f"\n Beverage Tax\t\t{self.Beverages_tax.get()}")
            if self.Confection_tax.get() != '0.0':
                    self.txtarea.insert(END, f"\n Confection Tax\t\t{self.Confection_tax.get()}")
                    
                    self.txtarea.insert(END, f"\n Total Bill:\t\t\t Rs.{self.total_bill}")
                    self.txtarea.insert(END, f"\n--------------------------------------")
                    self.save_bill()                  
            
    def save_bill(self):
           op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
           if op > 0:
                self.bill_data = self.txtarea.get('1.0', END)
                f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
           else:
               return     
       
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")
            
        
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.Dune.set(0)
            self.Sapiens.set(0)
            self.Fahrenheit.set(0)
            self.Grit.set(0)
            self.Beloved.set(0)
            self.Shantaram.set(0)     
            
        #     beverage
            self.Elixirs.set(0)
            self.Infusions.set(0)
            self.Kombucha.set(0)
            self.Seltzers.set(0)
            self.Matcha.set(0)
            self.Smoothies.set(0)
            
        #     confection
        
            self.Macaron.set(0)
            self.Truffle.set(0)
            self.Nougat.set(0)
            self.Taffy.set(0)
            self.Bonbon.set(0)
            self.Fudge.set(0)
            
      #   Taxes
      
            self.E_Books_price.set("")
            self.Beverages_price.set("")
            self.Confection_price.set("")
            
            self.E_Books_tax.set("")
            self.Beverages_tax.set("")
            self.Confection_tax.set("")
            
            self.c_name.set("")
            self.c_phone.set("")
            
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            
            self.search_bill.set("")
            self.welcome_bill()
            
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()                               

root = Tk()
obj = Bill_App(root)
root.mainloop()
