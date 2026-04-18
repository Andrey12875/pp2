class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


dog = Dog("asdf", 4)
print(dog.name)
print(dog.age)


class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand)
        self.speed = speed


car = Car("qwer", 120)
print(car.brand)
print(car.speed)


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade


student = Student("zxcv", 90)
print(student.name)
print(student.grade)


class Device:
    def __init__(self, model):
        self.model = model


class Phone(Device):
    def __init__(self, model, price):
        super().__init__(model)
        self.price = price


phone = Phone("hjkl", 300)
print(phone.model)
print(phone.price)


class Shape:
    def __init__(self, width):
        self.width = width


class Square(Shape):
    def __init__(self, width, height):
        super().__init__(width)
        self.height = height


square = Square(5, 5)
print(square.width)
print(square.height)


class Worker:
    def __init__(self, name):
        self.name = name


class Manager(Worker):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level


manager = Manager("tyui", 3)
print(manager.name)
print(manager.level)


class Food:
    def __init__(self, name):
        self.name = name


class Apple(Food):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price


apple = Apple("bnmv", 20)
print(apple.name)
print(apple.price)


class Game:
    def __init__(self, name):
        self.name = name


class Chess(Game):
    def __init__(self, name, players):
        super().__init__(name)
        self.players = players


chess = Chess("ghjk", 2)
print(chess.name)
print(chess.players)


class Tool:
    def __init__(self, name):
        self.name = name


class Hammer(Tool):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight


hammer = Hammer("vbnm", 6)
print(hammer.name)
print(hammer.weight)


class Account:
    def __init__(self, name):
        self.name = name


class Admin(Account):
    def __init__(self, name, active):
        super().__init__(name)
        self.active = active


admin = Admin("lkjh", True)
print(admin.name)
print(admin.active)