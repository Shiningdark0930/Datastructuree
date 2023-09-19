class Item:
    count = 0
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def getprice(self):
        pass

class Book(Item):
    def __init__(self, title, price, page, auther):
        self.title = title
        self.price = price
        self.page = page
        self.auther = auther

    def __str__(self):
        return f"제목:{self.title}, 가격:{self.price}, 페이지:{self.page}, 저자:{self.auther}"

    def getprice(self):
        print(self.title,"의 가격은", self.price,"원 입니다.")

class Magazine(Item):
    def __init__(self, title, price, date):
        self.title = title
        self.price = price
        self.date = date

    def __str__(self):
        return f"제목:{self.title}, 가격:{self.price}, 출간 월:{self.date}"

    def getprice(self):
        print(self.title,"의 가격은", self.price,"원 입니다.")

if __name__ == '__main__':
    book1 = Book('소나기', 10000, 123, '황순원')
    book2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
    book3 = Book('난쟁이가 쏘아올린 작은 공', 12000, 112, '조세희')
    magazine1 = Magazine('보그',11000, 9)
    magazine2 = Magazine('싱글즈',13000, 8)
    print('', book1,'\n', book2, '\n', book3, '\n', magazine1, '\n', magazine2)
    print('총',Item.count,'권')
    book2.getprice()
    magazine1.getprice()
    book1.getprice()
