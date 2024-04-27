import tkinter as tk
from pathlib import Path

# Assuming your script is located in the src directory
SCRIPT_PATH = Path(__file__).resolve().parent
ASSETS_PATH = SCRIPT_PATH.parent / "assets"

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

image_image_2 = tk.PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(408.2524070739746, 464.9999958243375, image=image_image_2)

image_image_3 = tk.PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(250.0, 36.0, image=image_image_3)

image_image_4 = tk.PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(196.0, 388.0408630371094, image=image_image_4)

image_image_5 = tk.PhotoImage(file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(303.9545593261719, 389.0, image=image_image_5)

entry_image_1 = tk.PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(249.69048309326172, 346.0, image=entry_image_1)
entry_1 = tk.Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=208.0, y=335.0, width=83.38096618652344, height=20.0)

image_image_6 = tk.PhotoImage(file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(113.0, 484.0, image=image_image_6)

image_image_7 = tk.PhotoImage(file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(250.0, 255.0, image=image_image_7)

image_image_8 = tk.PhotoImage(file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(106.0, 32.0, image=image_image_8)

image_image_9 = tk.PhotoImage(file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(467.5048179626465, 464.9999958243375, image=image_image_9)

image_image_10 = tk.PhotoImage(file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(348.99999618530273, 464.9999958243375, image=image_image_10)

canvas.create_text(193.0, 232.0, anchor="nw", text="25:00", fill="#FFFFFF", font=("Inter BlackItalic", 24 * -1))
window.resizable(False, False)
window.mainloop()
