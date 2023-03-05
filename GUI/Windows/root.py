from tkinter import *
from GUI.Buttons import NavigationButton
from GUI.Buttons import InfoButton
from .battlepane import *


class RootWindow:
    right_panels = []
    current_panel = 0

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

        # Grid option
        self.grids = Menu(self.menu_bar)
        self.grids.add_command(label="1", command=lambda: self.swap_grid(0))
        # self.grids.add_command(label="2", command=lambda: self.swap_grid(1))
        # self.grids.add_command(label="3", command=lambda: self.swap_grid(2))
        self.menu_bar.add_cascade(label="Турниры", menu=self.grids)

        # self.root.resizable(width=False, height=False)

    def swap_grid(self, number):
        for child in self.root.winfo_children():
            if child.__class__.__name__ == "PanedWindow":
                pane: PanedWindow = PanedWindow(child)

                # pane.remove(self.right_panels[self.current_panel])
                # pane.add(self.right_panels[number])
                # self.right_panels[number].tkraise()
                # # self.right_panels[self.current_panel].destroy()
                # self.current_panel = number

                # pane.remove(self.right_panels[self.current_panel])
                self.right_panels[self.current_panel].clear()
                self.right_panels[self.current_panel].fill()

                # //// ТЕСТЫ ////
                # self.right_panels[self.current_panel].frame_killer()
                # self.right_panels[self.current_panel].grid_forget()
                # self.right_panels[number].grid(row=0, column=0, sticky="news")
                # self.right_panels[number].frame_filler()
                # self.current_panel = number
                # //// ТЕСТЫ ////

                # print(pane.winfo_children())
                break


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

battle_window1 = BattleWindow(master=work_space, root_win=window, number=0)
RootWindow.right_panels.append(battle_window1)
work_space.add(child=battle_window1)

# judge_btn.config(command=lambda: work_space.remove(battle_window1))

battle_window1.create_grid()
battle_window1.start()

# battle_window2 = BattleWindow(master=None, root_win=window, number=1)
# RootWindow.right_panels.append(battle_window2)
#
# battle_window2.create_grid()
# battle_window2.start()
#
# battle_window3 = BattleWindow(master=None, root_win=window, number=2)
# RootWindow.right_panels.append(battle_window3)
#
# battle_window3.create_grid()
# battle_window3.start()
#
# battle_window3 = BattleWindow(master=None, root_win=window, number=2)
# RootWindow.right_panels.append(battle_window3)
#
# battle_window3.create_grid()
# battle_window3.start()
#
# battle_window3 = BattleWindow(master=None, root_win=window, number=2)
# RootWindow.right_panels.append(battle_window3)
#
# battle_window3.create_grid()
# battle_window3.start()

# ОПТИМИЗАЦИЯ!!! - когда вызывается одно из окон, у старого стирается сетка!!! (противоположная функции create_grid)
