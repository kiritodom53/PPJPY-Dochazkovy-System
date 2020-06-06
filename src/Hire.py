from tkinter import Tk, Text, BOTH, W, N, E, S, LEFT, END, Listbox, BooleanVar, Checkbutton, LabelFrame, Radiobutton, \
    IntVar, Entry, Toplevel, font, messagebox
from tkinter.ttk import Frame, Button, Label, Style, Combobox
from tkcalendar import Calendar, DateEntry
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
        self.__init_ui()

    def registration(self):
        # Todo: Přidat dynamický datum
        print("reg")
        print(self.__username_box.get())
        print(self.__password_box.get())
        print(self.__first_name_box.get())
        print(self.__surname_box.get())
        print(self.__cal.get())
        print("okok")
        print(self.__wage_box.get())
        if not db.user_exist(self.conn, self.__username_box.get()):
            hire_user = (
                self.__username_box.get(),
                self.__password_box.get(),
                self.__first_name_box.get(),
                self.__surname_box.get(),
                "26.01.2019", int(self.__wage_box.get()))
            db.hire_user(self.conn, hire_user)
        else:
            print("Již je registrován uživatel")
            messagebox.showwarning("Chyba zapsání příchodu!",
                                   "Již je registrován uživatel!")

    def __init_ui(self):
        lb_description = Label(self.root,
                               text="Registrace zaměstnance:")
        lb_description.grid(row=0,
                            column=1,
                            pady=5)

        lb_username = Label(self.root,
                            text="Username:")
        lb_username.grid(row=1,
                         column=2,
                         pady=5)

        lb_password = Label(self.root,
                            text="Password:")
        lb_password.grid(row=2,
                         column=2,
                         pady=5)

        lb_first_name = Label(self.root,
                              text="Name:")
        lb_first_name.grid(row=3,
                           column=2,
                           pady=5)

        lb_surname = Label(self.root,
                           text="Surname:")
        lb_surname.grid(row=4,
                        column=2,
                        pady=5)

        lb_hire_date = Label(self.root,
                             text="Hire date:")
        lb_hire_date.grid(row=5,
                          column=2,
                          pady=5)

        lb_wage_per_hour = Label(self.root,
                                 text="Wage /h:")
        lb_wage_per_hour.grid(row=6,
                              column=2,
                              pady=5)

        # Creating Buttons

        btn_hire = Button(self.root,
                          text="Hire!",
                          command=self.registration)
        btn_hire.grid(row=8,
                      pady=5,
                      column=2,
                      columnspan=2)
        # btn_hire(relx=0.440, rely=0.638, height=30, width=60)
        # btn_hire.configure(command=self.login_user)
        #
        # self.login_completed = IntVar()
        #
        # self.exit_button = Button(self.root, text="Exit")  # , command=master.quit)
        # self.exit_button.place(relx=0.614, rely=0.638, height=30, width=60)
        # self.exit_button.configure(command=self.exit_login)

        # Creating entry boxes

        self.__username_box = Entry(self.root)
        # self.__username_box.place(relx=0.440, rely=0.298, height=20, relwidth=0.35)
        self.__username_box.grid(row=1,
                                 column=3)

        self.__first_name_box = Entry(self.root)
        self.__first_name_box.grid(row=3,
                                   column=3)

        self.__surname_box = Entry(self.root)
        self.__surname_box.grid(row=4,
                                column=3)

        self.__password_box = Entry(self.root)
        self.__password_box.grid(row=2,
                                 column=3)
        self.__password_box.configure(show="*")
        self.__password_box.configure(background="white")

        self.__cal = DateEntry(self.root,
                               width=17,
                               bg="darkblue",
                               fg="white",
                               year=2010)
        self.__cal.grid(row=5,
                        column=3)

        self.__wage_box = Entry(self.root)
        self.__wage_box.grid(row=6,
                             column=3)
