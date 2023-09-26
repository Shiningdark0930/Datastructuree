from tkinter import *

# setting window
window = Tk()
window.title("practice window tab")
window.geometry("1280x720")
window.resizable(width = False, height = False)

i = 0
# functions
def numPlus():
    global i
    global label1
    if i > 7:
        i = -1
    i += 1
    label1.configure(text = textt[i])

def numMinus():
    global i
    global label1
    if i < 1:
        i = 9
    i -= 1
    label1.configure(text = textt[i])

textt = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]

# labels
label1 = Label(window, text = textt[i], font = ("궁서체", 30), fg = 'blue', bg = 'yellow')
label1.pack()

button1 = Button(window, text = "이--전", fg = 'red', command = numMinus)
button2 = Button(window, text = "다--음", fg = 'red', command = numPlus)
button1.pack(side = LEFT)
button2.pack(side = RIGHT)


# mainloop
window.mainloop()