from tkinter import *
from GUI.Buttons import NavigationButton
from GUI.Buttons import InfoButton
from .battlepane import *


class RootWindow:
    def __init__(self):
        self.root = Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.config(background="#6C6C6C")
        self.root.title("Жеребьевка")
        self.root.geometry(
            f"{self.screen_width // 2}x{self.screen_height // 2}"
            f"+{self.screen_width // 4}+{int(self.screen_height // 5)}")

        # Menu bar
        self.menu_bar = Menu(master=self.root)
        self.root.config(menu=self.menu_bar)

        # Settings menu
        self.settings_menu = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="Settings", menu=self.settings_menu)

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

exit_btn = NavigationButton(master=btn_frame, text="Выход", root_win=window, hover_color="BLUE",
                            command=window.root.destroy)
exit_btn.grid(row=1, column=0, sticky="news")

judge_btn = NavigationButton(master=btn_frame, text="Судья", root_win=window, hover_color="BLUE", command=None)
judge_btn.grid(row=0, column=0, sticky="news")

work_space.grid_columnconfigure(index=0, minsize=window.screen_height // 4)
work_space.grid_rowconfigure(index=0, minsize=window.screen_height // 2)

# BATTLE FIELD (RIGHT PANEL)

battle_window = BattleWindow(master=work_space, root_win=window)
work_space.add(child=battle_window)


judge_btn.config(command=lambda: work_space.remove(battle_window))

battle_window.create_grid()
battle_window.start()
