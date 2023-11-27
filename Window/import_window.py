from IO.parser import *
import tkinter as tk
import sys
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from Window.MainWindow.main_window import MainWindow
from Window.MainWindow.tracking import ADDRESS_LINK
from sorting.tournaments_list import PAIR_LIST
import shared
from sorting.tournaments_list import make_pair_list
from sorting.tournaments_list import pair_list_cleaner

'''
Window in which we will download file to our program.
'''

class ImportWindow:
    def __init__(self):
        self.import_frame = tk.Tk()
        self.import_frame.title('Жеребкування')
        self.import_frame.geometry('800x540')
        self.import_frame.resizable(False, False)
        self.import_frame.config(bg='#F6FFFE')

        self.import_frame.grid_rowconfigure(0, minsize=150)
        self.import_frame.grid_columnconfigure(0, minsize=250)

        self.create_widgets()

        self.import_frame.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        button_font = ('Times New Roman', 16)
        decoration = tk.Label(self.import_frame, text='武术', font=('Times New Roman', 260), fg='#9BB6FF', bg='#F6FFFE')
        choose_btn = tk.Button(self.import_frame, text='Вибрати файл', bg='#F6FFFE', fg='#000000', width=11, height=3,
                               command=self.open_file, relief=tk.FLAT, font=button_font)

        decoration.place(relx=0.5, rely=0.5, anchor="center")
        choose_btn.place(relx=0.5, rely=0.5, anchor="center")

    def run(self):
        self.import_frame.mainloop()

    def on_closing(self):
        self.import_frame.destroy()
        sys.exit(0)

    def open_file(self):
        # global ADDRESS_LINK
        shared.write_variable(fd.askopenfilename())
        # print(ADDRESS_LINK)
        # sth_list = make_pair_list()
        # PAIR_LIST = pair_list_cleaner(sth_list)
        self.import_frame.withdraw()  # Спрятать главное окно StartWindow, но не закрывать его
        test = MainWindow()
        test.run()
        self.import_frame.destroy()