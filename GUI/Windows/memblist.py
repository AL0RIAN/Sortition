__all__ = ["TopLevelMembers"]

from tkinter import *
from sorting.athlete_sort import *
from ..Buttons.colorbtn import *


class TopLevelMembers(Toplevel):
    """
    Этот класс нужен для реализации окна №2 (см. макет). Его роль в выводе и редактировании участников и в последующей конвертации
    в Ворд-документ.
    """

    def __init__(self, master, root_win):
        super().__init__(master)

        # self.resizable(width=False, height=False)
        self.root_win = root_win

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

        row = 0
        member_num = 0

        for data in parser_data['participants']:
            label = Label(master=self, text=data["age_category"])
            label.grid(row=row, column=0, sticky="news", columnspan=12)
            btn = ColorButton(master=self, root_win=self.root_win, hover_color="RED", start_bg="#fff")
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
            for widget in self.winfo_children():
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

        row = 0

        for key in self.entries.keys():
            info = self.entries[key]
            # Если размер массив равен 1, то там находится только Лейбл категории
            if len(info) == 1:
                label = Label(master=self, text=info[0].cget("text"))
                label.grid(row=row, column=1, columnspan=12, sticky="news")
                btn = ColorButton(master=self, root_win=self.root_win, hover_color="RED", start_bg="#fff")
                btn.config(text="+", font=("Montserrat", 15, "bold"))
                btn.config(command=lambda args=(row, btn): self.add_row(row=args[0] + 1, button=args[1]))
                btn.grid(row=row, column=12)
            else:
                Entry(master=self, textvariable=info[0]).grid(row=row, column=0, sticky="ns")
                Entry(master=self, textvariable=info[1]).grid(row=row, column=1, sticky="ns")
                Entry(master=self, textvariable=info[2]).grid(row=row, column=2, sticky="ns")
                Entry(master=self, textvariable=info[3]).grid(row=row, column=3, sticky="ns")
                Entry(master=self, textvariable=info[4]).grid(row=row, column=4, sticky="ns")
                Entry(master=self, textvariable=info[5]).grid(row=row, column=5, sticky="ns")
                Entry(master=self, textvariable=info[6]).grid(row=row, column=6, sticky="ns")
                Entry(master=self, textvariable=info[7]).grid(row=row, column=7, sticky="ns")
                Entry(master=self, textvariable=info[8]).grid(row=row, column=8, sticky="ns")
                Entry(master=self, textvariable=info[9]).grid(row=row, column=9, sticky="ns")
                Entry(master=self, textvariable=info[10]).grid(row=row, column=10, sticky="ns")
                Entry(master=self, textvariable=info[11]).grid(row=row, column=11, sticky="ns")

                btn = ColorButton(master=self, root_win=self.root_win, hover_color="RED", start_bg="#fff")
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

        btn = ColorButton(master=self, root_win=self.root_win, hover_color="RED", start_bg="#fff")
        btn.config(text="X", font=("Montserrat", 10, "bold"))
        btn.config(command=lambda args=(row, btn): self.delete_row(args[0], args[1]))
        btn.grid(row=row, column=12, sticky="news")

        print(len(self.entries[row]))
        self.entries[row].append(btn)

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

        entry = Entry(master=self, textvariable=variable, width=width)
        entry.grid(row=row, column=col, sticky="news")

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
