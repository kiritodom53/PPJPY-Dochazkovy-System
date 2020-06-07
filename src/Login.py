from tkinter import Tk, Label, Button, Entry, IntVar, Checkbutton, messagebox
import src.Database as db

class LoginPage:

    def __init__(self, login=Tk()):  # This is my first change so i already initialize a Tk window inside the class
        """
        :type login: object
        """
        self.user: str
        self.user_id: int
        self.hire: str
        self.isEmployer: int
        self.__login = login
        self.__login.protocol("WM_DELETE_WINDOW", self.__event_x)
        self.__login.title("Login - Docházkový systém MANDINEC 1.0")
        self.__login.geometry("450x230+450+170")
        self.__init_ui()

    def __init_ui(self):
        """Create graphic interface
        """
        self.username = Label(self.__login, text="Username:")
        self.username.place(relx=0.285, rely=0.298, height=20, width=55)

        self.password = Label(self.__login, text="Password:")
        self.password.place(relx=0.285, rely=0.468, height=20, width=55)

        self.login_button = Button(self.__login, text="Login")
        self.login_button.place(relx=0.440, rely=0.638, height=30, width=60)
        self.login_button.configure(command=self.login_user)

        self.login_completed = IntVar()

        self.exit_button = Button(self.__login, text="Exit")  # , command=master.quit)
        self.exit_button.place(relx=0.614, rely=0.638, height=30, width=60)
        self.exit_button.configure(command=self.exit_login)

        self.username_box = Entry(self.__login)
        self.username_box.place(relx=0.440, rely=0.298, height=20, relwidth=0.35)

        self.password_box = Entry(self.__login)
        self.password_box.place(relx=0.440, rely=0.468, height=20, relwidth=0.35)
        self.password_box.configure(show="*")
        self.password_box.configure(background="white")

        self.var = IntVar()
        self.show_password = Checkbutton(self.__login)
        self.show_password.place(relx=0.285, rely=0.650, relheight=0.100, relwidth=0.125)
        self.show_password.configure(justify='left')
        self.show_password.configure(text='''Show''')
        self.show_password.configure(variable=self.var, command=self.__cb)

    def __event_x(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            exit()

    def __cb(self, ):
        if self.var.get():
            self.password_box.configure(show="")
        else:
            self.password_box.configure(show="*")

    # Giving function to login process

    def login_user(self):
        """Login user
        """
        name = self.username_box.get()
        password = self.password_box.get()
        # login_completed = self.login_completed.get()

        # AUTO DATA PRO TESTOVÁNÍ
        name = "dom53"
        password = "admin"

        conn = db.create_connection()
        # us = db.select_user_by_id(conn, 1)
        # row = db.select_user_by_id(conn, 1)[0]
        row = db.select_user_by_credentials(conn, name, password)[0]

        print("name: " + name)
        print("password: " + password)
        print("row[1]: " + row[1])
        print("row[2]: " + row[2])
        # global qq
        # global userId
        # global hire
        # global isEmployer
        self.user = row[3] + " " + row[4]
        self.user_id = row[0]
        self.hire = row[5]
        self.isEmployer = row[7]
        print("tady typy")
        print(type(self.user))
        print(type(self.user_id))
        print(type(self.hire))
        print(type(self.isEmployer))
        print("isEmployer")
        print(self.isEmployer)

        # print ToDo: Hashovat heslo
        # Potom zapnout
        if name == row[1] and password == row[2]:

            # Potom zapnout
            # messagebox.showinfo("Login page", "Login successful!")
            self.__login.destroy()  # Removes the toplevel window
            # self.main_win.deiconify() #Unhides the root window
            # self.login_completed == 1


        # Potom zapnout
        else:
            messagebox.showwarning("Login Failed - Acess Denied", "Username or Password incorrect!")

        # return

    @property
    def get_user_id(self) -> int:
        """Return user id
        Returns:
            user id
        """
        return self.user_id

    @property
    def get_user_name(self) -> str:
        """Return username
        Returns:
            username
        """
        print("no co")
        print(self.user)
        return self.user

    @property
    def get_hire_date(self) -> str:
        """Return hire date
        Returns:
            hire date
        """
        return self.hire

    @property
    def is_employer(self) -> int:
        """Return if user is employer
        Returns:
            True if user is employer otherwise False
        """
        return self.isEmployer

    # def hire_user(self):
    #     print("hire user")

    def exit_login(self):
        msg = messagebox.askyesno("Exit login page", "Do you really want to exit?")
        if msg:
            exit()

    def mainloop_window(self):
        """Function that helps me to mainloop the window
        """
        self.__login.mainloop()
