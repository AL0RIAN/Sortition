__all__ = ["VersusButton"]

from .battlebtn import *

# ЕСЛИ ОПРЕДЕЛЕНА ПОБЕДА В РАУНДЕ (ДОБАВИТЬ ОДНО ПОЛСЕ ВМЕСТО БЛЕК), ТО ДЛЯ ЭТОЙ КНОПКИ (ДЛЯ ИМЕНИ) СДЕЛАТЬ ПРОВЕРКУ НА ПОБЕДИТЕЛЯ
class VersusButton(BattleButton):
    CURRENT_ROUND = 0

    def __init__(self, master, root_win, window=None):
        super().__init__(master=master, root_win=root_win, hover_color="DARK_MOON")

        self.SCORES = {0: [0, 0, False],
                       1: [0, 0, False],
                       2: [0, 0, False]}

        self.WARNS = {0: [0, 0],
                      1: [0, 0],
                      2: [0, 0]}

        self.OBSERV = {0: [0, 0],
                       1: [0, 0],
                       2: [0, 0]}

        self.root_win = root_win
        self.window = window
        self.config(text="БОЙ", state="normal", cursor="hand2", fg="#fff")
