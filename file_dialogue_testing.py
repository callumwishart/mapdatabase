from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()

root.filename = filedialog.askopenfile(initialdir="/", title="ZMap - Select a File", filetypes=(("jpg file", "*.jpg"), ("png files", "*.png")))
Label = Label(root, text=root.filename).pack()

myImage = ImageTk.PhotoImage(Image.open(root.filename))
myImage_label = Label(image=myImage).pack()

root.mainloop()