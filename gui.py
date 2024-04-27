import tkinter as tk
from pathlib import Path

# Assuming your script is located in the src directory
SCRIPT_PATH = Path(__file__).resolve().parent
ASSETS_PATH = SCRIPT_PATH.parent / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = tk.Tk()
window.geometry("500x500")
window.configure(bg="#FFFFFF")

canvas = tk.Canvas(
    window,
    bg="#FFFFFF",
    height=500,
    width=500,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(250.0, 250.0, image=image_image_1)

# Repeat the same process for other image files...

canvas.create_text(193.0, 232.0, anchor="nw", text="25:00", fill="#FFFFFF", font=("Inter BlackItalic", 24 * -1))
window.resizable(False, False)
window.mainloop()
