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
        print("제목:", self.title,"가격:", self.price,"페이지 수:", self.page,"저자:", self.auther)

    def getprice(self):
        print(self.title,"의 가격은", self.price,"원 입니다.")

if __name__ == '__main__':
    book1 = Book('소나기', 10000, 123, '황순원')
    book2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
    book3 = Book('난쟁이가 쏘아올린 작은 공', 12000, 112, '조세희')
    print(book1,'\n',book2,'\n',book3,'\n')
