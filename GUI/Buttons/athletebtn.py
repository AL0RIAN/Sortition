__all__ = ["InfoButton"]

import json
from tkinter import Toplevel, Label
from .colorbtn import *
from sorting.athlete import *


class InfoButton(ColorButton):
    def __init__(self, master, root_win, hover_color, info):
        super().__init__(master=master, root_win=root_win, hover_color=hover_color, start_bg="#F8F5F5")

        # text = "-"
        # try:
        #     # print(f"Info: {info}")
        #     if info.name == "-":
        #         text = "-"
        #     else:
        #         text = info.name.split()[0]
        #         text += f" {info.name.split()[1][:1]}."
        # except AttributeError:
        #     # print(f"Info: {info}")
        #     pass

        if type(info) != Athlete:
            info = Athlete(json.loads(info))

        self.root_win = root_win
        self.info = info  # Десерелизация
        self.config(width=11, text=info.name, borderwidth=0, cursor="hand2", font=("Montserrat", 15, "bold"))
        self.config(command=self.info_win)
        self.info = info

    def info_win(self):
        info_win = Toplevel(master=self)
        info_win.title(self.info.name)
        info_win.geometry("300x400")

        Label(master=info_win, text=f"Участник: {self.info.name}", font=("Montserrat", 15)).pack()
