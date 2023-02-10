__all__ = ["BattleWindow"]

from tkinter import *
from ..Buttons.battlebtn import *
from typing import List
import keyboard


class BattleWindow(PanedWindow):
    DIRECTION = True

    def __init__(self, master=None, root_win=None, cnf={}, **kwargs):
        Widget.__init__(self, master=master, widgetName='panedwindow', cnf={}, **kwargs)
        self.fields: List[List[BattleButton]] = []

        self.root_win = root_win
        self.grid_columnconfigure(index=0, minsize=self.winfo_screenwidth() // 16)
        self.config(background="#6C6C6C")

        # Vertical Scrollbar
        self.vertical_scroll = Scrollbar(master=self)
        self.vertical_scroll.pack(side=RIGHT, fill=Y)

        # Horizontal Scrollbar
        self.horizontal_scroll = Scrollbar(self, orient=HORIZONTAL)
        self.horizontal_scroll.pack(side=BOTTOM, fill=X)

        # Canvas (Scrollable Widget)
        self.canvas = Canvas(master=self,
                             background="#6C6C6C",
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

        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        keyboard.add_hotkey(hotkey="ctrl", callback=self.change_direction)

    def change_direction(self):
        print(f"H {self.DIRECTION}")
        print(f"V {not self.DIRECTION}\n")

        if not self.DIRECTION:
            self.DIRECTION = True
        else:
            self.DIRECTION = False

    def on_mousewheel(self, event):
        if self.DIRECTION:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif not self.DIRECTION:
            self.canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

    def create_grid(self) -> None:
        for row in range(32):
            temp: List[BattleButton] = []
            for col in range(16):
                btn = BattleButton(self.canvas_frame, text=f" ", root_win=self.root_win)
                btn.grid(row=row, column=col, sticky="news")
                temp.append(btn)
            self.fields.append(temp)
