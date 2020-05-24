from tkinter import Tk, Text, BOTH, W, N, E, S, LEFT, Listbox, LabelFrame, Radiobutton, IntVar, Toplevel
from tkinter.ttk import Frame, Button, Label, Style, Combobox


# Tk, Text, BOTH, W, N, E, S, Listbox, LabelFrame, Radiobutton, IntVar

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def update(self):
        print("btnUpdate")

    def initUI(self):
        self.master.title("Docházkový systém")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        # all_comboboxes = []
        # self.cb = Combobox(self, values=("A", "B", "C", "D", "E"))
        # self.cb.set("A")
        ##self.cb.pack()
        # self.cb.bind('<<ComboboxSelected>>', self.on_select)
        # all_comboboxes.append(self.cb)

        # cb2 = Combobox(self, values=("A", "B", "C", "D", "E"))
        # cb2.set("A")
        # cb2.grid(sticky=W, pady=6, padx=6)

        lblMonth = Label(self, text="Měsíc:")
        lblMonth.grid(row=1, column=0, sticky=W, pady=4, padx=5)

        cbMonth = Combobox(self, values=(
        "Leden", "Únor", "Březen", "Duben", "Květen", "Červen", "Červenec", "Srpen", "Září", "Říjen", "Listopad",
        "Prosinec"))
        cbMonth.set("Leden")
        cbMonth.grid(row=1, column=1, sticky=W, pady=2, padx=50)

        lblYear = Label(self, text="Rok:")
        lblYear.grid(row=2, column=0, sticky=W, pady=4, padx=5)

        cbYear = Combobox(self, values=("A", "B", "C", "D", "E"))
        cbYear.set("A")
        cbYear.grid(row=2, column=1, sticky=W, pady=2, padx=50)

        # area = Text(self)
        # area.grid(row=3, column=0, columnspan=2, rowspan=4,
        #    padx=5, sticky=E+W+S+N)

        lb = Listbox(self)
        lb.grid(row=3, column=0, columnspan=4, rowspan=1,
                padx=5, sticky=E + W + S + N)

        lblUser = Label(self, text="Uživatel:")
        lblUser.grid(row=1, column=2, sticky=W, pady=4)

        btnUpdate = Button(self, text="Aktualizovat", command=self.update)
        btnUpdate.grid(row=1, column=3, sticky=E)

        btnLogOut = Button(self, text="Odhlásit se")
        btnLogOut.grid(row=2, column=3, pady=4, sticky=E)

        gbZapis = LabelFrame(self, text="Zápis")
        gbZapis.grid(row=5, padx=10, column=0, columnspan=4, rowspan=1, sticky=E + W + S + N)

        var = IntVar()
        rbPrichod = Radiobutton(gbZapis, text="Příchod", variable=var, value=1)
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


