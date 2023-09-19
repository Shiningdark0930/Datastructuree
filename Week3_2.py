class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름:{self.name}, 나이:{self.age}"

class Dog(Pet):
    def bark(n):
        for i in n:
            print("bark!")

    def human_age(self):
        self.age *= 4

class Cat(Pet):
    def meow(n):
        for i in n:
            print("meow~")

    def human_age(self):
        self.age *= 4
