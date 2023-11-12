import tkinter as tk
from import_window import *
from main_window import starting

'''
First window in program.
'''


class StartWindow:
    def __init__(self):
        self.start = tk.Tk()
        self.start.title('Жеребкування')
        self.start.geometry('400x300')
        self.start.resizable(False, False)
        self.start.config(bg='#DCF4FF')

        self.start.grid_rowconfigure(0, minsize=150)
        self.start.grid_rowconfigure(1, minsize=150)
        self.start.grid_columnconfigure(0, minsize=400)

        self.create_widgets()
        self.run()

    def create_widgets(self):
        continue_btn = tk.Button(self.start, text='Продовжити', bg='#DCF4FF')
        start_btn = tk.Button(self.start, text='Новий турнір', bg='#DCF4FF', command=self.new_tournament)

        continue_btn.grid(row=0, column=0, sticky='wens')
        start_btn.grid(row=1, column=0, sticky='wens')

    def run(self):
        self.start.mainloop()

    def new_tournament(self):
        importing = ImportWindow()
        self.start.withdraw()  # Спрятать главное окно StartWindow, но не закрывать его
        importing.run()
        self.start.destroy()