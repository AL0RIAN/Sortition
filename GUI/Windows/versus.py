__all__ = ["VersusWindow"]

from tkinter import *
from ..Buttons import ColorButton
from ..athlete import *

FIRST = 0
SECOND = 1

"""
Этот класс будет представлять топ левел окно противостояния двух бойцов.

Он принимает в себя два экземпляра класса Атлетов и делит.
"""


# TODO настроить логику кнопок

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
        self.config(width=master.winfo_width(), height=master.winfo_height(), background="#D9D9D9")
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

        VersusWindow.frames[self.current_frame].place(width=master.winfo_width())

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
        try:
            VersusWindow.frames[VersusWindow.current_frame].place_forget()
            VersusWindow.frames[index].place(width=VersusWindow.WIDTH)
            VersusWindow.current_frame = index
        except IndexError:
            return


class VersusFrame(Frame):
    # Список, чтобы за проход заблокировать кнопки
    BUTTONS = {"nav": list(), "members": list()}

    def __init__(self, master: VersusWindow, first_athlete: Athlete, second_athlete: Athlete, call_btn: Button,
                 battle_round: int):
        super().__init__(master=master)
        self.first_athlete = first_athlete
        self.second_athlete = second_athlete
        self.battle_round = battle_round
        self.IS_WIN = VersusWindow.call_btn.SCORES[self.battle_round][2]

        # Grid
        for row in range(11):
            for col in range(5):
                btn = Button(master=self, borderwidth=0, state="disabled", background="#D9D9D9")
                btn.grid(row=row, column=col, sticky="news")

        # Grid settings
        for row in range(5):
            self.grid_columnconfigure(index=row, minsize=self.master.master.winfo_width() / 5)
            self.grid_rowconfigure(index=row, minsize=self.master.master.winfo_height() / 5)

        # Left Athlete Label
        self.left_name = ColorButton(master=self, root_win=master.root_win, hover_color="BLUE", start_bg="#D9D9D9")
        self.left_name.config(fg="black", text=f"{first_athlete.name}")
        self.left_name.config(command=lambda button=self.left_name: self.create_info_win(button, FIRST))
        self.left_name.grid(row=0, column=0, columnspan=2)

        # Versus Label
        Label(master=self, text=f"VS{battle_round + 1}", font=("Montserrat", 15, "bold"), fg="#DE5C5C",
              background="#D9D9D9").grid(row=0, column=2)

        # Right Athlete Label
        self.right_name = ColorButton(master=self, root_win=master.root_win, hover_color="BLUE", start_bg="#D9D9D9")
        self.right_name.config(fg="black", text=f"{second_athlete.name}")
        self.right_name.config(command=lambda button=self.right_name: self.create_info_win(button, SECOND))
        self.right_name.grid(row=0, column=3, columnspan=2)

        if VersusWindow.call_btn.SCORES[self.battle_round][2]:
            self.check_winner()

        # Score Variables
        first_score = IntVar(value=VersusWindow.call_btn.SCORES[self.battle_round][0])
        second_score = IntVar(value=VersusWindow.call_btn.SCORES[self.battle_round][1])

        # Names Labels
        Label(master=self, textvariable=first_score, font=("Montserrat", 15, "bold"),
              background="#D9D9D9").grid(row=1, column=0, columnspan=2)
        Label(master=self, textvariable=second_score, font=("Montserrat", 15, "bold"),
              background="#D9D9D9").grid(row=1, column=3, columnspan=2)

        # Left Navigation
        # TODO доделать все кнопки по примеру add_btn
        add_btn = self.create_nav(text="Добавить")
        add_btn.config(command=lambda: self.plus(first_score, FIRST))
        add_btn.grid(row=2, column=0, columnspan=2)

        warn_btn = self.create_nav(text="Предупреждение")
        warn_btn.config(command=lambda: self.warn(first_score, second_score, athlete_side=FIRST))
        warn_btn.grid(row=3, column=0, columnspan=2)

        observ_btn = self.create_nav(text="Замечание")
        observ_btn.config(command=lambda: self.observ(first_score, second_score, athlete_side=FIRST))
        observ_btn.grid(row=4, column=0, columnspan=2)

        # self.minus_btn_left = Button(master=self, text="Попередження", borderwidth=0, font=("Montserrat", 15, "bold"),
        #                              command=lambda: self.warn(first_score, "TOP"), background="#D9D9D9")
        # self.minus_btn_left.grid(row=3, column=0, columnspan=2)

        # self.minus_btn_left = Button(master=self, text="Замечания", borderwidth=0, font=("Montserrat", 15, "bold"),
        #                              command=lambda: self.minus(first_athlete, first_score, 0), background="#D9D9D9")
        # self.minus_btn_left.grid(row=4, column=0, columnspan=2)
        #
        # self.minus_btn_left = Button(master=self, text="Примусовий звіт", borderwidth=0,
        #                              font=("Montserrat", 15, "bold"),
        #                              command=lambda: self.minus(first_athlete, first_score, 0), background="#D9D9D9")
        # self.minus_btn_left.grid(row=5, column=0, columnspan=2)
        #
        # self.minus_btn_left = Button(master=self, text="Вихід за майданчик", borderwidth=0,
        #                              font=("Montserrat", 15, "bold"),
        #                              command=lambda: self.minus(first_athlete, first_score, 0), background="#D9D9D9")
        # self.minus_btn_left.grid(row=6, column=0, columnspan=2)
        #
        # # Right Navigation
        # self.plus_btn_right = Button(master=self, text="Добавить", borderwidth=0, font=("Montserrat", 15, "bold"),
        #                              command=lambda: self.plus(second_athlete, second_score, 1), background="#D9D9D9")
        # self.plus_btn_right.grid(row=2, column=3, columnspan=2)
        #
        # self.minus_btn_right = Button(master=self, text="Попередження", borderwidth=0, font=("Montserrat", 15, "bold"),
        #                               command=lambda: self.minus(second_athlete, second_score, 1), background="#D9D9D9")
        # self.minus_btn_right.grid(row=3, column=3, columnspan=2)
        #
        # self.minus_btn_right = Button(master=self, text="Замечания", borderwidth=0, font=("Montserrat", 15, "bold"),
        #                               command=lambda: self.minus(second_athlete, second_score, 1), background="#D9D9D9")
        # self.minus_btn_right.grid(row=4, column=3, columnspan=2)
        #
        # self.minus_btn_right = Button(master=self, text="Примусовий звіт", borderwidth=0,
        #                               font=("Montserrat", 15, "bold"),
        #                               command=lambda: self.minus(second_athlete, second_score, 1), background="#D9D9D9")
        # self.minus_btn_right.grid(row=5, column=3, columnspan=2)
        #
        # self.minus_btn_right = Button(master=self, text="Вихід за майданчик", borderwidth=0,
        #                               font=("Montserrat", 15, "bold"),
        #                               command=lambda: self.minus(second_athlete, second_score, 1), background="#D9D9D9")
        # self.minus_btn_right.grid(row=6, column=3, columnspan=2)

        # Col and Row settings

        self.rowconfigure(index=2, minsize=10)
        self.rowconfigure(index=3, minsize=10)
        self.rowconfigure(index=4, minsize=10)
        self.rowconfigure(index=5, minsize=10)
        self.rowconfigure(index=6, minsize=10)

        # Define Button
        self.define = Button(master=self, text="Определить", borderwidth=0, font=("Montserrat", 15, "bold"),
                             command=lambda: self.check_winner(),
                             background="#D9D9D9")
        self.define.grid(row=7, column=0, columnspan=5)

    def create_info_win(self, call_btn: Button, athlete_side: int):
        info_win = Toplevel(master=call_btn)
        info_win.geometry("300x400")
        info_win.title(f"{call_btn['text']}")

        scores = VersusWindow.call_btn.SCORES[self.battle_round][athlete_side]
        warns = VersusWindow.call_btn.WARNS[self.battle_round][athlete_side]
        observ = VersusWindow.call_btn.OBSERV[self.battle_round][athlete_side]

        Label(master=info_win, text=f"Очки: {scores}").pack()
        Label(master=info_win, text=f"Предупреждения: {warns}").pack()
        Label(master=info_win, text=f"Замечания: {observ}").pack()

    def create_nav(self, text: str) -> Button:
        btn = Button(master=self, text=text, borderwidth=0, font=("Montserrat", 15, "bold"), background="#D9D9D9")
        VersusFrame.BUTTONS["nav"].append(btn)
        return btn

    def plus(self, current_score: IntVar, athlete_side):
        current_score.set(current_score.get() + 1)

        if athlete_side == 0:
            VersusWindow.call_btn.SCORES[self.battle_round][0] = current_score.get()
        else:
            VersusWindow.call_btn.SCORES[self.battle_round][1] = current_score.get()

    def warn(self, current_score_first: IntVar, current_score_second: IntVar, athlete_side: int):
        """

        :param current_score_first:
        :param current_score_second:
        :param athlete_side: FIRST or SECOND
        :return:
        """

        if athlete_side == FIRST:
            current_score_second.set(current_score_second.get() + 2)
            VersusWindow.call_btn.SCORES[self.battle_round][SECOND] = current_score_second.get()
            VersusWindow.call_btn.WARNS[self.battle_round][FIRST] += 1
        elif athlete_side == SECOND:
            current_score_first.set(current_score_first.get() + 2)
            VersusWindow.call_btn.SCORES[self.battle_round][FIRST] = current_score_first.get()
            VersusWindow.call_btn.WARNS[self.battle_round][SECOND] += 1

        self.check_penalty()

    def observ(self, current_score_first: IntVar, current_score_second: IntVar, athlete_side: int):
        """

        :param current_score_first:
        :param current_score_second:
        :param athlete_side:
        :return:
        """

        if athlete_side == FIRST:
            current_score_second.set(current_score_second.get() + 1)
            VersusWindow.call_btn.SCORES[self.battle_round][SECOND] = current_score_second.get()
            VersusWindow.call_btn.OBSERV[self.battle_round][FIRST] += 1
        elif athlete_side == SECOND:
            current_score_first.set(current_score_first.get() + 1)
            VersusWindow.call_btn.SCORES[self.battle_round][FIRST] = current_score_first.get()
            VersusWindow.call_btn.OBSERV[self.battle_round][SECOND] += 1

    def check_penalty(self):
        if VersusWindow.call_btn.WARNS[self.battle_round][FIRST] == 3:
            self.check_winner(autowin_bottom=True)

        if VersusWindow.call_btn.WARNS[self.battle_round][SECOND] == 3:
            self.check_winner(autowin_top=True)

    def check_winner(self, autowin_top: bool = False, autowin_bottom: bool = False):
        """

        :param autowin_top:
        :param autowin_bottom:
        :return:
        """

        first_score = VersusWindow.call_btn.SCORES[self.battle_round][0]
        second_score = VersusWindow.call_btn.SCORES[self.battle_round][1]

        if first_score == second_score:
            return
        elif first_score > second_score or autowin_top:
            self.left_name.config(fg="#3fd44e")
        elif first_score < second_score or autowin_bottom:
            self.right_name.config(fg="#3fd44e")

        VersusWindow.call_btn.SCORES[self.battle_round][2] = True

        VersusWindow.call_btn.CURRENT_ROUND += 1

        for child in self.winfo_children():
            if child.__class__.__name__ == "Button":
                child.configure(state="disabled")

        # self.plus_btn_left.config(state="disabled")
        # self.plus_btn_right.config(state="disabled")
        # self.minus_btn_left.config(state="disabled")
        # self.minus_btn_right.config(state="disabled")
        # self.define.config(state="disabled")

        # for btn in self.BUTTONS["nav"]:
        #     btn.configure(state="disabled")

            # for btn in VersusWindow.frames[1].BUTTONS:
            #     btn.config(state="normal")

            # VersusWindow.swap(self.battle_round + 1)

