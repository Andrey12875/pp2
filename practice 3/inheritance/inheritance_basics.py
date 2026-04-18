class Animal:
    def move(self):
        return "asdf"


class Dog(Animal):
    pass


dog = Dog()
print(dog.move())


class Vehicle:
    def start(self):
        return "qwer"


class Car(Vehicle):
    pass


car = Car()
print(car.start())


class Person:
    def speak(self):
        return "zxcv"


class Student(Person):
    pass


student = Student()
print(student.speak())


class Device:
    def turnon(self):
        return "hjkl"


class Phone(Device):
    pass


phone = Phone()
print(phone.turnon())


class Shape:
    def area(self):
        return 0


class Square(Shape):
    pass


square = Square()
print(square.area())


class Worker:
    def work(self):
        return "tyui"


class Manager(Worker):
    pass


manager = Manager()
print(manager.work())


class Food:
    def taste(self):
        return "bnmv"


class Apple(Food):
    pass


apple = Apple()
print(apple.taste())


class Game:
    def play(self):
        return "ghjk"


class Chess(Game):
    pass


chess = Chess()
print(chess.play())


class Tool:
    def use(self):
        return "vbnm"


class Hammer(Tool):
    pass


hammer = Hammer()
print(hammer.use())


class Account:
    def login(self):
        return True


class Admin(Account):
    pass


admin = Admin()
print(admin.login())