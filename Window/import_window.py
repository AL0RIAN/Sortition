import tkinter as tk
import sys
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from Window.MainWindow.main_window import MainWindow
from Window.start_end_date import StartEndFrame
from IO.export.export_docx import ExportPairsDOCX
import shared
'''
Window in which we will download file to our program.
'''

# class ImportWindow:
#     def __init__(self):
#         self.import_frame = tk.Tk()
#         self.import_frame.title('Жеребкування')
#         self.import_frame.geometry('800x540')
#         self.import_frame.resizable(False, False)
#         self.import_frame.config(bg='#F6FFFE')
#
#         self.import_frame.grid_rowconfigure(0, minsize=150)
#         self.import_frame.grid_columnconfigure(0, minsize=250)
#
#         self.create_widgets()
#
#         self.import_frame.protocol("WM_DELETE_WINDOW", self.on_closing)
#
#     def create_widgets(self):
#         button_font = ('Times New Roman', 16)
#         decoration = tk.Label(self.import_frame, text='武术', font=('Times New Roman', 260), fg='#9BB6FF', bg='#F6FFFE')
#         choose_btn = tk.Button(self.import_frame, text='Вибрати файл', bg='#F6FFFE', fg='#000000', width=11, height=3,
#                                command=self.open_file, relief=tk.FLAT, font=button_font)
#
#         decoration.place(relx=0.5, rely=0.5, anchor="center")
#         choose_btn.place(relx=0.5, rely=0.5, anchor="center")
#
#     def run(self):
#         self.import_frame.mainloop()
#
#     def on_closing(self):
#         self.import_frame.destroy()
#         sys.exit(0)
#
#     def open_file(self):
#         # global ADDRESS_LINK
#         shared.write_variable(fd.askopenfilename())
#         # print(ADDRESS_LINK)
#         # sth_list = make_pair_list()
#         # PAIR_LIST = pair_list_cleaner(sth_list)
#         self.import_frame.withdraw()  # Спрятать главное окно StartWindow, но не закрывать его
#         test = MainWindow()
#         test.run()
#         self.import_frame.destroy()

class ImportWindow:
    def __init__(self):
        self.import_frame = tk.Toplevel()
        self.import_frame.title('Жеребкування')
        self.import_frame.geometry('800x540')
        self.import_frame.resizable(False, False)
        # self.import_frame.config(bg='#F6FFFE')
        self.import_frame.config(bg='#FFFFFF')

        self.import_frame.grid_rowconfigure(0, minsize=150)
        self.import_frame.grid_columnconfigure(0, minsize=250)

        self.create_widgets()

        self.import_frame.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.label = None

    def create_widgets(self):
        # Define button colors and padding
        button_fg_color = '#000000'
        button_padx = 10
        button_pady = 5
        button_font = ('Times New Roman', 16)

        choose_btn = tk.Button(self.import_frame, text='Вибрати файл', bg='#D4FFC7', fg=button_fg_color,
                               width=14, height=3, command=self.open_file, relief=tk.FLAT, font=button_font,
                               padx=button_padx, pady=button_pady)
        export_btn = tk.Button(self.import_frame, text='Експорт', bg='#FFC7C7', fg=button_fg_color,
                               width=14, height=3, command=self.export_file, relief=tk.FLAT, font=button_font,
                               padx=button_padx, pady=button_pady)
        start_btn = tk.Button(self.import_frame, text='Початок', bg='#DCF4FF', fg=button_fg_color,
                               width=14, height=3, command=self.start_sortition, relief=tk.FLAT, font=button_font,
                               padx=button_padx, pady=button_pady)

        # Apply styles for buttons
        # choose_btn.config(border=0, highlightthickness=0)  # Remove border and highlight
        # export_btn.config(border=0, highlightthickness=0)

        image_path = r"Window\MainWindow\third_frame_images\silhouette-kung-fu-wushu-shaolin.png"
        original_image = Image.open(image_path)
        resized_image = original_image.resize((400, 260))
        photo = ImageTk.PhotoImage(resized_image)

        self.label = tk.Label(self.import_frame, image=photo, bg='#FFFFFF', borderwidth=0, highlightthickness=0)
        self.label.image = photo
        self.label.place(relx=0.7, rely=0.5, anchor="center")

        choose_btn.place(relx=0.3, rely=0.3, anchor="center")
        start_btn.place(relx=0.3, rely=0.5, anchor="center")
        export_btn.place(relx=0.3, rely=0.7, anchor="center")

    def run(self):
        self.import_frame.mainloop()

    def on_closing(self):
        self.import_frame.destroy()
        sys.exit(0)

    def open_file(self):
        shared.write_variable(fd.askopenfilename())

    def start_sortition(self):
        self.import_frame.withdraw()
        test = MainWindow()
        test.run()
        self.import_frame.destroy()

    def export_file(self):
        start_end = StartEndFrame()
        start_end.start_end_s()