# external libraries
import sqlite3
from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import *
import winsound
from PIL import ImageTk, Image

# advanced technique - GUI's
# creates main window
master = Tk()
master.geometry("250x200")
master.title("Z-Map")
master.iconbitmap('C:/Users/cgawi/Downloads/map_icon1.ico')

# variables for page setup
column_pad = 20
row_pad = 10

# advanced technique - database usage
connection = sqlite3.connect('map_database.db')

c = connection.cursor()
# original code for creating table
# saved so I know the values for each column
'''
c.execute("""CREATE TABLE map_info(
    map_location_name text,
    map_competition_name,
    map_location text,
    map_path text,
    map_date integer,
    map_type text,
    map_region text)""")
'''
# code for upload a map page


# advanced technique - functions
def upload_file():
    # opens a new window
    root = Toplevel(master)
    root.title("Z-Map Upload a file")
    root.iconbitmap('C:/Users/cgawi/Downloads/map_icon1.ico')
    root.focus_set()

    # input fields
    # input for name of location of map
    m_location_name = Entry(root, width=50)
    m_location_name.grid(row=0, column=1, padx=column_pad, pady=row_pad)

    # input for name of competition of map
    m_competition_name = Entry(root, width=50)
    m_competition_name.grid(row=1, column=1, padx=column_pad, pady=row_pad)

    # drop-down for country of map
    country_frame = Frame(root)
    country_frame.grid(column=1, row=2, padx=column_pad, pady=row_pad)
    country_frame.columnconfigure(0, weight=1)
    country_frame.rowconfigure(0, weight=1)
    country_var = StringVar(root)
    country_var.set(' ')
    country_menu = OptionMenu(country_frame, country_var, ' ', 'New Zealand', 'Australia', 'Finland', 'Estonia')
    Label(country_frame, text="What country is your map from?  ").grid(column=0, row=1)
    country_menu.grid(column=1, row=1)

    # drop-down for region of map
    region_frame = Frame(root)
    region_frame.grid(column=1, row=3, padx=column_pad, pady=row_pad)
    region_frame.columnconfigure(0, weight=1)
    region_frame.rowconfigure(0, weight=1)
    region_var = StringVar(root)
    region_var.set(' ')
    region_menu = OptionMenu(region_frame, region_var, '', 'Northland', 'Auckland', 'Waikato', 'Napier', 'Palmerston North', 'Wellington', 'Nelson', 'Christchurch', 'Otago', 'Other', 'Not NZ')
    Label(region_frame, text="What region is your map from?  ").grid(column=0, row=1)
    region_menu.grid(column=1, row=1)

    # drop-down for type of map
    type_frame = Frame(root)
    type_frame.grid(column=1, row=4, padx=column_pad, pady=row_pad)
    type_frame.columnconfigure(0, weight=1)
    type_frame.rowconfigure(0, weight=1)
    type_var = StringVar(root)
    type_var.set(' ')
    type_menu = OptionMenu(type_frame, type_var, '', 'Forest', 'Farm', 'Sprint')
    Label(type_frame, text="What type of map is this?  ").grid(column=0, row=1)
    type_menu.grid(column=1, row=1)

    # input for date of map
    m_date = Entry(root, width=50)
    m_date.grid(column=1, row=5, padx=column_pad, pady=row_pad)

    # upload a file button
    def open_image():
        global map_1
        root.filename = filedialog.askopenfile(initialdir="/", title="Z-Map - Select a File", filetypes=(("jpg file", "*.jpg"), ("png files", "*.png")))
        map_1 = root.filename.name
        map_short = map_1
        '''
        for i in range(0, len(map_short)-25):
            map = map
            # get miss to help remove characters to shorten string so path can be viewed easily
        '''
        m_path_label = Label(root, text=map_1)
        m_path_label.grid(column=0, row=7, padx=column_pad, pady=row_pad, columnspan=2)

    # opens a file dialogue box
    file_open_button = Button(root, width=60, text="Browse", command=open_image)
    file_open_button.grid(column=0, row=6, padx=column_pad, pady=row_pad, columnspan=2)

    # end of input fields
    # label for text inputs
    # text for map location
    m_location_label = Label(root, text="What is the name of your map?")
    m_location_label.grid(row=0, column=0, padx=column_pad, pady=row_pad)

    # text for competition name
    m_competition_label = Label(root, text="What series / competition was this from?")
    m_competition_label.grid(row=1, column=0, padx=column_pad, pady=row_pad)

    # text for date of map
    m_date_label = Label(root, text="What date is your map from? (YYYYMMDD)")
    m_date_label.grid(row=5, column=0, padx=column_pad, pady=row_pad)

    # submit button
    def submit():

        # advanced technique - error handling
        # validates the date
        date_valid = m_date.get()
        try:
            int(date_valid)
            it_is = True
        except ValueError:
            it_is = False
        if it_is is False:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            return

        # creates a connection with my database
        connection = sqlite3.connect('map_database.db')
        c = connection.cursor()
        # chooses what data goes into what column
        c.execute("""INSERT INTO map_info VALUES(
            :map_location_name,
            :map_competition_name,
            :map_location,
            :map_path,
            :map_date,
            :map_type,
            :map_region)""",
                  {
                      'map_location_name': m_location_name.get(),
                      'map_competition_name': m_competition_name.get(),
                      'map_location': country_var.get(),
                      'map_path': map_1,
                      'map_date': m_date.get(),
                      'map_type': type_var.get(),
                      'map_region': region_var.get()
                  })
        # does the instructions
        connection.commit()
        # closes the connection
        connection.close()
        # destroys the upload window
        root.destroy()
    # code for submit button
    submit = Button(root, width=90, text="Submit", command=submit)
    submit.grid(row=8, column=0, padx=column_pad, pady=row_pad, columnspan=2)


