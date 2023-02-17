__all__ = ["InfoButton"]

from .colorbtn import *
from ..athlete import *


class InfoButton(ColorButton):
    def __init__(self, master, root_win, hover_color, info: Athlete):
        super().__init__(master=master, root_win=root_win, hover_color=hover_color, start_bg="#F8F5F5")

        self.root_win = root_win
        self.config(width=11, text=f"{info.index} | {info.name}", borderwidth=0, cursor="hand2", font=("Montserrat", 15, "bold"))
        self.info = info
