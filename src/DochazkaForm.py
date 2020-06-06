from tkinter import Tk, Text, BOTH, W, N, E, S, LEFT, END, Listbox, Checkbutton, LabelFrame, Radiobutton, IntVar, Entry, Toplevel, font, messagebox
from tkinter.ttk import Frame, Button, Label, Style, Combobox
from tkcalendar import Calendar,DateEntry
import src.Database as db
import src.Validation.Helper as helper
import src.Hire as hire
import src.Password as ps
from datetime import datetime
import time
# import Version.v01.TestForm as tf


# Tk, Text, BOTH, W, N, E, S, Listbox, LabelFrame, Radiobutton, IntVar

class Example(Frame):
    def __init__(self, usr, userId, nastupp, isEmployer, root):
        super().__init__()
        u = usr
        self.root = root
        self.var = IntVar()
        self.lbData = Listbox(self, font=('Courier New', 12))
        self.vypis = LabelFrame(self, text="Výpis")
        self.odchozenoHodin = "Odchozeno hodin: 0:0"
        self.celkovaMzda = "Celková hrubá mzda: 0,00 Kč"
        self.pocetDnu = "Počet dnů: 0"
        self.cbYear = Combobox(self, state="readonly")
        self.lblHodiny = Label(self.vypis, text=self.odchozenoHodin)
        self.lblMzda = Label(self.vypis, text=self.celkovaMzda)
        self.lblPocetDnu = Label(self.vypis, text=self.pocetDnu)
        self.conn = db.create_connection()
        self.user_id = userId
        self.isEmployer = isEmployer
        self.odchozeno = "Odchozeno:"
        self.nastup = "Nástup: " + nastupp
        self.userLogIn = "Přihlášen: " + usr
        self.initUI()
        self.btnUpdateEvent()