# Create a query function
def help():
    help_window = Toplevel(master)
    help_window.title("Z-Map Help")
    help_window.iconbitmap('C:/Users/cgawi/Downloads/map_icon1.ico')
    help_window.geometry("400x400")
    help_window.focus_set()

    instructions = Label(help_window, text="Instructions\n\n", font=("Arial", 15))
    instructions.grid(row=0, column=0)
    step1 = Label(help_window, text="""If you want to upload a file click on the 'upload a file window
     and fill in relevant info then press submit.\n\n""")
    step1.grid(row=1, column=0)
    step2 = Label(help_window, text="""If you want to view maps you open 'view maps' tab then press
    display window to view information. You can then sort the data by type of date.""")
    step2.grid(row=2, column=0)


# creates window for viewing all of my data
def view_files():
    view_window = Toplevel(master)
    view_window.title("Z-Map Map Viewer")
    view_window.iconbitmap('C:/Users/cgawi/Downloads/map_icon1.ico')
    view_window.focus_set()

    # function to connect to database
    def connect():
        connection = sqlite3.connect("map_database.db")
        c = connection.cursor()

        connection.commit()
        connection.close()

    # views data by date
    def view_date():
        connection = sqlite3.connect("map_database.db")
        c = connection.cursor()

        c.execute("SELECT * FROM map_info ORDER BY map_date DESC")
        rows = c.fetchall()

        for row in table.get_children():
            table.delete(row)
        for row in rows:
            table.insert("", tk.END, values=row)

        connection.close()

    # views data by type of map
    def view_type():
        connection = sqlite3.connect("map_database.db")
        c = connection.cursor()

        c.execute("SELECT * FROM map_info ORDER BY map_type")
        rows = c.fetchall()
        for row in table.get_children():
            table.delete(row)
        for row in rows:
            table.insert("", tk.END, values=row)

        connection.close()

    # connect to the database
    connect()

    # button to display data
    display_data = Button(view_window, text="Display data", command=view_date)
    display_data.grid(row=0, column=1, pady=10)

    # buttons for sorting data
    sort_date = Button(view_window, text="Sort by date", command=view_date)
    sort_date.grid(row=0, column=0, pady=10)

    sort_name = Button(view_window, text="Sort by type", command=view_type)
    sort_name.grid(row=0, column=2, pady=10)
    # creates table
    table = ttk.Treeview(view_window, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings')
    # puts data into table
    table.column("#1", anchor=tk.CENTER)
    table.heading("#1", text="Location of Map")

    table.column("#2", anchor=tk.CENTER)
    table.heading("#2", text="Name of competition")

    table.column("#3", anchor=tk.CENTER)
    table.heading("#3", text="Country")

    table.column("#4", anchor=tk.CENTER)
    table.heading("#4", text="Image path")

    table.column("#5", anchor=tk.CENTER)
    table.heading("#5", text="Date")

    table.column("#6", anchor=tk.CENTER)
    table.heading("#6", text="Type of Map")

    table.column("#7", anchor=tk.CENTER)
    table.heading("#7", text="Region")

    table.column("#8", anchor=tk.CENTER, width=15)
    table.heading("#8", text="")

    table.grid(row=1, column=0, columnspan=3, padx=5, pady=5)


# code for main window
title_label = Label(master, text="Z-Map", font=("Arial", 25))
title_label.grid(column=0, row=0, padx=column_pad, pady=row_pad)

# Create a Query Button
query = Button(master, width=30, text="Help", command=help)
query.grid(column=0, row=3, padx=column_pad, pady=row_pad)

# Create an upload button
upload = Button(master, width=30, text="Upload a file", command=upload_file)
upload.grid(column=0, row=1, padx=column_pad, pady=row_pad)

# Create a 'view table' button
view = Button(master, width=30, text="View maps", command=view_files)
view.grid(column=0, row=2, padx=column_pad, pady=row_pad)

# finishes connection
connection.commit()
connection.close()

# runs the code
master.mainloop()
