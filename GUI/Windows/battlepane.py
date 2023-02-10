__all__ = ["BattleWindow"]

from tkinter import *
from tkinter import ttk
from ..Buttons.battlebtn import *


class BattleWindow(PanedWindow):
    # Поле из двумерного массива
    fields = []

    def __init__(self, master, root_win, cnf={}, **kwargs):
        Widget.__init__(self, master, 'panedwindow', cnf, kwargs)
        self.root_win = root_win
        self.grid_columnconfigure(index=0, minsize=self.winfo_screenwidth() // 16)

        # Vertical Scrollbar
        self.vertical_scroll = Scrollbar(master=self)
        self.vertical_scroll.pack(side=RIGHT, fill=Y)

        # Horizontal Scrollbar
        self.horizontal_scroll = Scrollbar(self, orient=HORIZONTAL)
        self.horizontal_scroll.pack(side=BOTTOM, fill=X)

        # Canvas (Scrollable Widget)
        self.canvas = Canvas(master=self,
                             background="red",
                             highlightbackground="#6C6C6C",
                             yscrollcommand=self.vertical_scroll.set,
                             xscrollcommand=self.horizontal_scroll.set)
        self.canvas.pack(fill=BOTH, expand=1)

        # Scrolls Configure Update
        self.vertical_scroll.configure(command=self.canvas.yview)
        self.horizontal_scroll.configure(command=self.canvas.xview)

        # Binding
        self.canvas.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Creating A New Frame
        self.canvas_frame = Frame(master=self.canvas, background="#6C6C6C", highlightbackground="#6C6C6C")
        self.canvas.create_window((0, 0), window=self.canvas_frame, anchor="nw")

    def create_grid(self):
        for row in range(32):
            for col in range(16):
                BattleButton(self.canvas_frame, text=f"", root_win=self.root_win).grid(row=row, column=col,
                                                                                                  pady=10, padx=10,
                                                                                                  sticky="news")

# Сделать бинд на колесико мыши
