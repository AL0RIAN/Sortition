__all__ = ["VersusWindow"]

from tkinter import *
from tkinter import messagebox
from ..Buttons import ColorButton
from sorting.athlete import *

FIRST = 0
SECOND = 1

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
        print(f"{master.winfo_width()}x{master.winfo_height()}")
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
            print(f"{index + 1} {VersusWindow.frames[VersusWindow.current_frame].IS_WIN}")
            VersusWindow.frames[VersusWindow.current_frame].place_forget()
            VersusWindow.frames[index].place(width=VersusWindow.WIDTH)
            VersusWindow.current_frame = index
        except IndexError:
            return

    @staticmethod
    def disable_frames():
        for frame in VersusWindow.frames:
            frame.disable_buttons()

    @staticmethod
    def color_rounds(athlete_side):
        for frame in VersusWindow.frames:
            if athlete_side == FIRST:
                frame.left_name.config(fg="#3fd44e")
            if athlete_side == SECOND:
                frame.right_name.config(fg="#3fd44e")


class VersusFrame(Frame):
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
        Label(master=self, text=f"Раунд {battle_round + 1}", font=("Montserrat", 15, "bold"), fg="#DE5C5C",
              background="#D9D9D9").grid(row=0, column=2)

        # Right Athlete Label
        self.right_name = ColorButton(master=self, root_win=master.root_win, hover_color="BLUE", start_bg="#D9D9D9")
        self.right_name.config(fg="black", text=f"{second_athlete.name}")
        self.right_name.config(command=lambda button=self.right_name: self.create_info_win(button, SECOND))
        self.right_name.grid(row=0, column=3, columnspan=2)

        if VersusWindow.call_btn.SCORES[self.battle_round][2]:
            self.check_winner()

        # Score Variables
        self.first_score = IntVar(value=VersusWindow.call_btn.SCORES[self.battle_round][0])
        self.second_score = IntVar(value=VersusWindow.call_btn.SCORES[self.battle_round][1])

        # Names Labels
        Label(master=self, textvariable=self.first_score, font=("Montserrat", 15, "bold"),
              background="#D9D9D9").grid(row=1, column=0, columnspan=2)
        Label(master=self, textvariable=self.second_score, font=("Montserrat", 15, "bold"),
              background="#D9D9D9").grid(row=1, column=3, columnspan=2)

        # Left Navigation
        self.create_nav(FIRST)
        self.create_nav(SECOND)

        # Col and Row settings
        self.rowconfigure(index=2, minsize=10)
        self.rowconfigure(index=3, minsize=10)
        self.rowconfigure(index=4, minsize=10)
        self.rowconfigure(index=5, minsize=10)
        self.rowconfigure(index=6, minsize=10)

        # Define Button
        self.define = self.create_btn(text="Определить")
        self.define.config(command=lambda: self.check_winner())
        self.define.grid(row=7, column=0, columnspan=5)

    def create_info_win(self, call_btn: Button, athlete_side: int):
        info_win = Toplevel(master=call_btn)
        info_win.geometry("300x400")
        info_win.title(f"{call_btn['text']}")

        scores = VersusWindow.call_btn.SCORES[self.battle_round][athlete_side]
        warns = VersusWindow.call_btn.WARNS[athlete_side]
        observ = VersusWindow.call_btn.OBSERV[self.battle_round][athlete_side]
        outs = VersusWindow.call_btn.OUT[self.battle_round][athlete_side]
        knocks = VersusWindow.call_btn.KNOCK[self.battle_round][athlete_side]

        Label(master=info_win, text=f"Раунд {self.battle_round + 1}").pack()
        Label(master=info_win, text=f"Очки: {scores}").pack()
        Label(master=info_win, text=f"Предупреждения: {warns}").pack()
        Label(master=info_win, text=f"Замечания: {observ}").pack()
        Label(master=info_win, text=f"Нокдауны: {knocks}").pack()
        Label(master=info_win, text=f"Выходы за поле: {outs}").pack()

    def create_btn(self, text: str) -> Button:
        btn = Button(master=self, text=text, borderwidth=0, font=("Montserrat", 15, "bold"), background="#D9D9D9")
        return btn

    def create_nav(self, athlete_side: int):
        if athlete_side == FIRST:
            score = self.first_score
            col = 0
        elif athlete_side == SECOND:
            score = self.second_score
            col = 3
        else:
            raise ValueError

        add_btn = self.create_btn(text="Добавить")
        add_btn.config(command=lambda: self.plus(score, athlete_side))
        add_btn.grid(row=2, column=col, columnspan=2)

        warn_btn = self.create_btn(text="Предупреждение")
        warn_btn.config(command=lambda: self.warn(self.first_score, self.second_score, athlete_side=athlete_side))
        warn_btn.grid(row=3, column=col, columnspan=2)

        observ_btn = self.create_btn(text="Замечание")
        observ_btn.config(command=lambda: self.observ(self.first_score, self.second_score, athlete_side=athlete_side))
        observ_btn.grid(row=4, column=col, columnspan=2)

        knockdown_btn = self.create_btn(text="Нокдаун")
        knockdown_btn.config(
            command=lambda: self.knockdown(self.first_score, self.second_score, athlete_side=athlete_side))
        knockdown_btn.grid(row=5, column=col, columnspan=2)

        out_btn = self.create_btn(text="Граница")
        out_btn.config(command=lambda: self.out(self.first_score, self.second_score, athlete_side=athlete_side))
        out_btn.grid(row=5, column=col, columnspan=2)

    def plus(self, current_score: IntVar, athlete_side):
        current_vs_btn = VersusWindow.call_btn
        current_score.set(current_score.get() + 1)
        current_vs_btn.SCORES[self.battle_round][athlete_side] = current_score.get()

        self.check_penalty()

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
            VersusWindow.call_btn.WARNS[FIRST] += 1
        elif athlete_side == SECOND:
            current_score_first.set(current_score_first.get() + 2)
            VersusWindow.call_btn.SCORES[self.battle_round][FIRST] = current_score_first.get()
            VersusWindow.call_btn.WARNS[SECOND] += 1

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

    def knockdown(self, current_score_first: IntVar, current_score_second: IntVar, athlete_side: int):
        if athlete_side == FIRST:
            current_score_second.set(current_score_second.get() + 2)
            VersusWindow.call_btn.SCORES[self.battle_round][SECOND] = current_score_second.get()
            VersusWindow.call_btn.KNOCK[self.battle_round][FIRST] += 1
        elif athlete_side == SECOND:
            current_score_first.set(current_score_first.get() + 2)
            VersusWindow.call_btn.SCORES[self.battle_round][FIRST] = current_score_first.get()
            VersusWindow.call_btn.KNOCK[self.battle_round][SECOND] += 1

        self.check_penalty()

    def out(self, current_score_first: IntVar, current_score_second: IntVar, athlete_side: int):
        if athlete_side == FIRST:
            current_score_second.set(current_score_second.get() + 2)
            VersusWindow.call_btn.SCORES[self.battle_round][SECOND] = current_score_second.get()
            VersusWindow.call_btn.OUT[self.battle_round][FIRST] += 1
        elif athlete_side == SECOND:
            current_score_first.set(current_score_first.get() + 2)
            VersusWindow.call_btn.SCORES[self.battle_round][FIRST] = current_score_first.get()
            VersusWindow.call_btn.OUT[self.battle_round][SECOND] += 1

        self.check_penalty()

    def check_penalty(self):
        first_score = VersusWindow.call_btn.SCORES[self.battle_round][FIRST]
        first_warns = VersusWindow.call_btn.WARNS[FIRST]
        first_knocks = VersusWindow.call_btn.KNOCK[self.battle_round][FIRST]
        first_outs = VersusWindow.call_btn.OUT[self.battle_round][FIRST]

        second_score = VersusWindow.call_btn.SCORES[self.battle_round][SECOND]
        second_warns = VersusWindow.call_btn.WARNS[SECOND]
        second_knocks = VersusWindow.call_btn.KNOCK[self.battle_round][SECOND]
        second_outs = VersusWindow.call_btn.OUT[self.battle_round][SECOND]

        # For Data Base
        battle_window_db = self.master.master.data_base
        curr_vs_btn = VersusWindow.call_btn

        # Если Один Из Участников Набирает Три Предупреждения, Второй Побеждает Автоматом
        if first_warns == 3:
            VersusWindow.disable_frames()
            VersusWindow.color_rounds(SECOND)
            messagebox.showinfo(title="Победитель", message=f"{self.first_athlete.name} набирает три предупреждения!")
            VersusWindow.call_btn.AUTO_WIN = self.second_athlete

            battle_window_db[f"{curr_vs_btn.grid_info()['column']}x{curr_vs_btn.grid_info()['row']}"]["info"][
                "auto_win"] = self.second_athlete

        elif second_warns == 3:
            VersusWindow.disable_frames()
            VersusWindow.color_rounds(FIRST)
            messagebox.showinfo(title="Победитель", message=f"{self.second_athlete.name} набирает три предупреждения!")
            VersusWindow.call_btn.AUTO_WIN = self.first_athlete

            battle_window_db[f"{curr_vs_btn.grid_info()['column']}x{curr_vs_btn.grid_info()['row']}"]["info"][
                "auto_win"] = self.first_athlete

        if first_knocks == 2 or first_outs == 2 or (second_score - first_score) >= 12:
            self.check_winner(autowin_bottom=True)

        if second_knocks == 2 or second_outs == 2 or (first_score - second_score) >= 12:
            self.check_winner(autowin_top=True)

    def disable_buttons(self):
        for child in self.winfo_children():
            if child.__class__.__name__ == "Button":
                child.configure(state="disabled")

    def check_winner(self, autowin_top: bool = False, autowin_bottom: bool = False):
        """

        :param autowin_top:
        :param autowin_bottom:
        :return:
        """

        first_score = VersusWindow.call_btn.SCORES[self.battle_round][0]
        second_score = VersusWindow.call_btn.SCORES[self.battle_round][1]
        auto_winner = VersusWindow.call_btn.AUTO_WIN

        if first_score == second_score or self.IS_WIN:
            return
        elif first_score > second_score or autowin_top or auto_winner == self.first_athlete:
            self.left_name.config(fg="#3fd44e")
            VersusWindow.call_btn.CURRENT_ROUND += 1
        elif first_score < second_score or autowin_bottom or auto_winner == self.second_score:
            self.right_name.config(fg="#3fd44e")
            VersusWindow.call_btn.CURRENT_ROUND += 1

        current_vs_btn = VersusWindow.call_btn
        current_vs_btn.SCORES[self.battle_round][2] = True
        self.disable_buttons()

        if VersusWindow.current_frame < 2:
            VersusWindow.swap(self.battle_round + 1)
