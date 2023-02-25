__all__ = ["VersusWindow"]

from tkinter import *
from ..Buttons import ColorButton
from sorting.athlete import *

"""
Этот класс будет представлять топ левел окно противостояния двух бойцов.

Он принимает в себя два экземпляра класса Атлетов и делит.
"""


class VersusWindow(Toplevel):
    first: Athlete = None
    second: Athlete = None
    current_frame = None
    call_btn = None
    frames = list()
    wins = {first: 0, second: 0}
    WIDTH = 0
    HEIGHT = 0

    def __init__(self, master, root_win, first: Athlete, second: Athlete, call_btn: Button, current_frame):
        super().__init__(master=master)
        self.geometry(f"{master.winfo_width()}x{master.winfo_height()}")
        self.config(width=master.winfo_width(), height=master.winfo_height())
        self.title("Бой")
        self.resizable(False, False)
        self.root_win = root_win

        VersusWindow.current_frame = current_frame

        VersusWindow.first = first
        VersusWindow.second = second
        VersusWindow.WIDTH = master.winfo_width()
        VersusWindow.HEIGHT = master.winfo_height()
        VersusWindow.call_btn = call_btn

        VersusWindow.frames = [VersusFrame(self, first, second, call_btn, battle_round=battle) for battle in
                               range(0, 3)]

        for btn in VersusWindow.frames:
            if btn.battle_round != VersusWindow.current_frame:
                btn.plus_btn_left.config(state="disabled")
                btn.plus_btn_right.config(state="disabled")
                btn.minus_btn_left.config(state="disabled")
                btn.minus_btn_right.config(state="disabled")

        VersusWindow.frames[self.current_frame].place(width=master.winfo_width())

        # first_power.set(10)

        btn1 = ColorButton(master=self, root_win=self.root_win, hover_color="GREEN", start_bg="#D9D9D9")
        btn2 = ColorButton(master=self, root_win=self.root_win, hover_color="GREEN", start_bg="#D9D9D9")
        btn3 = ColorButton(master=self, root_win=self.root_win, hover_color="GREEN", start_bg="#D9D9D9")

        btn1.config(text="1", command=lambda: self.swap(0))
        btn1.place(x=master.winfo_width() / 2 - 40, y=master.winfo_height() - 40)

        btn2.config(text="2", command=lambda: self.swap(1))
        btn2.place(x=master.winfo_width() / 2, y=master.winfo_height() - 40)

        btn3.config(text="3", command=lambda: self.swap(2))
        btn3.place(x=master.winfo_width() / 2 + 40, y=master.winfo_height() - 40)

        self.grab_set()

    @staticmethod
    def swap(index):
        VersusWindow.frames[VersusWindow.current_frame].place_forget()
        VersusWindow.frames[index].place(width=VersusWindow.WIDTH)
        VersusWindow.current_frame = index


