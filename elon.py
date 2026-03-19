import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

SIZE = 150
ELON_PATH = "elon.jpg"


def brightness(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]


def create_elon_image(random_path):

    # open images
    random_img = Image.open(random_path).resize((SIZE,SIZE)).convert("RGB")
    elon_img = Image.open(ELON_PATH).resize((SIZE,SIZE)).convert("RGB")

    random_pixels = np.array(random_img).reshape(-1,3)
    elon_pixels = np.array(elon_img).reshape(-1,3)

    # brightness arrays
    random_b = np.array([brightness(p) for p in random_pixels])
    elon_b = np.array([brightness(p) for p in elon_pixels])

    # sorting
    random_order = np.argsort(random_b)
    elon_order = np.argsort(elon_b)

    result = np.zeros_like(random_pixels)

    # rearranging pixels
    for i in range(len(random_pixels)):
        result[elon_order[i]] = random_pixels[random_order[i]]

    result = result.reshape(SIZE,SIZE,3)

    return Image.fromarray(result.astype(np.uint8))


def upload_image():

    path = filedialog.askopenfilename()

    if not path:
        return

    result_img = create_elon_image(path)

    show_result(result_img)


def show_result(img):

    popup = tk.Toplevel(root)
    popup.title("Generated Elon Musk")

    img = img.resize((400,400))
    tk_img = ImageTk.PhotoImage(img)

    label = tk.Label(popup,image=tk_img)
    label.image = tk_img
    label.pack()


# GUI
root = tk.Tk()
root.title("Elon Musk Generator")
root.geometry("300x200")

title = tk.Label(root,text="Create Elon Musk",font=("Arial",12))
title.pack(pady=20)

upload_btn = tk.Button(root,text="Upload Random Image",command=upload_image)
upload_btn.pack(pady=20)

root.mainloop()