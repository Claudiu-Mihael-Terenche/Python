# Python program to create a file explorer in Tkinter

from tkinter import *
from tkinter import filedialog

def browseFiles(): # function for opening the file explorer window
    filename = filedialog.askopenfilename(initialdir='/',
                                          title='Select a file',
                                          filetypes=(('Text files',
                                                      '*.txt*'),
                                                     ('all files',
                                                      '*.*')))

    label_file_explorer.configure(text="File Opened: " + filename) # change label contents


window = Tk() # create the root window

window.title('File explorer') # set window title

window.geometry('500x500') # set window size

window.config(background='white') # set window background color

label_file_explorer = Label(window,
                            text='File explorer using Tkinter',
                            width=100, height=4,
                            fg='blue') # create a File Explorer label

button_explore = Button(window,
                        text='Browse files',
                        command=browseFiles)

button_exit = Button(window,
                     text='Exit',
                     command=exit)

# grid method is chosen for placing the widgets at respective positions in a table like structure by
# specifying rows and columns

label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

button_exit.grid(column=1, row=3)

window.mainloop() # let the window wait for any events