class VersusFrame(Frame):
    def __init__(self, master: VersusWindow, first_athlete: Athlete, second_athlete: Athlete, call_btn: Button,
                 battle_round: int):
        super().__init__(master=master)
        self.first_athlete = first_athlete
        self.second_athlete = second_athlete
        self.battle_round = battle_round

        for row in range(5):
            for col in range(5):
                Button(master=self, borderwidth=0, state="disabled", background="#D9D9D9").grid(row=row,
                                                                                                column=col,
                                                                                                sticky="news")
        for row in range(5):
            self.grid_columnconfigure(index=row, minsize=self.master.master.winfo_width() / 5)
            self.grid_rowconfigure(index=row, minsize=self.master.master.winfo_height() / 5)

        # Left Athlete Label
        self.left_name = Label(master=self, text=f"{first_athlete.name}", font=("Montserrat", 15, "bold"),
                               background="#D9D9D9", fg=VersusWindow.call_btn.SCORES[self.battle_round][2])
        self.left_name.grid(row=0, column=0, columnspan=2)

        # Versus Label
        Label(master=self, text=f"VS{battle_round + 1}", font=("Montserrat", 15, "bold"), fg="#DE5C5C",
              background="#D9D9D9").grid(row=0, column=2)

        # Right Athlete Label
        self.right_name = Label(master=self, text=f"{second_athlete.name}", font=("Montserrat", 15, "bold"),
                                background="#D9D9D9", fg=VersusWindow.call_btn.SCORES[self.battle_round][3])
        self.right_name.grid(row=0, column=3, columnspan=2)

        # Score Variables
        first_score = IntVar(value=VersusWindow.call_btn.SCORES[self.battle_round][0])
        second_score = IntVar(value=VersusWindow.call_btn.SCORES[self.battle_round][1])

        Label(master=self, textvariable=first_score, font=("Montserrat", 15, "bold"),
              background="#D9D9D9").grid(row=1, column=0, columnspan=2)
        Label(master=self, textvariable=second_score, font=("Montserrat", 15, "bold"),
              background="#D9D9D9").grid(row=1, column=3, columnspan=2)

        self.plus_btn_left = Button(master=self, text="+", borderwidth=0, font=("Montserrat", 25, "bold"),
                                    command=lambda: self.plus(first_athlete, first_score, 0), background="#D9D9D9")
        self.plus_btn_left.grid(row=2, column=0)

        self.minus_btn_left = Button(master=self, text="-", borderwidth=0, font=("Montserrat", 25, "bold"),
                                     command=lambda: self.minus(first_athlete, first_score, 0), background="#D9D9D9")
        self.minus_btn_left.grid(row=2, column=1)

        self.plus_btn_right = Button(master=self, text="+", borderwidth=0, font=("Montserrat", 25, "bold"),
                                     command=lambda: self.plus(second_athlete, second_score, 1), background="#D9D9D9")
        self.plus_btn_right.grid(row=2, column=3)

        self.minus_btn_right = Button(master=self, text="-", borderwidth=0, font=("Montserrat", 25, "bold"),
                                      command=lambda: self.minus(second_athlete, second_score, 1), background="#D9D9D9")
        self.minus_btn_right.grid(row=2, column=4)

        self.define = Button(master=self, text="Определить", borderwidth=0, font=("Montserrat", 15, "bold"),
                             command=lambda: self.check_winner(),
                             background="#D9D9D9")
        self.define.grid(row=3, column=0, columnspan=5)

    def plus(self, athlete: Athlete, current_score: IntVar, athlete_side):
        current_score.set(current_score.get() + 1)

        if athlete_side == 0:
            VersusWindow.call_btn.SCORES[self.battle_round][0] = current_score.get()
        else:
            VersusWindow.call_btn.SCORES[self.battle_round][1] = current_score.get()

    def minus(self, athlete: Athlete, current_score: IntVar, athlete_side):
        if current_score.get() - 1 != -1:
            current_score.set(current_score.get() - 1)

            if athlete_side == 0:
                VersusWindow.call_btn.SCORES[self.battle_round][0] = current_score.get()
            else:
                VersusWindow.call_btn.SCORES[self.battle_round][1] = current_score.get()

    def check_winner(self):
        if VersusWindow.call_btn.SCORES[self.battle_round][0] == VersusWindow.call_btn.SCORES[self.battle_round][1]:
            return
        elif VersusWindow.call_btn.SCORES[self.battle_round][0] > VersusWindow.call_btn.SCORES[self.battle_round][1]:
            VersusWindow.call_btn.SCORES[self.battle_round][2] = "#3fd44e"
            self.left_name.config(fg="#3fd44e")
        else:
            self.right_name.config(fg="#3fd44e")
            VersusWindow.call_btn.SCORES[self.battle_round][3] = "#3fd44e"

        self.plus_btn_left.config(state="disabled")
        self.plus_btn_right.config(state="disabled")
        self.minus_btn_left.config(state="disabled")
        self.minus_btn_right.config(state="disabled")
        self.define.config(state="disabled")

        try:
            next_button = VersusWindow.frames[self.battle_round + 1]
            next_button.plus_btn_left.config(state="normal")
            next_button.plus_btn_right.config(state="normal")
            next_button.minus_btn_left.config(state="normal")
            next_button.minus_btn_right.config(state="normal")
            next_button.define.config(state="normal")
            VersusWindow.swap(self.battle_round)
            VersusWindow.call_btn.SCORES[self.battle_round][2] = "#3fd44e"
            VersusWindow.call_btn.CURRENT_ROUND += 1
        except IndexError:
            return


