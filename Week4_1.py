from tkinter import *

# setting window
window = Tk()
window.title("practice window tab")
window.geometry("1280x720")
window.resizable(width = False, height = False)


# functions
def changeImages():
    global photo2
    if chk.get() == 1:
        photo2 = '.\jpegfiles\cat.gif'
    elif chk.get() == 2:
        photo2 = '.\jpegfiles\dog.gif'
    else:
        photo2 = '.\jpegfiles/rabbit.gif'

def ang():
    photo1.configure(file = photo2)

# labels
label1 = Label(window, text = "당신이 좋--아하는 동물 투표 ", font = ("궁서체", 30), fg = 'blue', bg = 'yellow')
label1.pack()

photo1 = PhotoImage(file = '.\jpegfiles\cat.gif')
photo2 = '.\jpegfiles\cat.gif'
chk = IntVar()
rb1 = Radiobutton(window, text = "야옹이", variable = chk, value = 1, command = changeImages)
rb2 = Radiobutton(window, text = "멍뭉이", variable = chk, value = 2, command = changeImages)
rb3 = Radiobutton(window, text = "Rabbit", variable = chk, value = 3, command = changeImages)

images1 = Label(window, image = photo1)
rb1.pack();rb2.pack();rb3.pack();images1.pack()

button1 = Button(window, text = "파이썬 종료", fg = 'red', command = quit)
button2 = Button(window, text = "동--물 봐버리기", fg = 'red', command = ang)
button1.pack()
button2.pack()


# mainloop
window.mainloop()