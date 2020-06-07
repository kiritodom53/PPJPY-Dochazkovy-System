import src.Data.SeedData as seedData
from src.Database import check_database, create_connection, create_database, check_tables, create_tables
from src.Login import LoginPage
from tkinter import Tk
from src.Dochazka import AttendanceFrame
from sys import exit


def startup_config():
    """Startup database configurations
    """
    print("STARTUP - CONFIG")
    if not check_database():
        print(check_database())
        create_database()

    conn = create_connection()
    users = check_tables(conn, "users")
    presence = check_tables(conn, "presence")

    # Vytvoří tabulky, pokud neexistují
    if users is False or presence is False:
        print("main")
        create_tables()
        print("seed data - start")
        seedData.main()
        print("seed data - end")
        print("start dochazka")


def login() -> LoginPage:
    login_page = LoginPage()  # I dont need to pass the root now since its initialized inside the class
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
        """

        Args:
            user: User full name
            user_id: user id
            hire_date: hire date
            is_employer: if user is employer
        """
        main_win = Tk()
        self.main_win = main_win
        main_win.title("Docházkový systém MANDINEC 1.0 - " + user)
        main_win.protocol("WM_DELETE_WINDOW", self.__event_x)
        main_win.geometry("700x500")
        main_win.minsize(700, 500)
        AttendanceFrame(user, user_id, hire_date, is_employer, main_win)

    def __event_x(self):
        exit()

    def mainloop_window(self):
        """Function that helps me to mainloop the window
        """
        self.main_win.mainloop()


if __name__ == '__main__':
    main()
