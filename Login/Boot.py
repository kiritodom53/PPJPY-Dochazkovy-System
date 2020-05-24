from tkinter import Tk, Label, Button, messagebox
from tkinter import *
import Login.DochazkaForm as td

##### Login Page #####

class Login_Page:

    def __init__(self, login=Tk()):  # This is my first change so i already initialize a Tk window inside the class
        """

        :type login: object
        """
        self.login = login
        login.protocol("WM_DELETE_WINDOW",self.event_X)
        login.title("Login - Docházkový systém MANDINEC 1.0")
        login.geometry("450x230+450+170")

    # Creating describtioneves

        self.username = Label(login, text="Username:")
        self.username.place(relx=0.285, rely=0.298, height=20, width=55)

        self.password = Label(login, text="Password:")
        self.password.place(relx=0.285, rely=0.468, height=20, width=55)

        # Creating Buttons

        self.login_button = Button(login, text="Login")
        self.login_button.place(relx=0.440, rely=0.638, height=30, width=60)
        self.login_button.configure(command=self.login_user)

        self.login_completed = IntVar()

        self.exit_button = Button(login, text="Exit")  # , command=master.quit)
        self.exit_button.place(relx=0.614, rely=0.638, height=30, width=60)
        self.exit_button.configure(command=self.exit_login)

        # Creating entry boxes

        self.username_box = Entry(login)
        self.username_box.place(relx=0.440, rely=0.298, height=20, relwidth=0.35)

        self.password_box = Entry(login)
        self.password_box.place(relx=0.440, rely=0.468, height=20, relwidth=0.35)
        self.password_box.configure(show="*")
        self.password_box.configure(background="white")

        # Creating checkbox

        self.var = IntVar()
        self.show_password = Checkbutton(login)
        self.show_password.place(relx=0.285, rely=0.650, relheight=0.100, relwidth=0.125)
        self.show_password.configure(justify='left')
        self.show_password.configure(text='''Show''')
        self.show_password.configure(variable=self.var, command=self.cb)

    def event_X(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            exit()

    def cb(self, ):
        if self.var.get() == True:
            self.password_box.configure(show="")
        else:
            self.password_box.configure(show="*")


# Giving function to login process

    def login_user(self):
        name = self.username_box.get()
        password = self.password_box.get()
        login_completed = self.login_completed.get()

        if name == "" and password == "":
            # messagebox.showinfo("Login page", "Login successful!")
            self.login.destroy()  # Removes the toplevel window
            # self.main_win.deiconify() #Unhides the root window
            self.login_completed == 1

        else:
            messagebox.showwarning("Login Failed - Acess Denied", "Username or Password incorrect!")

        # return


    def exit_login(self):
        msg = messagebox.askyesno("Exit login page", "Do you really want to exit?")
        if (msg):
            exit()


    def mainloop_window(self):  # This is the class function that helps me to mainloop the window
        self.login.mainloop()


login_page = Login_Page()  # I dont need to pass the root now since its initialized inside the class
login_page.mainloop_window()  # Just mainlooping the authentication window


    ##### Main Window #####


class Main_Win:
    def __init__(self, main_win=Tk()):  # This is my first change so i already initialize a Tk window inside the class
        self.main_win = main_win
        main_win.title("Docházkový systém MANDINEC")
        main_win.geometry("500x500")
        app = td.Example()
        #main_win.geometry("900x500+250+130")


    def mainloop_window(self):  # This is the class function that helps me to mainloop the window
        self.main_win.mainloop()


main_win = Main_Win()  # I dont need to pass the root now since its initialized inside the class
main_win.mainloop_window()  # Just mainlooping the authentication window