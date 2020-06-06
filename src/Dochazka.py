from tkinter import Tk, Label, Button, messagebox
from tkinter import *
import src.DochazkaForm as td
import src.Database as db
import src.LoginForm as lg

##### Login Page #####

qq = None
userId = None

login_page = lg.Login_Page()  # I dont need to pass the root now since its initialized inside the class
login_page.mainloop_window()
# Just mainlooping the authentication window
userId = login_page.get_user_id()
qq = login_page.get_user_name()
nastup = login_page.get_hire_date()
isEmployer = login_page.is_employer()

print("testloginform")
print(userId)
print(login_page.get_user_name())
    ##### Main Window #####


class Main_Win:
    def __init__(self, main_win=Tk()):  # This is my first change so i already initialize a Tk window inside the class
        self.main_win = main_win
        main_win.title("Docházkový systém MANDINEC - ")
        main_win.protocol("WM_DELETE_WINDOW", self.event_X)
        main_win.geometry("700x500")
        main_win.minsize(700, 500)
        app = td.Example(qq, userId, nastup, isEmployer, main_win)
        #main_win.geometry("900x500+250+130")

    def event_X(self):
        exit()

    def mainloop_window(self):  # This is the class function that helps me to mainloop the window
        self.main_win.mainloop()


main_win = Main_Win()  # I dont need to pass the root now since its initialized inside the class
main_win.mainloop_window()  # Just mainlooping the authentication window