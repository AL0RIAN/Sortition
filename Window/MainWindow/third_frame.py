import tkinter as tk
from PIL import Image, ImageTk

class AnimateGifLabel(tk.Label):
    def __init__(self, master, filename, width, height, delay=100):
        self.master = master
        self.filename = filename
        self.delay = delay
        self.check_frames()
        self.i = 0
        self.image = None
        self.width = width
        self.height = height
        super().__init__(master)
        self.load_frames()
        self.show_next_frame()

    def check_frames(self):
        self.frames = Image.open(self.filename).n_frames

    def load_frames(self):
        self.img = Image.open(self.filename)
        self.frame_width, self.frame_height = self.img.size

    def show_next_frame(self):
        if self.i == self.frames:
            self.i = 0
        self.img.seek(self.i)

        # Resize the image to fit the specified width and height
        self.img_resized = self.img.resize((self.width, self.height), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.img_resized)
        self.config(image=self.image)
        self.i += 1
        self.master.after(self.delay, self.show_next_frame)

class ThirdElement(tk.Frame):
    def __init__(self, parent, opponent_first, opponent_second, first_frame_instance):
        super().__init__(parent, bg="#7d7373", width=250, height=180)
        self.grid(row=2, column=0)
        self.opponent_first = opponent_first
        self.opponent_second = opponent_second
        self.first_frame = first_frame_instance
        self.create_widgets()

    def create_widgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Load GIF image
        gif_path = 'Window/MainWindow/third_frame_images/XOsX.gif'

        # Set desired width and height for the GIF image
        width, height = 245, 175

        # Display the GIF image using the AnimateGifLabel
        self.gif_frame = AnimateGifLabel(self, gif_path, width, height)
        self.gif_frame.grid(row=0, column=0, sticky='news')




