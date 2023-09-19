class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름:{self.name}, 나이:{self.age}"

class Dog(Pet):
    def bark(self, n):
        print("bark!")
        n -= 1
        if n == 0:
            return 0
        else:
            self.bark(n)

    def human_age(self):
        self.age *= 4
        return self.age

class Cat(Pet):
    def meow(self, n):
        print("meow~")
        n -= 1
        if n == 0:
            return 0
        else:
            self.meow(n)

    def human_age(self):
        self.age *= 4
        return self.age


if __name__ == '__main__':
    popo = Dog('popo', 10)
    popo.bark(3) 
    print(popo)
    print('사람 나이로 환산 :', popo.human_age())

    pipi = Cat('pipi', 5)
    pipi.meow(4) 
    print(pipi)
    print('사람 나이로 환산 :', pipi.human_age())
