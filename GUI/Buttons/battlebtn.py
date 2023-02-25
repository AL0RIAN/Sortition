__all__ = ["BattleButton"]

from tkinter import SUNKEN
from .colorbtn import *


class BattleButton(ColorButton):
    def __init__(self, master, root_win, hover_color, text=" ", cnf={}, **kw):
        super().__init__(master=master, root_win=root_win, hover_color=hover_color, start_bg="#212126")

        self.root_win = root_win
        self.config(width=11, text=text, borderwidth=0, background="#212126", relief=SUNKEN, state="disabled",
                    font=("Montserrat", 15, "bold"), )

