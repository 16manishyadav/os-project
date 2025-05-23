
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets//frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("937x693")
window.configure(bg = "#010101")


canvas = Canvas(
    window,
    bg = "#010101",
    height = 693,
    width = 937,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    338.0,
    16.0,
    anchor="nw",
    text="Benchmark",
    fill="#DFBAC7",
    font=("MontserratRoman Bold", 24 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    468.0,
    368.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