#=======================================================================================================================
#======================================================REGISTRACE=======================================================
#=======================================================================================================================

    def cb(self, ):
        if self.var.get() == True:
            self.password_box.configure(show="")
        else:
            self.password_box.configure(show="*")

    def open_test_form(self):
        print("test")
        # hire_win = Tk()
        # hire_form = hire.HireFrame(hire_win)
        # hire_form.mainloop()


    def change_password(self):
        print("change_password")
        pass_win = Tk()
        pass_form = ps.PassFrame(pass_win, self.user_id)
        pass_form.mainloop()
        # 3x TextBox - (old password, new password, confirm password)
        # 1x Button - submit


    def btnZapsatEvent(self):
        date_now = datetime.today().strftime('%Y-%m-%d')
        time_now = datetime.today().strftime('%H:%M')
        # print("______________")
        # print("btnZapsatEvent")
        # print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        # print("typ zápisu: ", self.var.get())
        # print("datum: ", date_now)
        # print("time: ", time_now)
        # print("userId", self.user_id)

        zapis = self.var.get()

        if (zapis == 0):
            print(zapis)
            # Příchod
            # Nový zápis
            # Kontrola da už je tenhle datum zapsán
            # db.exist_timeIn(self.conn, self.user_id, date_now)
            if(db.exist_timeIn(self.conn, self.user_id, date_now) == False):
                presence_in = (time_now, date_now, self.user_id)
                db.create_presence_in(self.conn, presence_in)
            else:
                print("Již je zapsán příchod")
                messagebox.showwarning("Chyba zapsání příchodu!", "Již je zapsán příchod!")
        else:
            print(zapis)
            if(db.exist_timeIn(self.conn, self.user_id, date_now) == True):
                if (db.exist_timeOut(self.conn, self.user_id, date_now) == False):
                    presence_out = (time_now, date_now, self.user_id)
                    db.create_presence_out(self.conn, presence_out)
                else:
                    print("Již je zapsán odchod")
                    messagebox.showwarning("Chyba zapsání odchodu!", "Již je zapsán odchod!")
            else:
                print("Nejdříve zapište příchod")
            # Odchod
            # Update zápisu
            # Kontrola da už je tenhle datum zapsán
        self.btnUpdateEvent()


    def btnUpdateEvent(self):
        user_years = self.get_update_mesic_cb()
        self.cbYear["values"] = user_years
        print("btnUpdateEvent")
        print(self.user_id)
        self.clear()
        year = self.get_year()
        month = self.get_month()
        # print("mm: " + str(month))
        p_rows = db.select_presence_by_user_id(self.conn, self.user_id, year, month)
        for x in p_rows:
            print("jeje")
            print(x[1])
            vstup = helper.Validation.date_convert(x[3]) \
                    + " :: " \
                    + helper.Validation.time_covert(x[1]) \
                    + " - "


            if (x[2] is None):
                # print("none")
                # print(x[2])
                vstup += "xx:xx"
            else:
                vstup += helper.Validation.time_covert(x[2])
                # print(datetime.strptime(helper.Validation.time_covert(x[2]), format) - datetime.strptime(helper.Validation.time_covert(x[1]), format))
                vstup += " >  " + str(helper.Validation.pocet_hodin(x[2], x[1]))
            self.lbData.insert(END, vstup)

        self.odchozenoHodin = db.select_user_time(self.conn, self.user_id, year, month)
        self.celkovaMzda = db.select_user_mzda(self.conn, self.user_id, year, month)
        self.pocetDnu = db.select_user_day_count(self.conn, self.user_id, year, month)


        self.lblHodiny["text"] = "Odchozeno hodin: " + self.odchozenoHodin
        self.lblMzda["text"] = "Celková hrubá mzda: " + self.celkovaMzda
        self.lblPocetDnu["text"] = "Počet dnů: " + str(self.pocetDnu)



    def clear(self):
        self.lbData.delete(0, END)
        self.lblHodiny["text"] = "Odchozeno hodin: 0:0"
        self.lblMzda["text"] = "Celková hrubá mzda: 0,00 Kč"
        self.lblPocetDnu["text"] = "Počet dnů: 0"

    def get_year(self):
        return self.cbYear.get()

    def get_month(self):
        return self.cbMonth.get()

    def cb_month_update(self, event):
        self.btnUpdateEvent()
        temp = self.cbMonth.get()
        print(temp)

    def cb_year_update(self, event):
        self.btnUpdateEvent()
        temp = self.cbYear.get()
        print(temp)

    def get_update_mesic_cb(self):
        user_years = list()

        print("userId: " + str(self.user_id))

        temp_year = db.get_presence_groupby_year_by_id(self.conn, self.user_id)
        print("temp: " + str(len(temp_year)))
        for x in temp_year:
            # print(x)
            user_years.append(x)

        if (len(temp_year) == 0):
            user_years.append("Žádný zápis")

        return user_years

    def initUI(self):
        #self.master.title("Docházkový systém")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(6, pad=7)

        # lblMonth = Label(self, text="Měsíc:")
        # lblMonth.grid(row=1, column=0, sticky=W, pady=4, padx=5)

        user_years = self.get_update_mesic_cb()
        print(user_years)
        # user_years = list()
        #
        #
        # print("userId: " + str(self.user_id))
        #
        # temp_year = db.get_presence_groupby_year_by_id(self.conn, self.user_id)
        # print("temp: " + str(len(temp_year)))
        # for x in temp_year:
        #     print(x)
        #     user_years.append(x)
        #
        # if(len(temp_year) == 0):
        #     user_years.append("Žádný zápis")

        # for x in user_years:
        #     print("---")
        #     print(x)

        self.cbMonth = Combobox(self, state="readonly", values=(
            "Leden", "Únor", "Březen", "Duben", "Květen", "Červen", "Červenec", "Srpen", "Září", "Říjen", "Listopad",
            "Prosinec"))
        self.cbMonth.set("Leden")
        self.cbMonth.bind('<<ComboboxSelected>>', self.cb_month_update)
        self.cbMonth.grid(row=1, column=0, pady=2, padx = 5, sticky=W)

        # lblYear = Label(self, text="Rok:")
        # lblYear.grid(row=2, column=0, sticky=W, pady=4, padx=5)

        self.cbYear["values"] = user_years
        self.cbYear.set(user_years[0])
        self.cbYear.bind('<<ComboboxSelected>>', self.cb_year_update)
        self.cbYear.grid(row=2, column=0, pady=2, padx=5, sticky=W)

        #13.04.2021 :: 17:43 - 11:34
        lblFormat = Label(self, text="datum :: příchod - odchod > doba", font=('Courier New', 12))
        # lblFormat = Label(self, text="DD.MM.YYYY :: HH:MM - HH:MM >", font=('Courier New', 12))
        lblFormat.grid(row=3, column=0, sticky=W, pady=4, padx=5)

        self.lbData.grid(row=4, column=0, columnspan=4, rowspan=1,
                padx=5, sticky=E + W + S + N)

        lblUser = Label(self, text=self.userLogIn)
        lblUser.grid(row=1, column=2, sticky=W, pady=4)

        btnUpdate = Button(self, text="Aktualizovat", command=self.btnUpdateEvent)
        btnUpdate.grid(row=1, column=3, sticky=E, padx="4")

        lblHire = Label(self, text=self.nastup)
        lblHire.grid(row=2, column=2, sticky=W, pady=4)

        # lblOdchozeno = Label(self, text="odchozeno", font=('Courier New', 12))
        # lblOdchozeno.grid(row=3, column=2, sticky=W, pady=4, padx=5)

        btnLogOut = Button(self, text="Clear", command=self.clear)
        btnLogOut.grid(row=2, column=3, pady=4, sticky=E, padx="4")

        if(self.isEmployer):
            btnHire = Button(self, text="Hire", command=self.open_test_form)
            btnHire.grid(row=3, column=3, pady=4, sticky=E, padx="4")
        else:
            btnChangePassword = Button(self, text="Změnit heslo", command=self.change_password)
            btnChangePassword.grid(row=3, column=3, pady=4, sticky=E, padx="4")

        gbZapis = LabelFrame(self, text="Zápis")
        gbZapis.grid(row=6, padx=10, column=0, columnspan=4, rowspan=1, sticky=E + W + S + N)

        rbPrichod = Radiobutton(gbZapis, text="Příchod", variable=self.var, value=0)
        rbPrichod.grid(row=1, column=1, sticky=W, pady=2, padx=5)
        # t1.pack()

        rbOdchod = Radiobutton(gbZapis, text="Odchod", variable=self.var, value=1)
        rbOdchod.grid(row=1, column=2, sticky=W, pady=2, padx=5)
        # t2.pack(side=LEFT)

        btnZapsat = Button(gbZapis, text="Zapsat", command=self.btnZapsatEvent)
        btnZapsat.grid(row=1, column=3, sticky=W, pady=2, padx=5)

        self.vypis.grid(row=7, pady=10, padx=10, column=0, columnspan=4, rowspan=1, sticky=E + W + S + N)

        self.lblHodiny.grid(row=1, column=1, sticky=W, pady=4, padx=5)
        self.lblMzda.grid(row=1, column=2, sticky=W, pady=4, padx=5)
        self.lblPocetDnu.grid(row=1, column=3, sticky=W, pady=4, padx=5)


