from tkinter import Tk, Text, BOTH, W, N, E, S, LEFT, Listbox, LabelFrame, Radiobutton, IntVar, Toplevel
from tkinter.ttk import Frame, Button, Label, Style, Combobox
import ReadFiles.ReadFileBoot as db


# Tk, Text, BOTH, W, N, E, S, Listbox, LabelFrame, Radiobutton, IntVar

class Example(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def update(self):
        print("btnUpdate")
        conn = db.create_connection()
        db.select_user_by_id(conn, 1)
        # root = Tk()
        # window = Toplevel(root)

    # def getBntUpdate(self):
    #    return self.btnUpdate

    def initUI(self):
        self.master.title("DTB")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        btnUpdate = Button(self, text="Aktualizovat", command=self.update)
        btnUpdate.pack()

        btnLogOut = Button(self, text="Odhlásit se")
        btnLogOut.pack()
