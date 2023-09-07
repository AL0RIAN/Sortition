__all__ = ["TopLevelMembers"]

from tkinter import ttk
from tkinter import *

from sorting.athlete_sort import *
from ..Buttons.colorbtn import *
from .battlegrid import *


class TopLevelMembers(Toplevel):
    """
    Этот класс нужен для реализации окна №2 (см. макет). Его роль в выводе и редактировании участников и в последующей конвертации
    в Ворд-документ.
    """

    def __init__(self, master, root_win):
        super().__init__(master)

        # Список Вводимых Полей
        values = dict()
        values["name"] = self.get_info_from_parser("name")
        values["birthday"] = self.get_info_from_parser("birthday")
        values["category"] = self.get_info_from_parser("category")
        values["gender"] = self.get_info_from_parser("gender")
        values["weight"] = self.get_info_from_parser("weight")
        values["is_sanda"] = self.get_info_from_parser("is_sanda")
        values["is_cinda"] = self.get_info_from_parser("is_cinda")
        values["is_tuishou"] = self.get_info_from_parser("is_tuishou")
        values["is_vinchun"] = self.get_info_from_parser("is_vinchun")
        values["region"] = self.get_info_from_parser("region")
        values["club"] = self.get_info_from_parser("club")
        values["trainer"] = self.get_info_from_parser("trainer")

        # Список виджетов, где +6 - Label'ы с категориями
        self.entries = {row: list() for row in range(len(values["name"]) + 6)}

        self.resizable(width=False, height=False)
        self.root_win = root_win

        # Main Frame
        self.main_frame = Frame(master=self)
        self.main_frame.pack(fill=BOTH, expand=1)
        self.second_frame = Frame()

        # Создаем Шапку и Подвал
        self.create_header()
        self.create_footer()
        self.create_work_space()

        row = 0
        member_num = 0
        for data in parser_data['participants']:
            label = Label(master=self.second_frame, text=data["age_category"])
            label.grid(row=row, column=0, sticky="news", columnspan=12)
            btn = ColorButton(master=self.second_frame, root_win=self.root_win, hover_color="RED", start_bg="#fff")
            btn.config(text="+", font=("Montserrat", 15, "bold"))
            btn.config(command=lambda args=(row, btn): self.add_row(row=args[0] + 1, button=args[1]))
            btn.grid(row=row, column=12)
            self.entries[row].append(label)
            row += 1
            for _ in data["data"]:
                self.fill_row(values, member_num, row)

                row += 1
                member_num += 1

    def delete_row(self, row: int, button: Button):
        for number in range(12):
            for widget in self.second_frame.winfo_children():
                if (type(widget) == Entry) and (str(widget.cget("textvariable")) == str(self.entries[row][number])):
                    widget.grid_forget()

        button.grid_forget()

        if row == len(self.entries) - 1:
            self.entries.pop(row)
        else:
            for key in range(row, len(self.entries.keys()) - 1):
                self.entries[key] = self.entries[key + 1]
            self.entries.pop(len(self.entries.keys()) - 1)

        for key in self.entries.keys():
            if len(self.entries[key]) == 1:
                print(f"{key} - {self.entries[key][0].cget('text')}")
            else:
                print(f"{key} - {self.entries[key][0].get()}")
                btn = self.entries[key][12]
                btn.config(command=lambda args=(key, btn): self.delete_row(args[0], args[1]))

    def add_row(self, row: int, button: Button):
        # Пересоздавать поле. Копировать в новый словарь, пока не дойдет до нового
        # +7, а не +6, ибо добавляется новая строка
        new_entries = {row: list() for row in range(len(self.entries.keys()) + 1)}
        old_entries = self.entries
        self.entries = new_entries

        keys = list(old_entries.keys())
        keys.sort()

        # Текущий ключ в новом словаре
        current_key = 0

        # Добавляет в новый словарь ключ-значение до нужного рядка
        for key in keys:
            if key == row:
                break
            #     Создаем новые экземпляры Энтрис и Лейблов
            if len(old_entries[key]) == 1:
                new_entries[key] = [Label(text=old_entries[key][0].cget("text"))]
            else:
                new_entries[key] = old_entries[key]
            current_key += 1

        self.fill_row(dict(), 0, row)

        for key in range(current_key, len(keys)):
            if len(old_entries[key]) == 1:
                new_entries[current_key + 1] = [Label(text=old_entries[key][0].cget("text"))]
            else:
                for var in old_entries[key]:
                    new_entries[current_key + 1].append(var)

            current_key += 1
        self.restart()

    def restart(self):
        self.destroy()
        super().__init__(master=self.master)

        self.resizable(width=False, height=False)

        # Main Frame
        self.main_frame = Frame(master=self)
        self.main_frame.pack(fill=BOTH, expand=1)
        self.second_frame = Frame()

        # Создаем Шапку И Подвал
        self.create_header()
        self.create_footer()
        self.create_work_space()

        row = 0

        for key in self.entries.keys():
            info = self.entries[key]
            # Если размер массив равен 1, то там находится только Лейбл категории
            if len(info) == 1:
                label = Label(master=self.second_frame, text=info[0].cget("text"))
                label.grid(row=row, column=1, columnspan=12, sticky="news")
                btn = ColorButton(master=self.second_frame, root_win=self.root_win, hover_color="RED", start_bg="#fff")
                btn.config(text="+", font=("Montserrat", 15, "bold"))
                btn.config(command=lambda args=(row, btn): self.add_row(row=args[0] + 1, button=args[1]))
                btn.grid(row=row, column=12)
            else:
                for col in range(12):
                    entry = Entry(master=self.second_frame, textvariable=info[col], justify=CENTER)
                    entry.grid(row=row, column=col, sticky="ns")

                btn = ColorButton(master=self.second_frame, root_win=self.root_win, hover_color="RED", start_bg="#fff")
                btn.config(text="X", font=("Montserrat", 10, "bold"))
                btn.config(command=lambda args=(row, btn): self.delete_row(args[0], args[1]))
                btn.grid(row=row, column=12, sticky="news")

                self.entries[row][12] = btn

            row += 1

    @staticmethod
    def get_info_from_parser(key: str):
        """
        Локальная функция. Получает информацию из парсера по ключу и добавляет в словарь в зависимости от рядка, где
        рядок - ключ, а значение этого ключа - список виджетов на этом рядке.

        :param key:
        :return:
        """
        result = list()

        for age_category in parser_data['participants']:
            for info in age_category["data"]:
                current = StringVar()
                current.set(info[key])
                result.append(current)

        return result

    def fill_row(self, value_list: dict, number, row) -> None:
        """

        :param value_list: словарь с соответствующими ключами: name, birthday, ..., trainer. Где значение - объект
                                класса StringVar
        :param entry_list:
        :param row:
        :param number: номер участника
        :return:
        """

        self.create_entry(variable=value_list.get("name", " ")[number], row=row, col=0, entry_list=self.entries)
        self.create_entry(variable=value_list.get("birthday", " ")[number], row=row, col=1, entry_list=self.entries)
        self.create_entry(variable=value_list.get("category", " ")[number], row=row, col=2, entry_list=self.entries)
        self.create_entry(variable=value_list.get("gender", " ")[number], row=row, col=3, entry_list=self.entries)
        self.create_entry(variable=value_list.get("weight", " ")[number], row=row, col=4, entry_list=self.entries)
        self.create_entry(variable=value_list.get("is_sanda", " ")[number], row=row, col=5, entry_list=self.entries)
        self.create_entry(variable=value_list.get("is_cinda", " ")[number], row=row, col=6, entry_list=self.entries)
        self.create_entry(variable=value_list.get("is_tuishou", " ")[number], row=row, col=7, entry_list=self.entries)
        self.create_entry(variable=value_list.get("is_vinchun", " ")[number], row=row, col=8, entry_list=self.entries)
        self.create_entry(variable=value_list.get("region", " ")[number], row=row, col=9, entry_list=self.entries)
        self.create_entry(variable=value_list.get("club", " ")[number], row=row, col=10, entry_list=self.entries)
        self.create_entry(variable=value_list.get("trainer", " ")[number], row=row, col=11, entry_list=self.entries)

        btn = ColorButton(master=self.second_frame, root_win=self.root_win, hover_color="RED", start_bg="#fff")
        btn.config(text="X", font=("Montserrat", 10, "bold"))
        btn.config(command=lambda args=(row, btn): self.delete_row(args[0], args[1]))
        btn.grid(row=row, column=12, sticky="news")

        self.entries[row].append(btn)

    def create_work_space(self):
        # Canvas
        canvas = Canvas(self.main_frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        canvas.config(height=750)

        # Scrollbar
        vertical_scrollbar = ttk.Scrollbar(master=self.main_frame, orient=VERTICAL, command=canvas.yview)
        vertical_scrollbar.pack(side=RIGHT, fill=Y)

        # Config Canvas
        canvas.configure(yscrollcommand=vertical_scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Another Frame inside the canvas
        self.second_frame = Frame(master=canvas)

        # Add That New Frame To A Window In The Canvas
        canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

    def create_header(self):
        header = Frame(self.main_frame)
        header.pack()

        names = ["Имя",
                 "Дата",
                 "Пол",
                 "Разряд",
                 "Категория",
                 "Саньда",
                 "Циньда",
                 "Туйшоу",
                 "Винчун",
                 "Город",
                 "Клуб",
                 "Тренер", ]

        for col in range(12):
            entry = Entry(master=header, textvariable=StringVar(value=names[col]), justify=CENTER)
            entry.grid(row=0, column=col, sticky="ns")

        # Кнопка с инструкцией
        Button(master=header, text="?", font=("Montserrat", 20, "bold")).grid(row=0, column=12)

    def create_footer(self):
        footer = Frame(self)
        footer.pack()
        Button(footer, text="Готово", font=("Montserrat", 20, "bold"), command=self.next_window).pack()

    def next_window(self):
        self.destroy()
        self.root_win.root.deiconify()
        BattleGrid(master=self.root_win.root)

    def create_entry(self, variable, entry_list, row, col, width=None) -> None:
        """
        Локальная функция. Создает Entry полее ввода в ТопЛевел окне со списком участников.

        :param variable:
        :param entry_list:
        :param row:
        :param col:
        :param width:
        """

        if variable == " ":
            variable = StringVar(value=" ")

        entry = Entry(master=self.second_frame, textvariable=variable, width=width, justify=CENTER)
        entry.grid(row=row, column=col, sticky="ns")

        # entry_list[row].append(entry.get())
        entry_list[row].append(variable)

    def save_info(self, entry_list: list, row_count):
        # TODO переделать: больше не передаются указатели на экземпляры, а просто строки
        """
        Сохраняет состояние поля и передает информацию конвертеру в ворд
    
        :param row_count: кол-во рядков
        :param entry_list: список Энтри
        :return:
        """
        result = {line: list() for line in range(row_count)}

        for widget in entry_list:
            if type(widget) == Label:
                result[widget.grid_info()["row"]].append(widget.cget("text"))
            else:
                result[widget.grid_info()["row"]].append(widget.get())
