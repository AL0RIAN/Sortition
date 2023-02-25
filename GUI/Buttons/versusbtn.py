__all__ = ["VersusButton"]

from .battlebtn import *


class VersusButton(BattleButton):
    CURRENT_ROUND = 0

    def __init__(self, master, root_win, window=None):
        super().__init__(master=master, root_win=root_win, hover_color="DARK_MOON", start_bg="#212126")

        self.SCORES = {0: [0, 0, "black", "black"],
                       1: [0, 0, "black", "black"],
                       2: [0, 0, "black", "black"]}

        self.root_win = root_win
        self.window = window
        self.config(text="БОЙ", state="normal", cursor="hand2", fg="#fff")
