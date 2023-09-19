class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름:{self.name}, 나이:{self.age}"

class Dog:
    pass

class Cat:
    pass
