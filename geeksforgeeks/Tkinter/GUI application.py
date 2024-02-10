from tkinter import * # import all functions from the tkinter
from tkinter import messagebox # import messagebox class from tkinter

tasks_list = [] # global list is declare for storing all the task

counter = 1 # global variable is declare for counting the task


# Function for checking input error when empty input is given in task field

def inputError():

    if enterTaskField.get() == '': # check for enter task field is empty or not

        messagebox.showerror('Input error') # show the error message
        return 0

    return 1


# Function for clearing the contents of task number text field

def clear_taskNumberField():

    taskNumberField.delete(0.0, END) # clear the content of task number text field


# Function for clearing the contents of task entry field

def clear_taskField():

    enterTaskField.delete(0, END) # clear the content of task field entry box


# Function for inserting the contents from the task entry field to the text area

def insertTask():
    global counter

    value = inputError() # check for error

    if value == 0:  # if error occur then return
        return

    content = enterTaskField.get() + '\n' # get the task string concatenating with new line character

    tasks_list.append(content) # store task in the list

    # insert content of task entry field to the text area and add task one by one in below one by one
    TextArea.insert('end -1 chars', '[ ' + str(counter) + ' ] ' + content)

    counter += 1 # incremented

    clear_taskField() # function calling for deleting the content of task field

def delete(): # function for deleting the specified task
    global counter

    if len(tasks_list) == 0: # handling the empty task error
        messagebox.showerror('No task')
        return

    number = taskNumberField.get(1.0, END) # get the task number, which is required to delete

    if number == '\n': # checking for input error when empty input in task number field
        messagebox.showerror('Input error')
        return

    else:
        task_no = int(number)

    clear_taskNumberField() # function calling for deleting the content of task number field

    tasks_list.pop(task_no - 1) # deleted specified task from the list

    counter -= 1 # decremented

    TextArea.delete(1.0, END) # whole content of text area widget is deleted

    for i in range(len(tasks_list)): # rewriting the task after deleting one task at a time
        TextArea.insert('end -1 chars', '[ ' + str(i + 1) + ' ] ' + tasks_list[i])


if __name__ == '__main__':
    gui = Tk() # create a GUI window

    gui.configure(background='light green') # set the background colour of GUI window

    gui.title('ToDo App') # set the title of GUI window

    gui.geometry('250x300') # set the configuration of GUI window

    enterTask = Label(gui, text='Enter your task', bg='light green') # create a label : Enter your task

    enterTaskField = Entry(gui) # create a text entry box for typing the task

    # create a submit button and place into the root window when user press the button, the command or
    # function affiliated to that button is executed
    Submit = Button(gui, text='Submit', fg='Black', bg='Red', command=insertTask)

    # create a text area for the root with lunida 13 font text area is for writing the content
    TextArea = Text(gui, height=5, width=25, font='lucida 13')

    taskNumber = Label(gui, text='Delete task number', bg='blue') # create a label : Delete task number

    taskNumberField = Text(gui, height=1, width=2, font='lucida 13')

    # create a delete button and place into the root window
    # when user press the button, the command or function affiliated to that button is executed
    delete = Button(gui, text="Delete", fg='Black', bg='Red', command=delete)

    # create a exit button and place into the root window
    # when user press the button, the command or function affiliated to that button is executed
    Exit = Button(gui, text="Exit", fg='Black', bg='Red', command=exit)

    # grid method is used for placing the widgets at respective positions in table like structure
    enterTask.grid(row=0, column=2)

    enterTaskField.grid(row=1, column=2, ipadx=50) # ipadx attributed set the entry box horizontal size

    Submit.grid(row=2, column=2)

    # padx attributed provide x-axis margin from the root window to the widget
    TextArea.grid(row=3, column=2, padx=10, sticky=W)

    taskNumber.grid(row=4, column=2, pady=5)

    taskNumberField.grid(row=5, column=2)

    delete.grid(row=6, column=2, pady=5) # pady attributed provide y-axis margin from the widget

    Exit.grid(row=7, column=2)

    gui.mainloop() # start the GUI
