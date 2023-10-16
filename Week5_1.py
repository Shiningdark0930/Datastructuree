from tkinter import *
from tkinter.simpledialog import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("./spite/md202310606")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS userTable(id char(4), userName char(15), email char(15), birthyear int)")

window = Tk()
window.geometry("720x480")
window.title("GUI 데이터 입력")
window.resizable(width = False, height = False)

def inputing():
    indexA = entry1.get()
    indexB = entry2.get()
    indexC = entry3.get()
    indexD = entry4.get()
    try:
        sql = "INSERT INTO userTable VALUES('" + indexA + "','" + indexB + "','" + indexC + "'," + indexD + ")"
        cur.execute(sql)
        messagebox.showinfo("성공", "데이터 입력 성공")
    except:
        messagebox.showwarning("실패", "데이터 입력 오류가 발생함")

def reading():
    index1.delete(0, END)
    index2.delete(0, END)
    index3.delete(0, END)
    index4.delete(0, END)
    index1.insert(0, "사용자ID")
    index2.insert(0, "사용자이름")
    index3.insert(0, "이메일")
    index4.insert(0, "출생연도")
    index1.insert(END, "----------")
    index2.insert(END, "----------")
    index3.insert(END, "----------")
    index4.insert(END, "----------")
    cur.execute("SELECT * FROM userTable")
    i = 0
    while (True) :
        row = cur.fetchone()
        if row == None :
            if i == 0:
                messagebox.showwarning("실패", "데이터가 없습니다!")
            break
        data1 = row[0]
        data2 = row[1]
        data3 = row[2]
        data4 = row[3]
        index1.insert(END, data1)
        index2.insert(END, data2)
        index3.insert(END, data3)
        index4.insert(END, data4)
        i += 1
    

entry1 = Entry(window, width = 16)
entry2 = Entry(window, width = 16)
entry3 = Entry(window, width = 16)
entry4 = Entry(window, width = 16)
entry1.pack()
entry2.pack()
entry3.pack()
entry4.pack()
entry1.place(x = 16, y = 16)
entry2.place(x = 148, y = 16)
entry3.place(x = 280, y = 16)
entry4.place(x = 412, y = 16)

button1 = Button(window, text = "입력", command = inputing)
button2 = Button(window, text = "조회", command = reading)
button1.pack()
button2.pack()
button1.place(x = 546, y = 16)
button2.place(x = 600, y = 16)

index1 = Listbox(window, width=22, height = 35)
index2 = Listbox(window, width=22, height = 35)
index3 = Listbox(window, width=22, height = 35)
index4 = Listbox(window, width=22, height = 35)
index1.pack()
index2.pack()
index3.pack()
index4.pack()
index1.place(x = 0, y = 48)
index2.place(x = 160, y = 48)
index3.place(x = 320, y = 48)
index4.place(x = 480, y = 48)

window.mainloop()