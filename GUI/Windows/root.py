__all__ = ["window"]

from tkinter import *
from tkinter import filedialog
from .battlepane import *
from ..Buttons.navigationbtn import *
from .memblist import *
import json


class RootWindow:
    """
    right_panels_grid: информация о сетке, где x - номер поля
    right_panels: информация о поле, где x - номер поля
    current_panel_num: номер текущего поля
    current_panel: текущее поле
    opening: приветственное окно
    """

    right_panels_grid = {str(x): {"grid": {}, "spaces_info": {}} for x in range(16)}
    right_panels = {str(x): {'direction': True,
                             'members': 16,
                             'column': 1,
                             'spaces': 2,
                             'cur_grid': 0,
                             'column_member': 8,
                             'border': False,
                             'cur_vs': 0} for x in range(16)}
    current_panel_num = 0
    current_panel = None
    opening = None

    def __init__(self):
        self.root = Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.config(background="#6C6C6C")
        self.root.title("Жеребьевка")
        self.root.geometry(
            f"{self.screen_width // 2}x{self.screen_height // 2}"
            f"+{self.screen_width // 4}+{int(self.screen_height // 5)}")

        self.root.withdraw()
        self.opening_win()

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

        self.menu_bar.add_cascade(label="Турниры", menu=self.grids)

        # Обработчик Закрытия
        self.root.protocol("WM_DELETE_WINDOW", self.save)

    def swap_grid(self, number):
        cur_num = self.current_panel_num
        dbg = self.right_panels_grid["grid"]
        dbw = self.right_panels["spaces_info"]
        cur_pane = self.current_panel

        # Add Old Info To DB
        dbg[cur_num] = cur_pane.data_base
        dbw[cur_num] = cur_pane.get_grid_info()

        # Delete Old Pane
        self.right_panel.remove(cur_pane)
        cur_pane.destroy()

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

    def opening_win(self):
        RootWindow.opening = Toplevel(master=self.root)
        RootWindow.opening.geometry("500x500")
        Button(master=RootWindow.opening, text="Открыть", command=self.browse_file).pack()
        Button(master=RootWindow.opening, text="Создать", command=self.work_space_creation).pack()

    def browse_file(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Выберите файл",
                                              filetypes=(("Json File", "*.json"),))
        with open(filename, "r") as file:
            self.right_panels_grid = json.load(file)

        self.root.deiconify()
        self.work_space_creation()

    def work_space_creation(self):
        # names = get_info_from_parser("name")
        # birthday = get_info_from_parser("birthday")
        # gender = get_info_from_parser("gender")
        # categories = get_info_from_parser("category")
        #
        #
        # for number in range(len(names)):
        #     Entry(master=review_win, textvariable=names[number]).grid(row=number, column=0)
        #     Entry(master=review_win, textvariable=birthday[number]).grid(row=number, column=1)
        #     Entry(master=review_win, textvariable=gender[number]).grid(row=number, column=2)
        #     Entry(master=review_win, textvariable=categories[number]).grid(row=number, column=3)

        TopLevelMembers(master=self.root, root_win=self)

        # RootWindow.opening.destroy()

        # WORK SPACE CREATION
        # work_space = PanedWindow(master=self.root, background="#6C6C6C")
        # work_space.pack(fill=BOTH, expand=True)
        # window.right_panel = work_space
        #
        # # NAVIGATION (LEFT PANEL)
        #
        # navigation_window = PanedWindow(master=work_space, background="#F8F5F5", width=window.screen_width // 8)
        # work_space.add(child=navigation_window)
        #
        # btn_frame = Frame(master=navigation_window, background="#F8F5F5", width=window.screen_width)
        # btn_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        #
        # exit_btn = NavigationButton(master=btn_frame, text="Выход", root_win=window, hover_color="BLUE",
        #                             command=window.root.destroy)
        # exit_btn.grid(row=1, column=0, sticky="news")
        # judge_btn = NavigationButton(master=btn_frame, text="Судья", root_win=window, hover_color="BLUE", command=None)
        # judge_btn.grid(row=0, column=0, sticky="news")
        #
        # work_space.grid_columnconfigure(index=0, minsize=window.screen_height // 4)
        # work_space.grid_rowconfigure(index=0, minsize=window.screen_height // 2)
        #
        # # BATTLE FIELD (RIGHT PANEL)
        #
        # battle_window1 = BattleWindow(master=work_space, root_win=window, args=self.right_panels["0"], number="0")
        # RootWindow.current_panel = battle_window1
        # work_space.add(child=battle_window1)
        #
        # print(self.right_panels_grid["0"])
        # battle_window1.create_grid(self.right_panels_grid["0"]["grid"])
        # self.root.deiconify()

    @staticmethod
    def set_dbg(number: str, data: dict) -> None:
        """
        Этот метод нужен для обновления базы данных всякий раз, как происходят изменения на Поле (СЕТКА)

        :param number:
        :param data:
        :return:
        """

        RootWindow.right_panels_grid[number]["grid"] = data

    @staticmethod
    def set_dbw(number: str, data: dict) -> None:
        """
        Этот метод нужен для обновления базы данных всякий раз, как происходят изменения на Поле (ОТСТУПЫ И КОНФИГУРАЦИЯ)

        :param number:
        :param data:
        :return:
        """

        RootWindow.right_panels_grid[number]["spaces_info"] = data

    def save(self):
        with open("js-db.json", "w") as file:
            json.dump(self.right_panels_grid, file)

        self.root.destroy()


window = RootWindow()

# Сделать Сериализацию и Десирализацию
# Сделать начальные окна, как ТопЛевел. Пока инструкции в них не заданы, не выводить основное

# window.root.withdraw()
# window.root.deiconify()

# TODO добавить метод и кнопку, которые будут отвечать за поднятие поля при удалении одного из. Для этого
# TODO нужно добавить переменную поля, в которой будут храниться данные о полях.
