__all__ = ["VersusButton"]

from .battlebtn import *


class VersusButton(BattleButton):
    CURRENT_ROUND = 0

    def __init__(self, master, root_win, window=None):
        super().__init__(master=master, root_win=root_win, hover_color="DARK_MOON")

        self.SCORES = {"0": [0, 0, False],
                       "1": [0, 0, False],
                       "2": [0, 0, False]}

        self.WARNS = [0, 0]

        self.OBSERV = {"0": [0, 0],
                       "1": [0, 0],
                       "2": [0, 0]}

        self.KNOCK = {"0": [0, 0],
                      "1": [0, 0],
                      "2": [0, 0]}

        self.OUT = {"0": [0, 0],
                    "1": [0, 0],
                    "2": [0, 0]}

        self.AUTO_WIN = None

        self.root_win = root_win
        self.window = window
        self.space = 1
        self.config(text="БОЙ", state="disabled", cursor="hand2", fg="#fff")

    def tester_mode(self):
        for score in "0", "1", "2":
            self.SCORES[score][0] = 100
            self.SCORES[score][2] = True
