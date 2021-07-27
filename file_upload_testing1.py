from tkinter import *
#from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import filedialog
from datetime import datetime

root = Tk()
root.geometry("800x500")
root.title("Upload a file")

column_padd = 20
column_paddy = 10

def open_image():
    global column_padd
    global Label
    global img
    global map
    root.filename = filedialog.askopenfile(initialdir="/", title="ZMap - Select a File", filetypes=(("jpg file", "*.jpg"), ("png files", "*.png")))
    map = root.filename.name
    Label = Label(root, text=map).grid(column=0, row=1)
    canvas = Canvas(root)
    canvas.grid(column=3, row=2, rowspan=100, padx=column_padd, pady=column_paddy)
    img = ImageTk.PhotoImage(Image.open(map))
    canvas.create_image(50, 50, anchor=NW, image=img)


file_path = Label(root, text="Upload a file").grid(column=0, row=0, padx=column_padd, pady=column_paddy)
browse_input = Entry(root, width=50)
browse_input.grid(column=0, row=1, padx=column_padd, pady=column_paddy)

file_open_button = Button(root, text="Browse", command=open_image).grid(column=1, row=1, padx=column_padd, pady=column_paddy)
name_of_map_title = Label(root, text="Name of Map").grid(column=0, row=2, padx=column_padd, pady=column_paddy)
name_of_map_input = Entry(root, width=50).grid(column=0, row=3, padx=column_padd, pady=column_paddy)

'''
'''

country_frame = Frame(root)
country_frame.grid(column=0, row=4, padx=column_padd, pady=column_paddy)
country_frame.columnconfigure(0, weight=1)
country_frame.rowconfigure(0, weight=1)

countryvar = StringVar(root)

country_choices = {'', 'New Zealand', 'Australia', 'Finland', 'Estonia'}
countryvar.set(' ')

country_menu = OptionMenu(country_frame, countryvar, *country_choices)
Label(country_frame, text="What country is your map from?").grid(column=0, row=1)
country_menu.grid(column=1, row=1)
name_of_country = countryvar.get()

date_of_map_title = Label(root, text="Enter date in DD-MM-YYYY format")
date_of_map_title.grid(column=0, row=5, padx=column_padd, pady=column_paddy)
date_of_map = Entry(root, width=50)
date_of_map.grid(column=0, row=6, padx=column_padd, pady=column_paddy)
#  date_of_map_entry = date_of_map.get()
# str(date_of_map_entry)
# date = datetime.strptime(date_of_map_entry, "%d-%m-%y")


# function to get info when 'submit' is pressed
def myClick():
    root.destroy

# submit button
submit = Button(root, text="Submit", command=myClick(), width="30")
submit.grid(column=0, row=7, padx=column_padd, pady=column_paddy)


root.mainloop()