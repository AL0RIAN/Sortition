import tkinter as tk
from tkcalendar import Calendar
from tkinter import filedialog
from IO.export.export_docx import ExportPairsDOCX
from sorting.tournaments_list import PAIR_LIST

class StartEndFrame:
    def __init__(self):
        self.start = tk.Tk()
        self.start.title('Жеребкування')
        self.start.geometry('540x300')
        self.start.resizable(False, False)
        self.start.config(bg='#DCF4FF')

        self.create_widgets()

    def create_widgets(self):
        start_label = tk.Label(self.start, text="Початок соревнований:", bg='#DCF4FF')
        start_label.grid(row=0, column=0, padx=10, pady=10)

        self.start_cal = Calendar(self.start, selectmode="day", year=2023, month=1, day=1)
        self.start_cal.grid(row=1, column=0, padx=10, pady=10)

        end_label = tk.Label(self.start, text="Кінець соревнований:", bg='#DCF4FF')
        end_label.grid(row=0, column=1, padx=10, pady=10)

        self.end_cal = Calendar(self.start, selectmode="day", year=2023, month=1, day=1)
        self.end_cal.grid(row=1, column=1, padx=10, pady=10)

        submit_button = tk.Button(self.start, text="Підтвердити", command=self.get_dates)
        submit_button.grid(row=2, columnspan=2, pady=20)

    def get_dates(self):
        start_value = self.start_cal.get_date()
        end_value = self.end_cal.get_date()
        folder_path = filedialog.askdirectory()
        ExportPairsDOCX(r"start_value", r"end_value", PAIR_LIST).export(folder_path)
        self.start.destroy()

    def start_end_s(self):
        self.start.mainloop()
