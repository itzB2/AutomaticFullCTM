
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("522x512")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 512,
    width = 522,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    522.0,
    512.0,
    fill="#131313",
    outline="")

canvas.create_text(
    38.0,
    0.0,
    anchor="nw",
    text="CTM MAKER BOIII",
    fill="#2D2D2D",
    font=("Montserrat Regular", 48 * -1)
)

canvas.create_rectangle(
    27.0,
    77.0,
    219.0,
    269.0,
    fill="#676767",
    outline="")

canvas.create_text(
    81.0,
    140.0,
    anchor="nw",
    text="Clear\nImage",
    fill="#000000",
    font=("Montserrat Regular", 24 * -1)
)

canvas.create_rectangle(
    302.0,
    77.0,
    494.0,
    269.0,
    fill="#676767",
    outline="")

canvas.create_text(
    322.0,
    140.0,
    anchor="nw",
    text="Image with\nno sides",
    fill="#000000",
    font=("Montserrat Regular", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
