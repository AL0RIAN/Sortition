from tkinter import *
from GUI.Buttons import NavigationButton
from GUI.Buttons import InfoButton
from .battlepane import *


class RootWindow:
    root = Tk()

    def __init__(self):
        self.screen_width = RootWindow.root.winfo_screenwidth()
        self.screen_height = RootWindow.root.winfo_screenheight()
        RootWindow.root.config(background="#6C6C6C")
        RootWindow.root.title("Жеребьевка")
        RootWindow.root.geometry(
            f"{self.screen_width // 2}x{self.screen_height // 2}"
            f"+{self.screen_width // 4}+{int(self.screen_height // 5)}")
        # RootWindow.root.resizable(width=False, height=False)


window = RootWindow()

# WORK SPACE CREATION

work_space = PanedWindow(master=window.root, background="#6C6C6C")
work_space.pack(fill=BOTH, expand=True)

# NAVIGATION (LEFT PANEL)

navigation_window = PanedWindow(master=work_space, background="#F8F5F5", width=window.screen_width // 8)
work_space.add(child=navigation_window)

btn_frame = Frame(master=navigation_window, background="#F8F5F5", width=window.screen_width)
btn_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

NavigationButton(master=btn_frame, text="Выход", root_win=window.root, hover_color="BLUE",
                 command=window.root.destroy).grid(row=0,
                                                   column=0,
                                                   sticky="news")

work_space.grid_columnconfigure(index=0, minsize=window.screen_height // 4)
work_space.grid_rowconfigure(index=0, minsize=window.screen_height // 2)

# BATTLE FIELD (RIGHT PANEL)

battle_window = BattleWindow(master=work_space, root_win=RootWindow.root)
work_space.add(child=battle_window)

battle_window.create_grid()
battle_window.start()


