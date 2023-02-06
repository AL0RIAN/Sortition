from tkinter import Button, Event
from GUI.colors import ColorRange, RED
from root import root

color_range = ColorRange(color=RED)


class NavigationButton(Button):
    """Tkinter Button child. Navigation bar button.

    TOP FIELDS

        ENTER_STATE: This filed indicate cursor position relative to the button.
        False - cursor is outside the button. True - cursor within the button.

        COLOR - indicator in range [0-255)
    """
    ENTER_STATE = False
    COLOR = 0

    def __init__(self, master, text="New",
                 font=("Montserrat", 15, "bold"),
                 borderwidth=0,
                 background="#F8F5F5",
                 cursor="hand2",
                 cnf={}, **kw):
        """Construct a button widget with the parent MASTER.


        STANDARD OPTIONS (tkinter.Button)

            activebackground, activeforeground, anchor,
            background, bitmap, borderwidth, cursor,
            disabledforeground, font, foreground
            highlightbackground, highlightcolor,
            highlightthickness, image, justify,
            padx, pady, relief, repeatdelay,
            repeatinterval, takefocus, text,
            textvariable, underline, wraplength

        WIDGET-SPECIFIC OPTIONS (tkinter.Button)

            command, compound, default, height,
            overrelief, state, width
        """
        super().__init__(master=master,
                         text=text,
                         font=("Montserrat", 15, "bold"),
                         borderwidth=borderwidth,
                         background=background,
                         cursor=cursor)
        self.bind("<Enter>", self.enter)
        self.bind("<Leave>", self.leave)

    def enter(self, event: Event = None) -> None:
        self.ENTER_STATE = True
        self.hover_enter()

    def leave(self, event: Event = None) -> None:
        self.ENTER_STATE = False
        self.hover_leave()

    def hover_enter(self) -> None:
        if self.ENTER_STATE:
            if self.COLOR < 150:
                color = color_range.get_color(index=self.COLOR)
                self.COLOR += 1
                self.config(background=color)
                root.after(1, self.hover_enter)
            else:
                return

    def hover_leave(self) -> None:
        if not self.ENTER_STATE:
            if self.COLOR - 1 != -1:
                self.COLOR -= 1
                color = color_range.get_color(self.COLOR)
                self.config(background=color)
                root.after(1, self.hover_leave)
            else:
                return
