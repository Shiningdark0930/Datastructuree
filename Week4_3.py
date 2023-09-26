from tkinter import *
from tkinter.simpledialog import *

window = Tk()
window.geometry("1280x720")

def deletee():
    index1.insert(0, label2.get())
    label2.delete(0, END)

def deleteee():
    selection = index1.curselection()
    if(len(selection)) == 0:
        return
    index1.delete(selection[0])

label1 = Label(window, text = "Add a Task")
label2 = Entry(window, width = 128)
label1.pack()
label2.pack()

button1 = Button(window, text = "Add Task", command = deletee)
button1.pack()

index1 = Listbox(window, width=128, height = 35)
index1.pack()

button2 = Button(window, text = "Delete Task", command = deleteee)
button2.pack()

window.mainloop()