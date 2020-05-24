from tkinter import Tk, Label, Button, messagebox
from tkinter import *
import Version.v01.DochazkaForm as td
import Version.v01.Database as db
import Version.v01.LoginForm as lg

##### Login Page #####

qq = None
userId = None



login_page = lg.Login_Page()# I dont need to pass the root now since its initialized inside the class
login_page.mainloop_window()  # Just mainlooping the authentication window
userId = login_page.get_user()
qq = login_page.get_user_name()

print("testloginform")
print(userId)
print(login_page.get_user_name())
    ##### Main Window #####


class Main_Win:
    def __init__(self, main_win=Tk()):  # This is my first change so i already initialize a Tk window inside the class
        self.main_win = main_win
        main_win.title("Docházkový systém MANDINEC - " + qq)
        main_win.geometry("500x500")
        app = td.Example(qq,userId)
        #main_win.geometry("900x500+250+130")


    def mainloop_window(self):  # This is the class function that helps me to mainloop the window
        self.main_win.mainloop()


main_win = Main_Win()  # I dont need to pass the root now since its initialized inside the class
main_win.mainloop_window()  # Just mainlooping the authentication window