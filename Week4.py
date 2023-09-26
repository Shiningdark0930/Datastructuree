
from tkinter import *
window = Tk()


# setting window
window.title("practice window tab")
window.geometry("1280x720")
window.resizable(width = False, height = False)


# labels
label1 = Label(window, text = "I learn Python", bg = 'green')
label2 = Label(window, text = "Hardly", font = ("궁서체", 30), fg = 'blue', bg = 'yellow')
label3 = Label(window, text = "wow", bg = 'magenta', width = 20, height = 5, anchor = SE)
label1.pack()
label2.pack()
label3.pack()

photo1 = PhotoImage(file = '.\jpegfiles\cat.gif')
photo2 = PhotoImage(file = '.\jpegfiles\dog.gif')
images1 = Label(window, image = photo1)
images2 = Label(window, image = photo2)
images1.pack(side = LEFT)
images2.pack(side = LEFT)

button1 = Button(window, text = "파이썬 종료", fg = 'red', command = quit)
button1.pack()


# mainloop
window.mainloop()