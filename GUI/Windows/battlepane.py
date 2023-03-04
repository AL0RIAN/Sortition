__all__ = ["BattleWindow"]

from tkinter import *
from ..Buttons.battlebtn import *
from typing import List
import keyboard
from GUI.Buttons import InfoButton, VersusButton
from GUI.athlete import *
from math import ceil
from .versus import *


class BattleWindow(PanedWindow):
    DIRECTION = True
    MEMBERS = len(all) * 2
    COLUMN = 0
    SPACES = 0  # Текущий отступ + текущая колонка + 1 (SPACES + COLUMN + 1)
    CURRENT_GRID = 0
    COLUMN_MEMBERS = ceil(MEMBERS / 2)
    BORDER = False
    VERSUS_BUTTONS = list()
    CURRENT_VERSUS = 0

    def __init__(self, master=None, root_win=None, cnf={}, **kwargs):
        Widget.__init__(self, master=master, widgetName='panedwindow', cnf={}, **kwargs)
        self.fields: List[List[Button]] = []

        self.root_win = root_win
        self.grid_columnconfigure(index=0, minsize=self.winfo_screenwidth() // 16)
        self.config(background="#212126")

        # Vertical Scrollbar
        self.vertical_scroll = Scrollbar(master=self)
        self.vertical_scroll.pack(side=RIGHT, fill=Y)

        # Horizontal Scrollbar
        self.horizontal_scroll = Scrollbar(self, orient=HORIZONTAL)
        self.horizontal_scroll.pack(side=BOTTOM, fill=X)

        # Canvas (Scrollable Widget)
        self.canvas = Canvas(master=self,
                             background="#212126",
                             highlightbackground="#212126",
                             yscrollcommand=self.vertical_scroll.set,
                             xscrollcommand=self.horizontal_scroll.set)
        self.canvas.pack(fill=BOTH, expand=1)

        # Scrolls Configure Update
        self.vertical_scroll.configure(command=self.canvas.yview)
        self.horizontal_scroll.configure(command=self.canvas.xview)

        # Binding
        self.canvas.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Creating A New Frame
        self.canvas_frame = Frame(master=self.canvas, background="#212126", highlightbackground="#212126")
        self.canvas.create_window((0, 0), window=self.canvas_frame, anchor="nw")

        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        keyboard.add_hotkey(hotkey="ctrl", callback=self.change_direction)

        # Add to settings
        self.root_win.settings_menu.add_command(label="Сетка", command=self.border_settings)

    def change_direction(self):
        # print(f"H {self.DIRECTION}")
        # print(f"V {not self.DIRECTION}\n")

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
                btn = BattleButton(self.canvas_frame, text=f" ", root_win=self.root_win, hover_color="DARK_MOON")
                btn.grid(row=row, column=col, sticky="news")
                temp.append(btn)
            self.fields.append(temp)

    def border_settings(self):
        settings = Toplevel(master=self)
        settings.geometry("300x300")
        Label(master=settings, text="Сетка").grid(row=0, column=0)
        Checkbutton(master=settings, command=self.border_set).grid(row=0, column=1)

    def border_set(self):
        for col in range(16):
            for row in range(32):
                if BattleWindow.BORDER:
                    self.fields[col][row].config(borderwidth=0)
                else:
                    self.fields[col][row].config(borderwidth=1)

        BattleWindow.BORDER = True if not BattleWindow.BORDER else False

    def start(self):
        column = 0
        row = 0

        for pair in all:
            InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=pair[0]).grid(
                row=row, column=0)
            first = pair[0]

            InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=pair[1]).grid(
                row=row + 2, column=0)
            second = pair[1]

            btn = self.fields[column][row + 1]

            btn = VersusButton(master=self.canvas_frame, root_win=self.root_win)
            self.fields[column][row + 1] = btn
            btn.config(command=lambda args=(first, second, btn): self.winner(args[0], args[1], args[2]))
            btn.grid(row=row + 1, column=column)
            BattleWindow.VERSUS_BUTTONS.append(btn)

            row += 4

        BattleWindow.VERSUS_BUTTONS[BattleWindow.CURRENT_VERSUS].config(state="normal")
        self.COLUMN += 1
        self.SPACES = self.SPACES + self.COLUMN + 1

    def winner(self, first: Athlete, second: Athlete, btn: VersusButton):
        # Если программа находит две победы, то блокирует кнопку и выводит победителя вперед
        first_scores = 0
        second_scores = 0

        if btn.AUTO_WIN is not None:
            self.check_winner(btn.AUTO_WIN, btn)
            return

        for btl_round in range(0, 3):
            if btn.SCORES[btl_round][0] > btn.SCORES[btl_round][1]:
                first_scores += 1
            elif btn.SCORES[btl_round][0] < btn.SCORES[btl_round][1]:
                second_scores += 1
            else:
                continue

        if first_scores >= 2:
            self.check_winner(first, btn)
        elif second_scores >= 2:
            self.check_winner(second, btn)
        else:
            VersusWindow(master=self, first=first, second=second, call_btn=btn, current_frame=btn.CURRENT_ROUND,
                         root_win=self.root_win)

    def check_winner(self, athlete: Athlete, btn: Button):
        # if first.score > second.score:
        #     new_btn = InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=first)
        #     new_btn.grid(row=btn.grid_info()["row"], column=btn.grid_info()["column"] + 1)
        #     self.fields[btn.grid_info()["column"] + 1][btn.grid_info()["row"]] = new_btn
        # else:
        #     new_btn = InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=second)
        #     new_btn.grid(row=btn.grid_info()["row"], column=btn.grid_info()["column"] + 1)
        #     self.fields[btn.grid_info()["column"] + 1][btn.grid_info()["row"]] = new_btn

        new_btn = InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=athlete)
        new_btn.grid(row=btn.grid_info()["row"], column=btn.grid_info()["column"] + 1)
        self.fields[btn.grid_info()["column"] + 1][btn.grid_info()["row"]] = new_btn

        if self.COLUMN_MEMBERS != 0:
            self.check_column()
            self.COLUMN_MEMBERS -= 1
        else:
            self.COLUMN += 1
            self.SPACES = 2 ** self.COLUMN
            self.COLUMN_MEMBERS = (self.MEMBERS // (2 ** self.COLUMN)) - 1
            self.CURRENT_GRID = 0

        try:
            BattleWindow.VERSUS_BUTTONS[BattleWindow.CURRENT_VERSUS].config(state="disabled")
            BattleWindow.VERSUS_BUTTONS[BattleWindow.CURRENT_VERSUS + 1].config(state="normal")
            BattleWindow.CURRENT_VERSUS += 1
        except IndexError:
            return

    def check_column(self):
        for row in range(self.CURRENT_GRID, 32):

            first_btn = self.fields[self.COLUMN][row]

            if first_btn.__class__.__name__ == "InfoButton":
                self.CURRENT_GRID = first_btn.grid_info()["row"]
                for under_row in range(self.CURRENT_GRID + 1, 32):
                    second_btn = self.fields[self.COLUMN][under_row]
                    if second_btn.__class__.__name__ == "InfoButton":
                        # btn = self.fields[column][row + 1]
                        #
                        # btn = VersusButton(master=self.canvas_frame, root_win=self.root_win)
                        # self.fields[column][row + 1] = btn
                        # btn.config(command=lambda args=(first, second, btn): self.winner(args[0], args[1], args[2]))
                        # btn.grid(row=row + 1, column=column)

                        battle_btn = self.fields[self.COLUMN][abs(under_row - self.SPACES)]
                        battle_btn = VersusButton(master=self.canvas_frame, root_win=self.root_win)
                        self.fields[self.COLUMN][abs(under_row - self.SPACES)] = battle_btn
                        battle_btn.config(
                            command=lambda args=(first_btn.info, second_btn.info, battle_btn): self.winner(args[0],
                                                                                                           args[1],
                                                                                                           args[2]))
                        battle_btn.grid(row=abs(under_row - self.SPACES), column=self.COLUMN)
                        BattleWindow.VERSUS_BUTTONS.append(battle_btn)

                        # battle_btn = self.fields[self.COLUMN][abs(under_row - self.SPACES)]
                        #
                        # battle_btn.config(text="БОЙ", state="normal", cursor="hand2", fg="#fff",
                        #                   command=lambda
                        #                       args=(first_btn.info, second_btn.info, battle_btn): self.winner(args[0],
                        #                                                                                       args[1],
                        #                                                                                       args[2]
                        #                                                                                       ))
                        self.CURRENT_GRID = under_row + 1

                        return
