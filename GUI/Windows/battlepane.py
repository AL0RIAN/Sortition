__all__ = ["BattleWindow"]

from tkinter import *
from ..Buttons.battlebtn import *
from typing import List
import keyboard
from GUI.Buttons import InfoButton
from GUI.athlete import *
from GUI.Buttons.colorbtn import *


class BattleWindow(PanedWindow):
    DIRECTION = True

    def __init__(self, master=None, root_win=None, cnf={}, **kwargs):
        Widget.__init__(self, master=master, widgetName='panedwindow', cnf={}, **kwargs)
        self.fields: List[List[Button]] = []

        self.root_win = root_win
        self.grid_columnconfigure(index=0, minsize=self.winfo_screenwidth() // 16)
        self.config(background="#6C6C6C")

        # Vertical Scrollbar
        self.vertical_scroll = Scrollbar(master=self)
        self.vertical_scroll.pack(side=RIGHT, fill=Y)

        # Horizontal Scrollbar
        self.horizontal_scroll = Scrollbar(self, orient=HORIZONTAL)
        self.horizontal_scroll.pack(side=BOTTOM, fill=X)

        # Canvas (Scrollable Widget)
        self.canvas = Canvas(master=self,
                             background="#6C6C6C",
                             highlightbackground="#6C6C6C",
                             yscrollcommand=self.vertical_scroll.set,
                             xscrollcommand=self.horizontal_scroll.set)
        self.canvas.pack(fill=BOTH, expand=1)

        # Scrolls Configure Update
        self.vertical_scroll.configure(command=self.canvas.yview)
        self.horizontal_scroll.configure(command=self.canvas.xview)

        # Binding
        self.canvas.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Creating A New Frame
        self.canvas_frame = Frame(master=self.canvas, background="#6C6C6C", highlightbackground="#6C6C6C")
        self.canvas.create_window((0, 0), window=self.canvas_frame, anchor="nw")

        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        keyboard.add_hotkey(hotkey="ctrl", callback=self.change_direction)

    def change_direction(self):
        print(f"H {self.DIRECTION}")
        print(f"V {not self.DIRECTION}\n")

        if not self.DIRECTION:
            self.DIRECTION = True
        else:
            self.DIRECTION = False

    def on_mousewheel(self, event):
        if self.DIRECTION:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif not self.DIRECTION:
            self.canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

    def create_grid(self) -> None:
        for col in range(16):
            temp: List[Button] = []
            for row in range(32):
                btn = BattleButton(self.canvas_frame, text=f" ", root_win=self.root_win, hover_color="GRAY")
                btn.grid(row=row, column=col, sticky="news")
                temp.append(btn)
            self.fields.append(temp)

    def add_members(self):
        # ЭТА ФУНКЦИЯ ДЛЯ СОЗДАНИЯ ТОЛЬКО ПЕРВОГО СТОЛБИКА
        column = 0
        row = 0

        for pair in all:
            print(pair[0].name, pair[1].name, end="\n")
        # for col in range(3):
        #     row = 0 + col
        for pair in all:
            InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=pair[0]).grid(row=row, column=0)
            first = pair[0]

            InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=pair[1]).grid(row=row + 2, column=0)
            second = pair[1]

            btn = self.fields[column][row + 1]
            btn.config(text="БОЙ", state="normal", cursor="hand2", command=lambda args=(first, second, btn): self.winner(args[0], args[1], args[2]))


            row += 4

    def winner(self, first: Athlete, second: Athlete, btn: Button):
        if first.power > second.power:
            InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=first).grid(row=btn.grid_info()["row"], column=btn.grid_info()["column"] + 1)
        else:
            InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=second).grid(row=btn.grid_info()["row"], column=btn.grid_info()["column"] + 1)

        btn.config(state="disabled")

# СОЗДАТЬ ФУНКЦИЮ, КОТОРАЯ БУДЕТ ПРОДЛЕВАТЬ СЕТКУ НА ОДНОГО УЧАСТНИКА. ГЛОБАЛЬНЫЙ СПИСОК УЧАСТНИКОВ УМЕНЬШАЕТСЯ
