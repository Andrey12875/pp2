class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name


dog = Dog("asdf")
print(dog.speak())


class Cat:
    def __init__(self, color):
        self.color = color

    def show(self):
        return self.color


cat = Cat("qwer")
print(cat.show())


class Car:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        self.speed += 10
        return self.speed


car = Car(50)
print(car.move())


class Book:
    def __init__(self, pages):
        self.pages = pages

    def read(self):
        self.pages -= 10
        return self.pages


book = Book(200)
print(book.read())


class Phone:
    def __init__(self, charge):
        self.charge = charge

    def use(self):
        self.charge -= 5
        return self.charge


phone = Phone(100)
print(phone.use())


class Game:
    def __init__(self, level):
        self.level = level

    def up(self):
        self.level += 1
        return self.level


game = Game(3)
print(game.up())


class User:
    def __init__(self, active):
        self.active = active

    def change(self):
        self.active = not self.active
        return self.active


user = User(True)
print(user.change())


class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


box = Box(4, 6)
print(box.area())


class City:
    def __init__(self, people):
        self.people = people

    def add(self):
        self.people += 100
        return self.people


city = City(1000)
print(city.add())


class Student:
    def __init__(self, grade):
        self.grade = grade

    def passcheck(self):
        return self.grade >= 50


student = Student(90)
print(student.passcheck())