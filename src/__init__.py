import src.Data.SeedData as sd
import src.Database as db
import src.Login as lg
from tkinter import Tk
import src.Dochazka as td


def startup_config():
    print("STARTUP - CONFIG")
    if not db.check_database():
        print(db.check_database())
        db.create_database()

    conn = db.create_connection()
    users = db.check_tables(conn, "users")
    presence = db.check_tables(conn, "presence")

    # Vytvoří tabulky, pokud neexistují
    if users is False or presence is False:
        print("main")
        db.create_tables()
        print("seed data - start")
        sd.main()
        print("seed data - end")
        print("start dochazka")


def login():
    login_page = lg.Login_Page()  # I dont need to pass the root now since its initialized inside the class
    login_page.mainloop_window()
    return login_page


def main():
    startup_config()
    lp = login()

    main_win = MainWin(lp.get_user_name, lp.get_user_id, lp.get_hire_date, lp.is_employer)
    main_win.mainloop_window()


class MainWin:
    def __init__(self,
                 user,
                 user_id,
                 hire_date,
                 is_employer):
        main_win = Tk()
        self.main_win = main_win
        main_win.title("Docházkový systém MANDINEC - ")
        main_win.protocol("WM_DELETE_WINDOW", self.__event_x)
        main_win.geometry("700x500")
        main_win.minsize(700, 500)
        app = td.Example(user, user_id, hire_date, is_employer, main_win)

    def __event_x(self):
        exit()

    def mainloop_window(self):  # This is the class function that helps me to mainloop the window
        self.main_win.mainloop()


if __name__ == '__main__':
    main()
