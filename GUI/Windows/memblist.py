__all__ = ["TopLevelMembers"]

from tkinter import *
from sorting.athlete_sort import *


class TopLevelMembers(Toplevel):
    """
    Этот класс нужен для реализации окна №2 (см. макет). Его роль в выводе и редактировании участников и в последующей конвертации
    в Ворд-документ.
    """

    def __init__(self, master):
        super().__init__(master)

        self.resizable(width=False, height=False)

        entries = list()
        name = self.get_info_from_parser("name")
        birthday = self.get_info_from_parser("birthday")
        category = self.get_info_from_parser("category")
        gender = self.get_info_from_parser("gender")
        weight = self.get_info_from_parser("weight")
        is_sanda = self.get_info_from_parser("is_sanda")
        is_cinda = self.get_info_from_parser("is_cinda")
        is_tuishou = self.get_info_from_parser("is_tuishou")
        is_vinchun = self.get_info_from_parser("is_vinchun")
        region = self.get_info_from_parser("region")
        club = self.get_info_from_parser("club")
        trainer = self.get_info_from_parser("trainer")

        row = 0
        index = 0
        label = None
        for data in parser_data['participants']:
            label = Label(master=self, text=data["age_category"])
            label.grid(row=row, column=0, sticky="news", columnspan=13)
            entries.append(label)
            row += 1
            for _ in data["data"]:
                self.create_entry(variable=name[index], row=row, col=0, entry_list=entries)
                self.create_entry(variable=birthday[index], row=row, col=1, entry_list=entries)
                self.create_entry(variable=category[index], row=row, col=2, entry_list=entries)
                self.create_entry(variable=gender[index], row=row, col=3, entry_list=entries)
                self.create_entry(variable=weight[index], row=row, col=4, entry_list=entries)
                self.create_entry(variable=is_sanda[index], row=row, col=5, entry_list=entries, width=1)
                self.create_entry(variable=is_cinda[index], row=row, col=6, entry_list=entries, width=1)
                self.create_entry(variable=is_tuishou[index], row=row, col=7, entry_list=entries, width=1)
                self.create_entry(variable=is_vinchun[index], row=row, col=8, entry_list=entries, width=1)
                self.create_entry(variable=region[index], row=row, col=9, entry_list=entries)
                self.create_entry(variable=club[index], row=row, col=10, entry_list=entries)
                self.create_entry(variable=trainer[index], row=row, col=11, entry_list=entries)

                row += 1
                index += 1

        Button(master=self, text="X", command=lambda: self.save_info(entries, row)).grid(row=row, column=0,
                                                                                          columnspan=12)
        # Label(master=review_win, name=category).pack()
        print(row)

        # review_win.geometry("500x500")

    def get_info_from_parser(self, key: str):
        """
        Локальная функция. Получает информацию из парсера по ключу.

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

    def create_entry(self, variable, entry_list, row, col, width=None) -> None:
        """
        Локальная функция. Создает Entry полее ввода в ТопЛевел окне со списком участников.
    
        :param variable:
        :param entry_list:
        :param row:
        :param col:
        :param width:
        """
        entry = Entry(master=review_win, textvariable=variable, width=width)
        entry.grid(row=row, column=col, sticky="news")
        entry_list.append(entry)

    def save_info(self, entry_list: list, row_count):
        """
        Сохраняет состояние поля и передает информацию конвертеру в ворд
    
        :param row_count: кол-во рядков
        :param entry_list: список Энтри
        :return:
        """
        print(entries)
        result = {line: list() for line in range(row_count)}

        for widget in entry_list:
            if type(widget) == Label:
                print(result[widget.grid_info()["row"]].append(widget.cget("text")))
            else:
                result[widget.grid_info()["row"]].append(widget.get())
                # print(widget.cget("text"))

        # TODO ДОПИСАТЬ ВЫЗОВ ФУНКЦИИ КОНВЕРТАЦИИ
