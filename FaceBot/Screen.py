import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

# Create the main window
window = tk.Tk()
window.geometry("1000x500")

arrays = []
photo_images = []
labels = []
n = ['Josh' , 'Oliver']
labs = []
for i in range(2):
    array = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
    arrays.append(array)

def placePics(arrays):
    for array in arrays:
        image = Image.fromarray(array)
        photo = ImageTk.PhotoImage(image)
        photo_images.append(photo)
        label = tk.Label(window, image=photo)
        labels.append(label)
    Lx = 800
    Ly = 25
    for l in labels:
        l.place(x = Lx, y = Ly)
        Lx += 0
        Ly += 150

def LabelTheLabels(names):
    for name in names:
        label = tk.Label(window, text = name)
        labs.append(label)
    Lx = 750
    Ly = 75
    for l in labs:
        l.place(x = Lx, y = Ly)
        Lx += 0
        Ly += 150

placePics(arrays)
LabelTheLabels(n)
window.mainloop()