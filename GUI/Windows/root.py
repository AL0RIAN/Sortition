from tkinter import *
from GUI.Buttons import NavigationButton
from GUI.Buttons import InfoButton
from .battlepane import *


class RootWindow:
    right_panels_grid = {x: {} for x in range(16)}
    right_panels = {x: {'direction': True,
                        'members': 16,
                        'column': 1,
                        'spaces': 2,
                        'cur_grid': 0,
                        'column_member': 8,
                        'border': False,
                        'cur_vs': 0} for x in range(16)}
    current_panel_num = 0
    current_panel = None

    def __init__(self):
        self.root = Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.config(background="#6C6C6C")
        self.root.title("Жеребьевка")
        self.root.geometry(
            f"{self.screen_width // 2}x{self.screen_height // 2}"
            f"+{self.screen_width // 4}+{int(self.screen_height // 5)}")

        # Pane
        self.right_panel = None

        # Menu bar
        self.menu_bar = Menu(master=self.root)
        self.root.config(menu=self.menu_bar)

        # Settings menu
        self.settings_menu = Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="Settings", menu=self.settings_menu)

        # Grid option
        self.grids = Menu(self.menu_bar)

        for grid in range(16):
            self.grids.add_command(label=f"{grid + 1}", command=lambda num=grid: self.swap_grid(num))

        # self.grids.add_command(label="1", command=lambda: self.swap_grid(0))
        # self.grids.add_command(label="2", command=lambda: self.swap_grid(1))
        # self.grids.add_command(label="3", command=lambda: self.swap_grid(2))
        self.menu_bar.add_cascade(label="Турниры", menu=self.grids)

        # self.root.resizable(width=False, height=False)

    def swap_grid(self, number):
        cur_num = self.current_panel_num
        dbg = self.right_panels_grid
        dbw = self.right_panels
        cur_pane = self.current_panel

        # Add Old Info To DB
        dbg[cur_num] = cur_pane.data_base
        dbw[cur_num] = cur_pane.get_grid_info()

        # Delete Old Pane
        self.right_panel.remove(cur_pane)
        cur_pane.destroy()

        print(dbg)
        print(dbw)

        # Add New Pane
        new_pane = BattleWindow(master=self.right_panel, root_win=self, number=2)
        new_pane.create_grid(db=dbg[number])
        new_pane.MEMBERS = dbw[number]["members"]
        new_pane.COLUMN = dbw[number]["column"]
        new_pane.SPACES = dbw[number]["spaces"]
        new_pane.CURRENT_GRID = dbw[number]["cur_grid"]
        new_pane.COLUMN_MEMBERS = dbw[number]["column_member"]
        new_pane.CURRENT_VERSUS = dbw[number]["cur_vs"]

        self.right_panel.add(new_pane)

        # Change Current Pane And Number
        RootWindow.current_panel_num = number
        RootWindow.current_panel = new_pane

        # self.right_panel.remove(self.current_panel)
        # self.right_panels[self.current_panel] =
        # self.current_panel.destroy()
        #
        # battle_window = BattleWindow(master=self.right_panel, root_win=self, number=number)
        # battle_window.create_grid(db=self.right_panel[number])
        #
        # self.right_panel.add(battle_window)
        #
        # self.right_panels[number] = battle_window.data_base
        #
        # self.current_panel = number

        # //// ТЕСТЫ ////
        # self.right_panels[self.current_panel].frame_killer()
        # self.right_panels[self.current_panel].grid_forget()
        # self.right_panels[number].grid(row=0, column=0, sticky="news")
        # self.right_panels[number].frame_filler()
        # self.current_panel = number
        # //// ТЕСТЫ ////

        # print(pane.winfo_children())
        # break


window = RootWindow()

# WORK SPACE CREATION

work_space = PanedWindow(master=window.root, background="#6C6C6C")
work_space.pack(fill=BOTH, expand=True)
window.right_panel = work_space

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
RootWindow.right_panels[0] = battle_window1.data_base
RootWindow.current_panel = battle_window1
work_space.add(child=battle_window1)
# judge_btn.config(command=lambda: work_space.remove(battle_window1))

battle_window1.create_grid(db={})

# for bw in range(15):
#     b = BattleWindow(master=None, root_win=window, number=2)
#     RootWindow.right_panels.append(b.data_base)

# НУЖНО ТЕПЕРЬ ХРАНИТЬ ДАННЫ ОБ ОТСТУПАХ И ТЕКУЩЕЙ КОЛОНКЕ
