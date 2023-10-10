import sqlite3
con = sqlite3.connect("./spite/naverDB")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS productTable(id char(4), userName char(15), email char(15), birthyear int)")

while (True) :
    data1 = input("제품코드 ==> ")
    if data1 == "" :
        break
    data2 = input("제품명 ==> ")
    data3 = input("가격 ==> ")
    data4 = input("재고수량 ==> ")
    sql = "INSERT INTO productTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(sql)
con.commit()

data1, data2, data3, data4 = "", "", "", ""
row = None
con = sqlite3.connect("./spite/naverDB")
cur = con.cursor()
cur.execute("SELECT * FROM productTable")

print("제품코드    제품명    가격        재고수량")
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

con.close()
