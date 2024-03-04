import tkinter as tk
from tkinter import ttk
from Window.import_window import *

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

        self.start.protocol("WM_DELETE_WINDOW", self.on_closing)

    # def create_widgets(self):
    #     continue_btn = tk.Button(self.start, text='Продовжити', bg='#DCF4FF')
    #     start_btn = tk.Button(self.start, text='Новий турнір', bg='#DCF4FF', command=self.new_tournament)
    #
    #     continue_btn.grid(row=0, column=0, sticky='wens')
    #     start_btn.grid(row=1, column=0, sticky='wens')

    def create_widgets(self):
        button_font = ('Times New Roman', 16)
        button_width = 20
        button_height = 2

        continue_btn = tk.Button(self.start, text='Продовжити', bg='#D4FFC7', font=button_font, width=button_width,
                                 height=button_height, state=tk.DISABLED)
        start_btn = tk.Button(self.start, text='Новий турнір', bg='#FFC7C7', command=self.new_tournament,
                              font=button_font, width=button_width, height=button_height)

        continue_btn.grid(row=0, column=0, sticky='wens', padx=10, pady=10)
        start_btn.grid(row=1, column=0, sticky='wens', padx=10, pady=10)

    def run(self):
        self.start.mainloop()

    def on_closing(self):
        self.start.destroy()
        sys.exit(0)

    def new_tournament(self):
        importing = ImportWindow()
        self.start.withdraw()  # Спрятать главное окно StartWindow, но не закрывать его
        importing.run()
        self.start.destroy()