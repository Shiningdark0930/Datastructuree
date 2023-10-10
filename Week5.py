import sqlite3
con = sqlite3.connect("./spite/naverDB")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS userTable(id char(4), userName char(15), email char(15), birthyear int)")

while (True) :
    data1 = input("사용자ID ==> ")
    if data1 == "" :
        break
    data2 = input("사용자이름 ==> ")
    data3 = input("이메일 ==> ")
    data4 = input("출생연도 ==> ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(sql)
con.commit()
con.close()


data1, data2, data3, data4 = "", "", "", ""
row = None
con = sqlite3.connect("naverDB")
cur = con.cursor()
cur.execute("SELECT * FROM userTable")

print("사용자ID    사용자이름    이메일            출생연도")
print("--------------------------------------------------------")


while (True) :
    row = cur.fetchone()
    if row == None :
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s   %15s   %15s   %5d" % (data1, data2, data3, data4))


