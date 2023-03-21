__all__ = ["BattleWindow"]

import json
from tkinter import *
from ..Buttons.battlebtn import *
from typing import List, Dict
import keyboard
from GUI.Buttons import InfoButton, VersusButton
from sorting.athlete_sort import *
from sorting.athlete import *
from .versus import *


class BattleWindow(PanedWindow):

    def __init__(self, master=None, root_win=None, args: dict = None, number="0"):
        Widget.__init__(self, master=master, widgetName='panedwindow', cnf={})

        self.DIRECTION = args["direction"]
        self.MEMBERS = args["members"]
        self.COLUMN = args["column"]
        self.SPACES = args["spaces"]  # Текущий отступ + текущая колонка + 1 (SPACES + COLUMN + 1)
        self.CURRENT_GRID = args["cur_grid"]
        self.COLUMN_MEMBERS = args["column_member"]
        self.BORDER = args["border"]
        self.VERSUS_BUTTONS = list()
        self.CURRENT_VERSUS = args["cur_vs"]

        self.fields: List[List[Button]] = list()
        self.data_base: Dict = dict()
        self.number = number

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

        # Creating A New Frame For Scroll
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

    def create_grid(self, db: dict = None) -> None:
        self.data_base = db

        if self.data_base == {}:
            for col in range(16):
                temp: List[Button] = []
                for row in range(32):
                    btn = BattleButton(self.canvas_frame, text=" ", root_win=self.root_win, hover_color="DARK_MOON")
                    btn.grid(row=row, column=col, sticky="news")
                    temp.append(btn)
                    self.data_base[f"{col}x{row}"] = dict()
                    self.data_base[f"{col}x{row}"]["type"] = "BattleButton"
                self.fields.append(temp)
            self.start()

        else:
            self.fill()

        # Сохраняем в общую базу данных состояние поля
        self.root_win.set_dbg(number=self.number, data=self.data_base)
        self.root_win.set_dbw(number=self.number, data={"DIRECTION": self.DIRECTION,
                                                        "MEMBERS": self.MEMBERS,
                                                        "COLUMN": self.COLUMN,
                                                        "SPACES": self.SPACES,
                                                        "CURRENT_GRID": self.CURRENT_GRID,
                                                        "COLUMN_MEMBERS": self.COLUMN_MEMBERS,
                                                        "BORDER": self.BORDER,
                                                        # "VERSUS_BUTTONS": self.VERSUS_BUTTONS,
                                                        "CURRENT_VERSUS": self.CURRENT_VERSUS
                                                        })

    def get_grid_info(self) -> dict:
        info = {"direction": self.DIRECTION,
                "members": self.MEMBERS,
                "column": self.COLUMN,
                "spaces": self.SPACES,
                "cur_grid": self.CURRENT_GRID,
                "column_member": self.COLUMN_MEMBERS,
                "border": self.BORDER,
                "cur_vs": self.CURRENT_VERSUS}
        return info

    def clear(self) -> dict:
        for child in self.canvas_frame.winfo_children():
            if child.__class__.__name__ in ("BattleButton", "InfoButton", "VersusButton"):
                child.destroy()
        self.fields.clear()
        self.VERSUS_BUTTONS.clear()
        return self.data_base

    def fill(self) -> None:
        for col in range(8):
            temp = []
            for row in range(32):
                if self.data_base[f"{col}x{row}"]["type"] == "BattleButton":
                    btn = BattleButton(self.canvas_frame, text=" ", root_win=self.root_win, hover_color="DARK_MOON")
                    btn.grid(row=row, column=col, sticky="news")
                    temp.append(btn)
                elif self.data_base[f"{col}x{row}"]["type"] == "InfoButton":
                    # Десериализация Из Словаря В Поля Класса Атлет
                    # TODO Десериализация происходит не до конца (инфа в виде строк)

                    athlete_data = json.loads(self.data_base[f"{col}x{row}"]["Athlete"])

                    athlete = Athlete(args=athlete_data)

                    btn = InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN",
                                     info=athlete)
                    btn.grid(row=row, column=col, sticky="news")
                    temp.append(btn)

                elif self.data_base[f"{col}x{row}"]["type"] == "VersusButton":
                    btn = VersusButton(self.canvas_frame, root_win=self.root_win)

                    # TODO TESTER MODE
                    # btn.tester_mode()
                    btn.grid(row=row, column=col, sticky="news")

                    scores = self.data_base[f"{col}x{row}"]["info"]["scores"]
                    warns = self.data_base[f"{col}x{row}"]["info"]["warns"]
                    observ = self.data_base[f"{col}x{row}"]["info"]["observ"]
                    knocks = self.data_base[f"{col}x{row}"]["info"]["knocks"]
                    outs = self.data_base[f"{col}x{row}"]["info"]["outs"]
                    auto_win = self.data_base[f"{col}x{row}"]["info"]["auto_win"]
                    state = self.data_base[f"{col}x{row}"]["info"]["state"]
                    spaces = self.data_base[f"{col}x{row}"]["info"]["space"]

                    btn.config(state=state)
                    btn.SCORES = scores
                    btn.WARNS = warns
                    btn.OBSERV = observ
                    btn.KNOCK = knocks
                    btn.OUT = outs
                    btn.AUTO_WIN = auto_win
                    btn.space = spaces

                    self.VERSUS_BUTTONS.append(btn)
                    temp.append(btn)

            self.fields.append(temp)

        count = 1
        for btn in self.VERSUS_BUTTONS:
            first = self.fields[btn.grid_info()['column']][btn.grid_info()['row'] - btn.space].info
            second = self.fields[btn.grid_info()['column']][btn.grid_info()['row'] + btn.space].info
            btn.config(command=lambda args=(first, second, btn): self.winner(args[0], args[1], args[2]))
            count += 1

    def border_settings(self):
        settings = Toplevel(master=self)
        settings.geometry("300x300")
        Label(master=settings, text="Сетка").grid(row=0, column=0)
        Checkbutton(master=settings, command=self.border_set).grid(row=0, column=1)

    def border_set(self):
        for col in range(16):
            for row in range(16):
                if BattleWindow.BORDER:
                    self.fields[col][row].config(borderwidth=0)
                else:
                    self.fields[col][row].config(borderwidth=1)

        BattleWindow.BORDER = True if not BattleWindow.BORDER else False

    def start(self):
        column = 0
        row = 0

        for pair in grids[int(self.number)].ATHLETE_LIST:
            first_atl = InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=pair[0])
            first_atl.grid(row=row, column=0)
            first = pair[0]

            # To Data Base (Info Button)
            self.data_base[f"{0}x{row}"]["type"] = "InfoButton"
            self.data_base[f"{0}x{row}"]["Athlete"] = pair[0].toJson()

            second_atl = InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=pair[1])
            second_atl.grid(row=row + 2, column=0)
            second = pair[1]

            # To Data Base (Second Info Button)
            self.data_base[f"{0}x{row + 2}"]["type"] = "InfoButton"
            self.data_base[f"{0}x{row + 2}"]["Athlete"] = pair[1].toJson()

            # Versus Button Create
            btn = self.fields[column][row + 1]

            btn = VersusButton(master=self.canvas_frame, root_win=self.root_win)
            # TODO TESTER MODE
            # btn.tester_mode()
            self.fields[column][row + 1] = btn
            btn.grid(row=row + 1, column=column)
            btn.config(command=lambda args=(first, second, btn): self.winner(args[0], args[1], args[2]))
            btn.grid(row=row + 1, column=column)
            self.VERSUS_BUTTONS.append(btn)
            row += 4

            # To Data Base (Versus Button)
            self.data_base[f"{btn.grid_info()['column']}x{btn.grid_info()['row']}"]["type"] = "VersusButton"
            self.data_base[f"{btn.grid_info()['column']}x{btn.grid_info()['row']}"]["info"] = {"scores": btn.SCORES,
                                                                                               "warns": btn.WARNS,
                                                                                               "observ": btn.OBSERV,
                                                                                               "knocks": btn.KNOCK,
                                                                                               "outs": btn.OUT,
                                                                                               "auto_win": btn.AUTO_WIN,
                                                                                               "state": "disabled",
                                                                                               "row": btn.grid_info()[
                                                                                                   "row"],
                                                                                               "col": btn.grid_info()[
                                                                                                   "column"],
                                                                                               "space": 1,
                                                                                               }

        first_vs_btn = self.VERSUS_BUTTONS[self.CURRENT_VERSUS]
        first_vs_btn.config(state="normal")

        self.data_base[f"{first_vs_btn.grid_info()['column']}x{first_vs_btn.grid_info()['row']}"]["info"][
            "state"] = "normal"

        self.COLUMN += 1
        self.SPACES = self.SPACES + self.COLUMN + 1

    def winner(self, first: Athlete, second: Athlete, btn: VersusButton):
        # Если программа находит две победы, то блокирует кнопку и выводит победителя вперед
        first_scores = 0
        second_scores = 0

        if btn.AUTO_WIN is not None:
            self.check_winner(btn.AUTO_WIN, btn)
            return

        for btl_round in ("0", "1", "2"):
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
        new_btn = InfoButton(master=self.canvas_frame, root_win=self.root_win, hover_color="GREEN", info=athlete)
        new_btn.grid(row=btn.grid_info()["row"], column=btn.grid_info()["column"] + 1)
        self.fields[btn.grid_info()["column"] + 1][btn.grid_info()["row"]] = new_btn

        # To Data Base
        self.data_base[f"{new_btn.grid_info()['column']}x{new_btn.grid_info()['row']}"]["type"] = "InfoButton"
        self.data_base[f"{new_btn.grid_info()['column']}x{new_btn.grid_info()['row']}"]["Athlete"] = athlete

        if self.COLUMN_MEMBERS != 0:
            self.check_column()
            self.COLUMN_MEMBERS -= 1
        else:
            self.COLUMN += 1
            self.SPACES = 2 ** self.COLUMN
            self.COLUMN_MEMBERS = (self.MEMBERS // (2 ** self.COLUMN)) - 1
            self.CURRENT_GRID = 0

        try:
            current_vs_btn = self.VERSUS_BUTTONS[self.CURRENT_VERSUS]
            next_vs_btn = self.VERSUS_BUTTONS[self.CURRENT_VERSUS + 1]

            current_vs_btn.config(state="disabled")
            next_vs_btn.config(state="normal")
            self.CURRENT_VERSUS += 1

            # To Data Base
            self.data_base[f"{current_vs_btn.grid_info()['column']}x{current_vs_btn.grid_info()['row']}"]["info"][
                "state"] = "disabled"

            self.data_base[f"{next_vs_btn.grid_info()['column']}x{next_vs_btn.grid_info()['row']}"]["info"][
                "state"] = "normal"

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
                        battle_btn = VersusButton(master=self.canvas_frame, root_win=self.root_win)
                        # TODO TESTER MODE
                        # battle_btn.tester_mode()
                        self.fields[self.COLUMN][abs(under_row - self.SPACES)] = battle_btn
                        battle_btn.config(
                            command=lambda args=(first_btn.info, second_btn.info, battle_btn): self.winner(args[0],
                                                                                                           args[1],
                                                                                                           args[2]))
                        battle_btn.grid(row=abs(under_row - self.SPACES), column=self.COLUMN)
                        self.VERSUS_BUTTONS.append(battle_btn)

                        # To Data Base
                        self.data_base[f"{battle_btn.grid_info()['column']}x{battle_btn.grid_info()['row']}"] = {}
                        self.data_base[f"{battle_btn.grid_info()['column']}x{battle_btn.grid_info()['row']}"][
                            "type"] = "VersusButton"
                        self.data_base[f"{battle_btn.grid_info()['column']}x{battle_btn.grid_info()['row']}"][
                            "info"] = {
                            "scores": battle_btn.SCORES,
                            "warns": battle_btn.WARNS,
                            "observ": battle_btn.OBSERV,
                            "knocks": battle_btn.KNOCK,
                            "outs": battle_btn.OUT,
                            "auto_win": battle_btn.AUTO_WIN,
                            "state": "disabled",
                            "row": battle_btn.grid_info()["row"],
                            "col": battle_btn.grid_info()["column"],
                            "space": self.SPACES
                        }

                        battle_btn = self.fields[self.COLUMN][abs(under_row - self.SPACES)]

                        battle_btn.config(text="БОЙ", state="normal", cursor="hand2", fg="#fff",
                                          command=lambda
                                              args=(first_btn.info, second_btn.info, battle_btn): self.winner(args[0],
                                                                                                              args[1],
                                                                                                              args[2]
                                                                                                              ))
                        self.CURRENT_GRID = under_row + 1

                        self.root_win.set_dbw(number=self.number, data={"DIRECTION": self.DIRECTION,
                                                                        "MEMBERS": self.MEMBERS,
                                                                        "COLUMN": self.COLUMN,
                                                                        "SPACES": self.SPACES,
                                                                        "CURRENT_GRID": self.CURRENT_GRID,
                                                                        "COLUMN_MEMBERS": self.COLUMN_MEMBERS,
                                                                        "BORDER": self.BORDER,
                                                                        # "VERSUS_BUTTONS": self.VERSUS_BUTTONS,
                                                                        "CURRENT_VERSUS": self.CURRENT_VERSUS
                                                                        })

                        print("DIRECTION:", self.DIRECTION)
                        print("MEMBERS:", self.MEMBERS)
                        print("COLUMN:", self.COLUMN)
                        print("SPACES:", self.SPACES)
                        print("CURRENT_GRID:", self.CURRENT_GRID)
                        print("COLUMN_MEMBERS:", self.COLUMN_MEMBERS)
                        print("BORDER:", self.BORDER)
                        print("VERSUS_BUTTONS:", self.VERSUS_BUTTONS)
                        print("CURRENT_VERSUS:", self.CURRENT_VERSUS)

                        return
