class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

p1 = Person('ganq', 45)
p2 = Person('ganq', 35)
p3 = Person('ganq', 25)
p4 = Person('ganq', 55)
p5 = Person('ganq', 65)
print(p1, p2, p3, p4, p5)

