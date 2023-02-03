import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(f"Width: {screen_height}\nHeight: {screen_width}")

root.title("Жеребьевка")
root.geometry(f"{screen_width // 2}x{screen_height // 2}")

root.mainloop()
