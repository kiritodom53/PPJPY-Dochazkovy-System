from tkinter import Tk, Text, BOTH, W, N, E, S, LEFT, END, Listbox, LabelFrame, Radiobutton, IntVar, Toplevel
from tkinter.ttk import Frame, Button, Label, Style, Combobox
import Version.v01.Database as db


# Tk, Text, BOTH, W, N, E, S, Listbox, LabelFrame, Radiobutton, IntVar

class Example(Frame):
    def __init__(self, usr, userId):
        super().__init__()
        u = usr
        self.lb = Listbox(self)
        self.conn = db.create_connection()
        self.user_id = userId
        self.userLogIn = "Přihlášen: " + usr
        self.initUI()

    def btnUpdateEvent(self):
        print("btnUpdateEvent")
        print(self.user_id)
        self.clear()
        p_rows = db.select_presence_by_user_id(self.conn, self.user_id)
        for x in p_rows:
            print(x)
            self.lb.insert(END, x)

    def clear(self):
        self.lb.delete(0, END)


    def cb_month_update(self, event):
        print(self.cbMonth.get())

    def initUI(self):
        #self.master.title("Docházkový systém")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lblMonth = Label(self, text="Měsíc:")
        lblMonth.grid(row=1, column=0, sticky=W, pady=4, padx=5)

        user_years = list()


        print("userId: " + str(self.user_id))

        temp_year = db.get_presence_groupby_year_by_id(self.conn, self.user_id)
        print("temp: " + str(len(temp_year)))
        for x in temp_year:
            print(x)
            user_years.append(x)

        # for x in user_years:
        #     print("---")
        #     print(x)

        self.cbMonth = Combobox(self, state="readonly", values=(
            "Leden", "Únor", "Březen", "Duben", "Květen", "Červen", "Červenec", "Srpen", "Září", "Říjen", "Listopad",
            "Prosinec"))
        self.cbMonth.set("Leden")
        self.cbMonth.bind('<<ComboboxSelected>>', self.cb_month_update)
        self.cbMonth.grid(row=1, column=1, sticky=W, pady=2, padx=50)

        lblYear = Label(self, text="Rok:")
        lblYear.grid(row=2, column=0, sticky=W, pady=4, padx=5)

        cbYear = Combobox(self, state="readonly", values=user_years)
        cbYear.set(user_years[0])
        cbYear.grid(row=2, column=1, sticky=W, pady=2, padx=50)

        # area = Text(self)
        # area.grid(row=3, column=0, columnspan=2, rowspan=4,
        #    padx=5, sticky=E+W+S+N)


        # for item in [u"jedna", u"dva", u"tři", u"čtyři"]:
        #     lb.insert(END, item)
        self.lb.grid(row=3, column=0, columnspan=4, rowspan=1,
                padx=5, sticky=E + W + S + N)

        lblUser = Label(self, text=self.userLogIn)
        lblUser.grid(row=1, column=2, sticky=W, pady=4)

        btnUpdate = Button(self, text="Aktualizovat", command=self.btnUpdateEvent)
        btnUpdate.grid(row=1, column=3, sticky=E, padx="4")

        btnLogOut = Button(self, text="Clear", command=self.clear)
        btnLogOut.grid(row=2, column=3, pady=4, sticky=E, padx="4")

        gbZapis = LabelFrame(self, text="Zápis")
        gbZapis.grid(row=5, padx=10, column=0, columnspan=4, rowspan=1, sticky=E + W + S + N)

        var = IntVar()
        rbPrichod = Radiobutton(gbZapis, text="Příchod", variable=var, value=0)
        rbPrichod.grid(row=1, sticky=W, pady=2, padx=0)
        # t1.pack()

        rbOdchod = Radiobutton(gbZapis, text="Odchod", variable=var, value=1)
        rbOdchod.grid(row=1, sticky=W, pady=2, padx=80)
        # t2.pack(side=LEFT)

        btnZapsat = Button(gbZapis, text="Zapsat")
        btnZapsat.grid(row=1, sticky=W, pady=2, padx=160)

        vypis = LabelFrame(self, text="Výpis")
        vypis.grid(row=6, pady=10, padx=10, column=0, columnspan=4, rowspan=1, sticky=E + W + S + N)

        lblHodiny = Label(vypis, text="Odchozeno hodin:")
        lblHodiny.grid(row=1, sticky=W, pady=4, padx=5)

        lblMzda = Label(vypis, text="Vydělaná mzda:")
        lblMzda.grid(row=1, sticky=W, pady=4, padx=155)

        # obtn = Button(self, text="OK")
        # obtn.grid(row=5, column=3)


