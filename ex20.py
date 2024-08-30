class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

myCat1 = Cat("xiaobai", 3)
myCat2 = Cat("xiaohei", 2)

print(f'{myCat1.name} is {myCat1.age} years old\n{myCat2.name} is {myCat2.age} years old')

