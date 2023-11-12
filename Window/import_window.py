from IO.parser import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from MainWindow.main_window import MainWindow

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

    def create_widgets(self):
        button_font = ('Times New Roman', 16)
        decoration = tk.Label(self.import_frame, text='武术', font=('Times New Roman', 260), fg='#9BB6FF', bg='#F6FFFE')
        choose_btn = tk.Button(self.import_frame, text='Вибрати файл', bg='#FFFFFF', fg='#000000', width=20, height=3,
                               command=self.open_file, relief=tk.FLAT, font=button_font)

        decoration.place(relx=0.5, rely=0.5, anchor="center")
        choose_btn.place(relx=0.5, rely=0.5, anchor="center")

    def run(self):
        self.import_frame.mainloop()

    def open_file(self):
        file_name = fd.askopenfilename()
        print(file_name)
        self.import_frame.withdraw()  # Спрятать главное окно StartWindow, но не закрывать его
        test = MainWindow()
        test.run()
        self.import_frame.destroy()