from tkinter import *

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(f"Width: {screen_width}\nHeight: {screen_height}")
root.title("Жеребьевка")
root.geometry(f"{screen_width // 2}x{screen_height // 2}")
root.resizable(width=False, height=False)
