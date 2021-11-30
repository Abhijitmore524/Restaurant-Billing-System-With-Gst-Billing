from tkinter import *
import math, random, os
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Restaurant Billing Software", bd=12, relief=GROOVE, bg=bg_color,
                      font=("Times new roman", 30, 'bold'), pady=2).pack(fill=X)
        # ======================variable==========================
        # ======================Meals=========================
        self.Butter_Chicken = IntVar()
        self.Paneer_Tikka = IntVar()
        self.Plain_Stream_Rice = IntVar()
        self.Palak_Paneer = IntVar()
        self.Veg_Biryani = IntVar()
        self.Roti = IntVar()
        # ======================Starter============================
        self.Masala_Papad = IntVar()
        self.Paneer_chilli = IntVar()
        self.Mushroom_Gravy = IntVar()
        self.Paneer_65 = IntVar()
        self.Veg_Munchuriyan = IntVar()
        self.tea = IntVar()
        # ========================Cold drinks==========================
        self.maza = IntVar()
        self.Cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # ======================Total product Price and text variables======================
        self.Meal_Price = StringVar()
        self.Starter_Price = StringVar()
        self.cold_drink_Price = StringVar()

        self.Meal_tax = StringVar()
        self.Starter_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ==========================customer================================================
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        # =======================Customer Detail Frame
        F1 = LabelFrame(self.root, bd=10, text="Customer Details", font=("Times new roman", 15, "bold"), fg="gold",bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg='white', font=("Times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=20, textvariable=self.c_name, font='arial 15', bd=7, relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text=" Phone No", bg=bg_color, fg='white', font=("Times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=20, textvariable=self.c_phon, font='arial 15', bd=7, relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl = Label(F1, text="Bill No", bg=bg_color, fg='white', font=("Times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=20, textvariable=self.search_bill, font='arial 15', bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text='Search', command=self.find_bill, width=16, bd=7, font='arial 12 bold').grid(row=0,column=6,pady=10,padx=10)

        # ===================Meals Frame=================================================================================================
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Meals", font=("Times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=450, height=400)

        Butter_chicken_lbl = Label(F2, text="Butter Chicken", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10,
                                                                                                                        sticky=W)
        Butter_chicken_txt = Entry(F2, width=10, textvariable=self.Butter_Chicken, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=0, column=1, padx=10,
                                                                                                                              pady=10)

        Paneer_Tikka_lbl = Label(F2, text="Paneer Tikka", font=("times new roman", 16, "bold"), bg=bg_color, fg='lightgreen').grid(row=1, column=0, padx=10,
                                                                                                                               pady=10, sticky=W)
        Paneer_Tikka_txt = Entry(F2, width=10, textvariable=self.Paneer_Tikka, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=1,column=1, padx=10, pady=10)

        Plain_stream_rice_lbl = Label(F2, text="Plain Stream Rice", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10,
                                                                                                                         sticky=W)
        Plain_stream_rice_txt = Entry(F2, width=10, textvariable=self.Plain_Stream_Rice, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=2,
                                                                                                                            column=1, padx=10, pady=10)

        Palak_Paneer_lbl = Label(F2, text="Palak Paneer", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky=W)
        Palak_Paneer_txt = Entry(F2, width=10, textvariable=self.Palak_Paneer, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Veg_Biryani_lbl = Label(F2, text="Veg Biryani", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky=W)
        Veg_Biryani_txt = Entry(F2, width=10, textvariable=self.Veg_Biryani, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Body_L_lbl = Label(F2, text="Roti", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky=W)
        Body_L_txt = Entry(F2, width=10, textvariable=self.Roti, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===================Starter Frame=================================================================================================
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Starter", font=("Times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F3.place(x=360, y=180, width=450, height=400)

        g1_lbl = Label(F3, text="Masala Papad", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky=W)
        g1_txt = Entry(F3, width=10, textvariable=self.Masala_Papad, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3, text="Paneer chilli", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky=W)
        g2_txt = Entry(F3, width=10, textvariable=self.Paneer_chilli, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(F3, text="Mushroom Gravy", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky=W)
        g3_txt = Entry(F3, width=10, textvariable=self.Mushroom_Gravy, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F3, text="Paneer 65", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky=W)
        g4_txt = Entry(F3, width=10, textvariable=self.Paneer_65, font=("times new roman", 16, "bold"), bd=5,relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F3, text="Veg Munchuriyan", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,column=0,padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky=W)
        g5_txt = Entry(F3, width=10, textvariable=self.Veg_Munchuriyan, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky=W)
        g6_txt = Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===================Cold Drink Frame=================================================================================================
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold drinks", font=("Times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=700, y=180, width=390, height=400)

        C1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky=W)
        C1_txt = Entry(F4, width=10, textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        C2_lbl = Label(F4, text="Cock", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky=W)
        C2_txt = Entry(F4, width=10, textvariable=self.Cock, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        C3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky=W)
        C3_txt = Entry(F4, width=10, textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        C4_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky=W)
        C4_txt = Entry(F4, width=10, textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        C5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky=W)
        C5_txt = Entry(F4, width=10, textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        C6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky=W)
        C6_txt = Entry(F4, width=10, textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # =============Bill Area==============================================================================================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1100, y=180, width=430, height=400)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ==================Button Frame====================================================================================

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Billing Menu", font=("Times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=2, y=590, relwidth=1, height=190)

        m1_lbl = Label(F6, text="Total Meal", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=2, sticky="w")
        m1_txt = Entry(F6, width=22, textvariable=self.Meal_Price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=2)

        m2_lbl = Label(F6, text="Total Starter", bg=bg_color, fg="white",
                       font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=2, sticky="w")
        m2_txt = Entry(F6, width=22, textvariable=self.Starter_Price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=2)

        m3_lbl = Label(F6, text="Total Cold Drinks", bg=bg_color , fg="white",
                       font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=2, sticky="w")
        m3_txt = Entry(F6, width=22, textvariable=self.cold_drink_Price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=2)

        c1_lbl = Label(F6, text="Meal Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=0, column=2, padx=20, pady=2, sticky="w")
        c1_txt = Entry(F6, width=22, font="arial 10 bold", textvariable=self.Meal_tax, bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=10, pady=2)

        c2_lbl = Label(F6, text="Starter Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=1, column=2, padx=20, pady=2, sticky="w")
        c2_txt = Entry(F6, width=22, font="arial 10 bold", textvariable=self.Starter_tax, bd=7, relief=SUNKEN).grid(
            row=1, column=3, padx=10, pady=2)

        c3_lbl = Label(F6, text="Cold Drinks Tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(
            row=2, column=2, padx=20, pady=2, sticky="w")
        c3_txt = Entry(F6, width=22, font="arial 10 bold", textvariable=self.cold_drink_tax, bd=7, relief=SUNKEN).grid(
            row=2, column=3, padx=10, pady=2)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=800, width=700, height=110)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="cadetblue", fg="white", pady=15, width=12, bd=5,
                           font="arial 15 bold").grid(row=0, column=0, padx=7, pady=5)
        GBill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white", pady=15,
                           width=12, bd=5, font="arial 15 bold").grid(row=0, column=1, padx=7, pady=5)
        Clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", pady=15, width=12,
                           bd=5, font="arial 15 bold").grid(row=0, column=2, padx=7, pady=5)
        Exit_btn = Button(btn_F, text="Exit", command=self.Exit_app, bg="cadetblue", fg="white", pady=15, width=11,
                          bd=5, font="arial 15 bold").grid(row=0, column=3, padx=7, pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p = self.Butter_Chicken.get() * 240
        self.c_fc_p = self.Paneer_Tikka.get() * 160
        self.c_fw_p = self.Plain_Stream_Rice.get() * 80
        self.c_hs_p = self.Palak_Paneer.get() * 160
        self.c_hg_p = self.Veg_Biryani.get() * 140
        self.c_bl_p = self.Roti.get() * 12

        self.total_Meal_Price = float(
            self.c_s_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_hs_p +
            self.c_hg_p +
            self.c_bl_p
        )
        self.Meal_Price.set("Rs. " + str(self.total_Meal_Price))
        self.c_tax = round((self.total_Meal_Price * 0.05), 2)
        self.Meal_tax.set("Rs. " + str(self.c_tax))

        self.g_r_p = self.Masala_Papad.get() * 15
        self.g_f_p = self.Paneer_chilli.get() * 120
        self.g_d_p = self.Mushroom_Gravy.get() * 60
        self.g_w_p = self.Paneer_65.get() * 130
        self.g_s_p = self.Veg_Munchuriyan.get() * 80
        self.g_t_p = self.tea.get() * 20

        self.total_Starter_Price = float(
            self.g_r_p +
            self.g_f_p +
            self.g_d_p +
            self.g_w_p +
            self.g_s_p +
            self.g_t_p
        )
        self.Starter_Price.set("Rs. " + str(self.total_Starter_Price))
        self.g_tax = round((self.total_Starter_Price * 0.05), 2)
        self.Starter_tax.set("Rs. " + str(self.g_tax))

        self.d_m_p = self.maza.get() * 40
        self.d_c_p = self.Cock.get() * 120
        self.d_f_p = self.frooti.get() * 30
        self.d_t_p = self.thumbsup.get() * 180
        self.d_l_p = self.limca.get() * 40
        self.d_s_p = self.sprite.get() * 180

        self.total_drinks_Price = float(
            self.d_m_p +
            self.d_c_p +
            self.d_f_p +
            self.d_t_p +
            self.d_l_p +
            self.d_s_p
        )
        self.cold_drink_Price.set("Rs. " + str(self.total_drinks_Price))
        self.d_tax = round((self.total_drinks_Price * 0.05), 2)
        self.cold_drink_tax.set("Rs. " + str(self.d_tax))

        self.Total_bill = float(self.total_Meal_Price +
                                self.total_Starter_Price +
                                self.total_drinks_Price +
                                self.c_tax +
                                self.g_tax +
                                self.d_tax
                                )


    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t\tThe Blue MerMaid\t")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phon.get()} ")
        self.txtarea.insert(END, f"\n================================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n================================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        elif self.Meal_Price.get() == "Rs. 0.0" and self.Starter_Price.get() == "Rs. 0.0" and self.cold_drink_Price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            # =========Meals==============================================================
            if self.Butter_Chicken.get() != 0:
                self.txtarea.insert(END, f"\n Butter Chicken\t\t{self.Butter_Chicken.get()}\t\t{self.c_s_p}")
            if self.Paneer_Tikka.get() != 0:
                self.txtarea.insert(END, f"\n Paneer Tikka\t\t{self.Paneer_Tikka.get()}\t\t{self.c_fc_p}")
            if self.Plain_Stream_Rice.get() != 0:
                self.txtarea.insert(END, f"\n Plain Stream Rice\t\t{self.Plain_Stream_Rice.get()}\t\t{self.c_fw_p}")
            if self.Palak_Paneer.get() != 0:
                self.txtarea.insert(END, f"\n Palak_Paneer\t\t{self.Palak_Paneer.get()}\t\t{self.c_hs_p}")
            if self.Veg_Biryani.get() != 0:
                self.txtarea.insert(END, f"\n Veg Biryani\t\t{self.Veg_Biryani.get()}\t\t{self.c_hg_p}")
            if self.Roti.get() != 0:
                self.txtarea.insert(END, f"\n Roti\t\t{self.Roti.get()}\t\t{self.c_bl_p}")

            # =========Starter==============================================================
            if self.Masala_Papad.get() != 0:
                self.txtarea.insert(END, f"\n Masala Papad\t\t{self.Butter_Chicken.get()}\t\t{self.g_r_p}")
            if self.Paneer_chilli.get() != 0:
                self.txtarea.insert(END, f'\n Paneer chilli\t\t{self.Paneer_chilli.get()}\t\t{self.g_f_p}')
            if self.Mushroom_Gravy.get() != 0:
                self.txtarea.insert(END, f"\n Mushroom Gravy\t\t{self.Mushroom_Gravy.get()}\t\t{self.g_d_p}")
            if self.Paneer_65.get() != 0:
                self.txtarea.insert(END, f"\n Paneer 65\t\t{self.Paneer_65.get()}\t\t{self.g_w_p}")
            if self.Veg_Munchuriyan.get() != 0:
                self.txtarea.insert(END, f"\n Veg  Munchuriyan\t\t{self.Veg_Munchuriyan.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            # =========drinks==============================================================
            if self.maza.get() != 0:
                self.txtarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
            if self.Cock.get() != 0:
                self.txtarea.insert(END, f"\n Cock\t\t{self.Cock.get()}\t\t{self.d_c_p}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            self.txtarea.insert(END, f"\n-----------------------------------------------")

            if self.Meal_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Meal Tax\t\t\t\t{self.Meal_tax.get()}")

            if self.Starter_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Starter Tax\t\t\t\t{self.Starter_tax.get()}")

            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold drink Tax\t\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill : \t\t\t\t Rs. {str(self.Total_bill)}")
            self.txtarea.insert(END, f"\n-----------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save bill?")
        if op > 0:
            self.bill_data = self.txtarea.get("1.0", END)
            f1 = open("Customer/"+ str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no : {self.bill_no.get()}""Bill saved successfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("customer/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"customer/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.askyesno("Error", "Invalid Bill No.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:

            # ======================Meals=========================
            self.Butter_Chicken.set(0)
            self.Paneer_Tikka.set(0)
            self.Plain_Stream_Rice.set(0)
            self.Palak_Paneer.set(0)
            self.Veg_Biryani.set(0)
            self.Roti.set(0)
            # ======================Starter============================
            self.Masala_Papad.set(0)
            self.Paneer_chilli.set(0)
            self.Mushroom_Gravy.set(0)
            self.Paneer_65.set(0)
            self.Veg_Munchuriyan.set(0)
            self.tea.set(0)
            # ========================Cold drinks==========================
            self.maza.set(0)
            self.Cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # ======================Total product Price and text variables======================
            self.Meal_Price.set("")
            self.Starter_Price.set("")
            self.cold_drink_Price.set("")

            self.Meal_tax.set("")
            self.Starter_tax.set("")
            self.cold_drink_tax.set("")

            # ==========================customer================================================
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to Exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
