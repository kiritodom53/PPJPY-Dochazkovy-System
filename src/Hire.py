from tkinter import Tk, Text, BOTH, W, N, E, S, LEFT, END, Listbox, BooleanVar, Checkbutton, LabelFrame, Radiobutton, IntVar, Entry, Toplevel, font, messagebox
from tkinter.ttk import Frame, Button, Label, Style, Combobox
from tkcalendar import Calendar,DateEntry
import src.Database as db

class HireFrame(Frame):
    def __init__(self, root):
        super().__init__()
        self.root = root
        root.title("Hire")
        root.geometry("450x270+450+170")
        root.minsize(450, 270)
        root.maxsize(450, 270)
        self.var = BooleanVar()
        self.conn = db.create_connection()
        self.initUI()

    def registr(self):
        print("reg")
        print(self.username_box.get())
        print(self.password_box.get())
        print(self.first_name_box.get())
        print(self.surname_box.get())
        print(self.cal.get())
        print("okok")
        print(self.wage_box.get())
        if (db.user_exist(self.conn, self.username_box.get()) == False):
            hire_user = (self.username_box.get(),
                           self.password_box.get(),
                           self.first_name_box.get(),
                           self.surname_box.get(),
                           "26.01.2019",
                           int(self.wage_box.get()))
            # h = ("q", "q", "q", "q", "26.01.2019", 53)
            db.hire_user(self.conn, hire_user)
        else:
            print("Již je registrován uživatel")
            messagebox.showwarning("Chyba zapsání příchodu!", "Již je registrován uživatel!")

    def initUI(self):
        self.popis_lbl = Label(self.root, text="Registrace zaměstnance:")
        self.popis_lbl.grid(row=0, column=1, pady=5)

        self.username = Label(self.root, text="Username:")
        # self.username.place(relx=0.285, rely=0.298, height=20, width=60)
        self.username.grid(row=1, column=2, pady=5)

        self.password = Label(self.root, text="Password:")
        # self.password.place(relx=0.285, rely=0.468, height=20, width=60)
        self.password.grid(row=2, column=2, pady=5)

        self.firstName = Label(self.root, text="Name:")
        # self.firstName.place(relx=0.285, rely=0.638, height=20, width=60)
        self.firstName.grid(row=3, column=2, pady=5)

        self.surname = Label(self.root, text="Surname:")
        # self.surname.place(relx=0.285, rely=0.808, height=20, width=60)
        self.surname.grid(row=4, column=2, pady=5)

        self.hireDate = Label(self.root, text="Hire date:")
        # self.hireDate.place(relx=0.285, rely=0.978, height=20, width=60)
        self.hireDate.grid(row=5, column=2, pady=5)

        self.wagePerHour = Label(self.root, text="Wage /h:")
        # self.surname.place(relx=0.285, rely=0.1148, height=20, width=60)
        self.wagePerHour.grid(row=6, column=2, pady=5)

        # Creating Buttons

        self.hire_button = Button(self.root, text="Hire!", command=self.registr)
        self.hire_button.grid(row=8, column=2, columnspan=2, pady=5)
        # self.hire_button(relx=0.440, rely=0.638, height=30, width=60)
        # self.hire_button.configure(command=self.login_user)
        #
        # self.login_completed = IntVar()
        #
        # self.exit_button = Button(self.root, text="Exit")  # , command=master.quit)
        # self.exit_button.place(relx=0.614, rely=0.638, height=30, width=60)
        # self.exit_button.configure(command=self.exit_login)

        # Creating entry boxes

        self.username_box = Entry(self.root)
        # self.username_box.place(relx=0.440, rely=0.298, height=20, relwidth=0.35)
        self.username_box.grid(row=1, column=3)

        self.password_box = Entry(self.root)
        # self.password_box.place(relx=0.440, rely=0.468, height=20, relwidth=0.35)
        self.password_box.grid(row=2, column=3)
        self.password_box.configure(show="*")
        self.password_box.configure(background="white")

        self.first_name_box = Entry(self.root)
        self.first_name_box.grid(row=3, column=3)

        self.surname_box = Entry(self.root)
        self.surname_box.grid(row=4, column=3)

        self.cal = DateEntry(self.root, width=17, bg="darkblue", fg="white", year=2010)
        self.cal.grid(row=5, column=3)

        self.wage_box = Entry(self.root)
        self.wage_box.grid(row=6, column=3)