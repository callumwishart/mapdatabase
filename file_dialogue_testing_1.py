from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()


def open_image():
    global Label
    global img
    global map
    root.filename = filedialog.askopenfile(initialdir="/", title="ZMap - Select a File", filetypes=(("jpg file", "*.jpg"), ("png files", "*.png")))
    map = root.filename.name
    Label = Label(root, text=map).pack()
    canvas = Canvas(root)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(map))
    canvas.create_image(0, 0, anchor=NW, image=img)


browse_input = Entry(root, width=50)
browse_input.insert(0, "File Name")
browse_input.grid(column=0, row=0)

file_open_button = Button(root, text="Browse", command=open_image).grid(column=1, row=0)


root.mainloop()