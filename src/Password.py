from tkinter import Tk, Text, BOTH, W, N, E, S, LEFT, END, Listbox, BooleanVar, Checkbutton, LabelFrame, Radiobutton, \
    IntVar, Entry, Toplevel, font, messagebox
from tkinter.ttk import Frame, Button, Label, Style, Combobox
from tkcalendar import Calendar, DateEntry
import src.Database as db


class PassFrame(Frame):
    def __init__(self,
                 root,
                 user_id):
        super().__init__()
        self.root = root
        root.title("Hire")
        root.geometry("350x200+250+170")
        root.minsize(350, 200)
        root.maxsize(350, 200)
        self.user_id = user_id
        self.var = BooleanVar()
        self.conn = db.create_connection()
        print("toto -> " + str(self.user_id))
        self.__init_ui()

    def change_pass(self):
        print("reg")
        print(self.__old_password_box.get())
        print(self.__new_password_box.get())
        print(self.__new_again_password.get())
        print("okok")
        print(self.__new_password_box.get())
        print(len(self.__new_password_box.get()))
        if (len(self.__new_password_box.get()) != 0 and len(self.__old_password_box.get()) != 0 and len(
                self.__new_again_password.get()) != 0):
            print("no empty")
            if db.check_pass(self.conn, self.__old_password_box.get()) is True:
                print("check pass aprove")
                if self.__new_password_box.get() == self.__new_again_password.get():
                    print("change")
                    change_pass = (self.__new_password_box.get(), self.user_id)
                    db.change_password(self.conn, change_pass)
                else:
                    print("Hesla se neshodují")
                    messagebox.showwarning("Chyba hesla!", "Hesla se neshodují!")
            else:
                print("Špatně zadané staré heslo")
                messagebox.showwarning("Chyba hesla!", "Špatně zadané staré heslo!")

        else:
            print("Hesla nesmí být prázdné")
            messagebox.showwarning("Chyba hesla!", "Hesla nesmí být prázdné!")

    def __init_ui(self):
        lb_popis = Label(self.root, text="Změna hesla:")
        lb_popis.grid(row=0, column=1, pady=5)

        lb_old_pass = Label(self.root, text="Staré heslo:")
        # self.username.place(relx=0.285, rely=0.298, height=20, width=60)
        lb_old_pass.grid(row=1, column=2, pady=5)

        lb_new_pass = Label(self.root, text="Nové heslo:")
        # self.password.place(relx=0.285, rely=0.468, height=20, width=60)
        lb_new_pass.grid(row=2, column=2, pady=5)

        lb_new_pass_again = Label(self.root, text="Heslo znova:")
        # self.firstName.place(relx=0.285, rely=0.638, height=20, width=60)
        lb_new_pass_again.grid(row=3, column=2, pady=5)

        # Creating Buttons

        self.__btn_hire = Button(self.root, text="Změnit heslo!", command=self.change_pass)
        self.__btn_hire.grid(row=4, column=2, columnspan=2, pady=5)
        # self.__btn_hire(relx=0.440, rely=0.638, height=30, width=60)
        # self.__btn_hire.configure(command=self.login_user)
        #
        # self.login_completed = IntVar()
        #
        # self.exit_button = Button(self.root, text="Exit")  # , command=master.quit)
        # self.exit_button.place(relx=0.614, rely=0.638, height=30, width=60)
        # self.exit_button.configure(command=self.exit_login)

        # Creating entry boxes

        self.__old_password_box = Entry(self.root)
        # self.username_box.place(relx=0.440, rely=0.298, height=20, relwidth=0.35)
        self.__old_password_box.grid(row=1, column=3)
        self.__old_password_box.configure(show="*")
        self.__old_password_box.configure(background="white")

        self.__new_password_box = Entry(self.root)
        # self.password_box.place(relx=0.440, rely=0.468, height=20, relwidth=0.35)
        self.__new_password_box.grid(row=2, column=3)
        self.__new_password_box.configure(show="*")
        self.__new_password_box.configure(background="white")

        self.__new_again_password = Entry(self.root)
        self.__new_again_password.grid(row=3, column=3)
        self.__new_again_password.configure(show="*")
        self.__new_again_password.configure(background="white")
