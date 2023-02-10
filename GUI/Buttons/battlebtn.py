__all__ = ["BattleButton"]

from tkinter import Button


class BattleButton(Button):
    """Tkinter Button child. Navigation bar button.

    TOP FIELDS

        ENTER_STATE: This filed indicate cursor position relative to the button.
        False - cursor is outside the button. True - cursor within the button.

        COLOR - indicator in range [0-255)
    """

    def __init__(self, master, root_win, text=" ",
                 font=("Montserrat", 15, "bold"),
                 borderwidth=1,
                 background="#F8F5F5",
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
                         borderwidth=0,
                         background="#6C6C6C",
                         )

        self.root_win = root_win
        self.config(width=11)
        self.config(state="disabled")
