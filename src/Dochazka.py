from tkinter import Tk, BOTH, W, N, E, S, END, Listbox, LabelFrame, Radiobutton, IntVar, messagebox
from tkinter.ttk import Frame, Button, Label, Combobox
import src.Database as db
import src.Validation.Helper as helper
import src.Hire as hire
import src.Password as ps
from datetime import datetime


def hire_form():
    print("test")
    hire_win = Tk()
    hire_form_frame = hire.HireFrame(hire_win)
    hire_form_frame.mainloop()


class AttendanceFrame(Frame):
    def __init__(self,
                 user_log_in,
                 user_id,
                 hire_date,
                 is_employer,
                 root):
        super().__init__()
        self.root: Tk = root
        self.var = IntVar()

        self.__default_time: str = "Odchozeno hodin: "
        self.__default_wage: str = "Celková hrubá mzda: "
        self.__default_days: str = "Počet dnů: "

        self.__cb_year = Combobox(self, state="readonly")
        self.__lb_data = Listbox(self, font=('Courier New', 12))

        self.__output = LabelFrame(self, text="Výpis")
        self.__lb_time = Label(self.__output, text=self.__default_time + "0:0")
        self.__lb_wage = Label(self.__output, text=self.__default_wage + "0,00 Kč")
        self.__lb_days = Label(self.__output, text=self.__default_days + "0")

        self.__conn = db.create_connection()
        self.user_id = user_id
        self.isEmployer = is_employer
        self.hire_date: str = hire_date
        self.user_log_in: str = user_log_in

        self.__init_ui()
        self.__btn_update_event()

    def change_password_form(self):
        """Open change password form
        """
        print("change_password")
        pass_win = Tk()
        pass_form = ps.PassFrame(pass_win, self.user_id)
        pass_form.mainloop()

    def btn_entry_event(self):
        """Button event - entry presence
        """
        date_now: str = datetime.today().strftime('%Y-%m-%d')

        time_now: str = datetime.today().strftime('%H:%M')
        entry: int = self.var.get()

        if entry == 0:
            print(entry)
            # Příchod
            # Nový zápis
            # Kontrola da už je tenhle datum zapsán
            # db.exist_timeIn(self.__conn, self.user_id, date_now)
            if not db.exist_time_in(self.__conn, self.user_id, date_now):
                presence_in = (time_now, date_now, self.user_id)
                db.create_presence_in(self.__conn, presence_in)
            else:
                print("Již je zapsán příchod")
                messagebox.showwarning("Chyba zapsání příchodu!", "Již je zapsán příchod!")
        else:
            print(entry)
            if db.exist_time_in(self.__conn, self.user_id, date_now):
                if not db.exist_time_out(self.__conn, self.user_id, date_now):
                    presence_out = (time_now, date_now, self.user_id)
                    db.create_presence_out(self.__conn, presence_out)
                else:
                    print("Již je zapsán odchod")
                    messagebox.showwarning("Chyba zapsání odchodu!", "Již je zapsán odchod!")
            else:
                print("Nejdříve zapište příchod")
            # Odchod
            # Update zápisu
            # Kontrola da už je tenhle datum zapsán
        self.__btn_update_event()

    def __btn_update_event(self):
        """Button event - update user presence in listbox
        """
        user_years: list = self.get_update_month_cb
        self.__cb_year["values"] = user_years
        print("__btn_update_event")
        print(self.user_id)
        self.clear()
        year: str = self.get_year
        month: str = self.get_month
        # print("mm: " + str(month))
        p_rows: list = db.select_presence_by_user_id(self.__conn, self.user_id, year, month)
        for x in p_rows:
            print("jeje")
            print(x[1])
            data_entry = "{0} :: {1} - ".format(helper.Validation.date_convert(x[3]),
                                                helper.Validation.time_covert(x[1]))

            if x[2] is None:
                # print("none")
                # print(x[2])
                data_entry += "xx:xx"
            else:
                data_entry += helper.Validation.time_covert(x[2])
                # print(datetime.strptime(helper.Validation.time_covert(x[2]), format) - datetime.strptime(helper.Validation.time_covert(x[1]), format))
                data_entry += " >  " + str(helper.Validation.number_of_hours(x[2], x[1]))
            self.__lb_data.insert(END, data_entry)

        self.__lb_time["text"] = self.__default_time + db.select_user_time(self.__conn, self.user_id, year, month)
        self.__lb_wage["text"] = self.__default_wage + db.select_user_wage(self.__conn, self.user_id, year, month)
        self.__lb_days["text"] = self.__default_days + str(
            db.select_user_day_count(self.__conn, self.user_id, year, month))

    def clear(self):
        """Clear user data from interface
        """
        self.__lb_data.delete(0, END)
        self.__lb_time["text"] = self.__default_time + "0:0"
        self.__lb_wage["text"] = self.__default_wage + "0,00 Kč"
        self.__lb_days["text"] = self.__default_days + "0"

    @property
    def get_year(self) -> str:
        """Return year
        Returns:
            str: year
        """
        return self.__cb_year.get()

    @property
    def get_month(self) -> str:
        """Return month
        Returns:
            str: month
        """
        return self.__cb_month.get()

    def cb_month_update(self, event):
        """Update data on change
        """
        self.__btn_update_event()
        temp = self.__cb_month.get()
        print(temp)

    def cb_year_update(self, event):
        """Update data on change
        """
        self.__btn_update_event()
        temp = self.__cb_year.get()
        print(temp)

    @property
    def get_update_month_cb(self) -> list:
        """Return user years
        Returns:
            list: user years
        """
        user_years = list()

        print("userId: " + str(self.user_id))

        temp_year = db.get_presence_group_by_year_by_id(self.__conn, self.user_id)
        print("temp: " + str(len(temp_year)))
        for x in temp_year:
            print("type x")
            print(type(x))

            user_years.append(x)

        if len(temp_year) == 0:
            user_years.append("Žádný zápis")
        print(type(user_years))

        return user_years

    def __init_ui(self):
        """Create graphic interface
        """
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(6, pad=7)

        user_years: list = self.get_update_month_cb

        print(user_years)

        self.__cb_month = Combobox(self, state="readonly", values=(
            "Leden", "Únor", "Březen", "Duben", "Květen", "Červen", "Červenec", "Srpen", "Září", "Říjen", "Listopad",
            "Prosinec"))
        self.__cb_month.set(helper.Validation.get_current_month())
        self.__cb_month.bind('<<ComboboxSelected>>', self.cb_month_update)
        self.__cb_month.grid(row=1, column=0, pady=2, padx=5, sticky=W)

        self.__cb_year["values"] = user_years
        self.__cb_year.set(user_years[len(user_years) - 1])
        self.__cb_year.bind('<<ComboboxSelected>>', self.cb_year_update)
        self.__cb_year.grid(row=2, column=0, pady=2, padx=5, sticky=W)

        lb_format = Label(self, text="datum :: příchod - odchod > doba", font=('Courier New', 12))
        lb_format.grid(row=3, column=0, sticky=W, pady=4, padx=5)

        self.__lb_data.grid(row=4, column=0, columnspan=4, rowspan=1,
                            padx=5, sticky=E + W + S + N)

        lb_user = Label(self, text="Přihlášen: " + self.user_log_in)
        lb_user.grid(row=1, column=2, sticky=W, pady=4)

        btn_update = Button(self, text="Aktualizovat", command=self.__btn_update_event)
        btn_update.grid(row=1, column=3, sticky=E, padx="4")

        lb_hire = Label(self, text="Nástup: " + self.hire_date)
        lb_hire.grid(row=2, column=2, sticky=W, pady=4)

        btn_log_out = Button(self, text="Clear", command=self.clear)
        btn_log_out.grid(row=2, column=3, pady=4, sticky=E, padx="4")

        if self.isEmployer:
            btn_hire = Button(self, text="Hire", command=hire_form)
            btn_hire.grid(row=3, column=3, pady=4, sticky=E, padx="4")
        else:
            btn_change_password = Button(self, text="Změnit heslo", command=self.change_password_form)
            btn_change_password.grid(row=3, column=3, pady=4, sticky=E, padx="4")

        gb_entry = LabelFrame(self, text="Zápis")
        gb_entry.grid(row=6, padx=10, column=0, columnspan=4, rowspan=1, sticky=E + W + S + N)

        rb_entry = Radiobutton(gb_entry, text="Příchod", variable=self.var, value=0)
        rb_entry.grid(row=1, column=1, sticky=W, pady=2, padx=5)

        rb_exit = Radiobutton(gb_entry, text="Odchod", variable=self.var, value=1)
        rb_exit.grid(row=1, column=2, sticky=W, pady=2, padx=5)

        btn_entry = Button(gb_entry, text="Zapsat", command=self.btn_entry_event)
        btn_entry.grid(row=1, column=3, sticky=W, pady=2, padx=5)

        self.__output.grid(row=7, pady=10, padx=10, column=0, columnspan=4, rowspan=1, sticky=E + W + S + N)

        self.__lb_time.grid(row=1, column=1, sticky=W, pady=4, padx=5)
        self.__lb_wage.grid(row=1, column=2, sticky=W, pady=4, padx=5)
        self.__lb_days.grid(row=1, column=3, sticky=W, pady=4, padx=5)
