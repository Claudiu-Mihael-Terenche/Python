from tkinter import *
import calendar


# function for showing the calendar of the given year

def show_cal():
    new_gui = Tk()  # create a GUI window

    new_gui.config(background='white')  # set the background color of a GUI window

    new_gui.title('Calendar')  # set the name of tkinter GUI window

    new_gui.geometry('550x600')  # set the configuration of GUI window

    fetch_year = int(year_field.get())  # get method returns current text as string

    # calendar method of calendar module returns the calendar of the given year
    cal_content = calendar.calendar(fetch_year)

    # create a label for showing the content of the calendar
    cal_year = Label(new_gui, text=cal_content, font='Consolas 10 bold')

    # grid method is used for placing the widgets at respective positions in table like structure
    cal_year.grid(row=5, column=1, padx=20)

    new_gui.mainloop()  # start the GUI


if __name__ == '__main__':
    gui = Tk()  # create a GUI window

    gui.config(background='white')  # set the background color of a GUI window

    gui.title('Calendar')  # set the name of tkinter GUI window

    gui.geometry('250x140')  # set the configuration of GUI window

    # create a calendar: label with specified font and size
    cal = Label(gui, text='Calendar', bg='dark gray', font=('times', 28, 'bold'))

    year = Label(gui, text='Enter year', bg='light green')  # create an entered year: label

    year_field = Entry(gui)  # create a text entry box for filling or typing the information

    # create a Show Calendar Button and attached to showCal function
    Show = Button(gui, text='Show calendar', fg='Black', bg='Red', command=show_cal)

    # create an exit button and attached to exit function
    Exit = Button(gui, text='Exit', fg='Black', bg='Red', command=exit)

    # grid method is used for placing the widgets at respective positions in table like structure
    cal.grid(row=1, column=1)

    year.grid(row=2, column=1)

    year_field.grid(row=3, column=1)

    Show.grid(row=4, column=1)

    Exit.grid(row=6, column=1)

    gui.mainloop()  # start the GUI
