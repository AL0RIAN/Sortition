__all__ = ["ColorButton"]

from tkinter import Button, Event
from GUI.Colors.colors import *


class ColorButton(Button):
    """Tkinter Button child. Navigation bar button.

    TOP FIELDS

        ENTER_STATE: This filed indicate cursor position relative to the button.
        False - cursor is outside the button. True - cursor within the button.

        COLOR - indicator in range [0-255)
    """

    ENTER_STATE = False
    COLOR = 0

    def __init__(self, master, root_win, hover_color: str, start_bg: str):
        super().__init__(master=master)
        self.root_win = root_win
        self.hover_range = ColorRange(ColorRange.colors[hover_color], background=start_bg)
        self.config(activebackground=self.hover_range.get_color(200))
        self.config(font=("Montserrat", 15, "bold"))
        self.config(background=start_bg)
        self.config(borderwidth=0)

        self.bind("<Enter>", self.enter)
        self.bind("<Leave>", self.leave)

    def enter(self, event: Event = None) -> None:
        self.ENTER_STATE = True
        self.hover_enter()

    def hover_enter(self) -> None:
        if self.ENTER_STATE:
            if self.COLOR < 150:
                current_color = self.hover_range.get_color(index=self.COLOR)
                self.COLOR += 1
                self.config(background=current_color)
                self.root_win.root.after(1, self.hover_enter)
            else:
                return

    def leave(self, event: Event = None) -> None:
        self.ENTER_STATE = False
        self.hover_leave()

    def hover_leave(self) -> None:
        if not self.ENTER_STATE:
            if self.COLOR - 1 != -1:
                self.COLOR -= 1
                current_color = self.hover_range.get_color(self.COLOR)
                self.config(background=current_color)
                self.root_win.root.after(1, self.hover_leave)
            else:
                return
