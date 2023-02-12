__all__ = ["NavigationButton"]

from .colorbtn import *


class NavigationButton(ColorButton):
    def __init__(self, master, root_win, hover_color, command, text="New"):

        super().__init__(master=master, root_win=root_win, hover_color=hover_color, start_bg="#F8F5F5")

        self.root_win = root_win
        self.config(text=text,
                    borderwidth=0,
                    cursor="hand2",
                    command=command,
                    background="#F8F5F5",
                    font=("Montserrat", 15, "bold"))
