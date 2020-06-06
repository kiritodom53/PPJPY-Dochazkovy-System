import src.Data.SeedData as sd
import src.Database as db
import src.LoginForm as lg
from tkinter import Tk
import src.DochazkaForm as td


class Boot:
    def startup_config(self):
        if (db.check_database() == False):
            print(db.check_database())
            db.create_database()

        conn = db.create_connection()
        users = db.check_tables(conn, "users")
        presence = db.check_tables(conn, "presence")

        # Vytvoří tabulky, pokud neexistují
        if (users == False or presence == False):
            print("main")
            db.create_tables()
            print("seed data - start")
            sd.main()
            print("seed data - end")
            print("start dochazka")

    def login(self):
        login_page = lg.Login_Page()  # I dont need to pass the root now since its initialized inside the class
        login_page.mainloop_window()
        return login_page

    def main(self):
        self.startup_config()
        lp = self.login()

        main_win = MainWin(lp.get_user_name(), lp.get_user_id(), lp.get_hire_date(), lp.is_employer())
        main_win.mainloop_window()


class MainWin:
    def __init__(self, user, userId, nastup, isEmployer):
        main_win = Tk()
        self.main_win = main_win
        main_win.title("Docházkový systém MANDINEC - ")
        main_win.protocol("WM_DELETE_WINDOW", self.event_X)
        main_win.geometry("700x500")
        main_win.minsize(700, 500)
        app = td.Example(user, userId, nastup, isEmployer, main_win)

    def event_X(self):
        exit()

    def mainloop_window(self):  # This is the class function that helps me to mainloop the window
        self.main_win.mainloop()


if __name__ == '__main__':
    boot = Boot()
    boot.main()
