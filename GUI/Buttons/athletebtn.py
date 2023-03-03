__all__ = ["InfoButton"]

from tkinter import Toplevel, Label
from .colorbtn import *
from ..athlete import *


class InfoButton(ColorButton):
    def __init__(self, master, root_win, hover_color, info: Athlete):
        super().__init__(master=master, root_win=root_win, hover_color=hover_color, start_bg="#F8F5F5")

        self.root_win = root_win
        self.info = info
        self.config(width=11, text=f"{info.index} | {info.name}", borderwidth=0, cursor="hand2", font=("Montserrat", 15, "bold"))
        self.config(command=self.info_win)
        self.info = info

    def info_win(self):
        info_win = Toplevel(master=self)
        info_win.title(self.info.name)
        info_win.geometry("300x400")

        Label(master=info_win, text=f"Имя: {self.info.name}", font=("Montserrat", 15)).pack()
        Label(master=info_win, text=f"Индекс: {self.info.index}", font=("Montserrat", 15)).pack()

